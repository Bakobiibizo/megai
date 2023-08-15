from pathlib import Path
from typing import Optional

from openai.error import OpenAIError

from api import transcribe_audio
from audio import AudioProcessor
from logger import logger
from minutes import meeting_minutes
from text import format_minutes, format_transcript

logger = logger.get_logger(__name__)



def scriber(in_d: Optional[str], out_d: Optional[str] = None) -> Optional[str]:
    """
    @param in_d: Optional input directory path where the audio files are located. If not provided, it defaults to
    "src/in/".
    @param out_d: Optional output directory path where the meeting minutes will be saved. If not provided,
    it defaults to "src/out/".
    @param in_d: Optional input directory path where the audio files are located. If not provided, it defaults to
    "src/in/".
    @return: The generated meeting minutes as a string.


    This method takes in an input directory path and an optional output directory path. It processes audio files in
    the input directory, transcribes them, generates meeting minutes, and saves them as a file in the output
    directory. The method returns the generated meeting minutes as a string.

    If the input directory or output directory does not exist or is not accessible, an error is logged and None is
    returned.

    Usage example:
        in_directory = "path/to/input"
        out_directory = "path/to/output"
        result = scriber(in_directory, out_directory)
        print(result)
    """

    logger.info("Starting Scriber...")

    # Use the input directory parameter or default to "src/in/"
    in_directory = in_d or "src/in/"

    # Use the output directory parameter or default to "src/out/"
    out_directory = out_d or "src/out/"

    # Check if the input directory exists and is accessible
    if not Path(in_directory).is_dir():
        logger.error(
            f"Input directory does not exist or is not accessible: {in_directory}"
        )
        return None

    # Check if the output directory exists and is accessible
    if not Path(out_directory).is_dir():
        logger.error(
            f"Output directory does not exist or is not accessible: {out_directory}"
        )
        return None

    # Create an instance of AudioProcessor with the input and output directories
    audio = AudioProcessor(in_directory, out_directory)

    # Get the list of file paths in the input directory
    file_paths = [
        str(file)
        for file in Path(in_directory).rglob("*")
        if file.suffix in {".mp4", ".mkv"}
    ]

    # Check the file types and lengths
    files = audio.check_file_types(file_paths)
    audio_chunks = audio.check_file_length(files)

    # Segment the audio into smaller chunks
    segments = audio.segment_audio(audio_chunks)

    max_retries = 3
    full_minutes = ""
    for i, segment in enumerate(segments):
        temp_file_name = f"src/out/temp_{i}.mp3"
        try:
            segment.export(temp_file_name, format="mp3")
        except Exception as e:
            logger.error(f"Error occurred while exporting segment: {e}")
            continue

        retries = 0
        transcription = None
        while not transcription and retries < max_retries:
            try:
                transcription = transcribe_audio(
                    model="GPT-4", audio_file_path=temp_file_name, out_dir=out_directory
                )
            except Exception as e:
                logger.error(f"Error occurred while transcribing audio: {e}")
                retries += 1
                continue

        if not transcription:
            logger.info(f"No transcription available for {temp_file_name}.")
            continue

        try:
            # Generate meeting minutes from the transcription
            full_minutes += meeting_minutes(
                audio_file_name=transcription,
                roles_and_extracted_info=(),
                timestamp="%Y-%m-%d %H:%M:%S",
                transcription=transcription,
            )

        except FileNotFoundError as e:
            logger.error(f"File not found: {e}")
        except PermissionError as e:
            logger.error(f"Permission error: {e}")
        except OpenAIError as e:
            logger.error(f"API error: {e}")
        except Exception as e:
            logger.error(f"Error occurred while processing audio: {e}")
            return None

        # Remove the temporary audio file
        if Path(temp_file_name).exists():
            Path(temp_file_name).unlink()

    # Save the minutes as a file and format the minutes for readability
    format_transcript()
    pretty_minutes = format_minutes(full_minutes)

    logger.info(f"Complete, check {out_directory} for results.")
    return pretty_minutes


if __name__ == "__main__":
    logger.log("Running main scriber...")
    in_dir = "src/in"
    out_dir = "src/out"
    result = scriber(in_dir, out_dir)
    print(result)
