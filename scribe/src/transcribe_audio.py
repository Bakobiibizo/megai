import openai
from dotenv import load_dotenv
import loguru
import os

logger = loguru.logger

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")


def transcribe_audio(audio_file_name) -> str:
    logger.info(f"Transcribing audio: {audio_file_name}")
    out_file = "./src/out/transcript.txt"
    try:
        lines = []
        with open(audio_file_name, "rb") as audio_file:
            transcription = openai.Audio.transcribe("whisper-1", audio_file)
            transcript = transcription["text"]
            logger.info(f"{transcript}")
            lines.append(transcript.split(".", -1))
            logger.debug(lines)
            with open(out_file, "a", encoding="utf-8") as file:
                for line in lines[0]:
                    if line == "":
                        continue
                    logger.debug(line)
                    file.writelines(f"{line}.\n")
        logger.info("Transcribed")

    except FileNotFoundError as error:
        raise FileNotFoundError(
            f"{logger.exception(f'File {out_file} not found: {error}')}"
        ) from error


if __name__ == "__main__":
    audio_temp = "src/audio_temp/"
    chunks = os.listdir(audio_temp)
    for chunk in chunks:
        logger.info(f"Transcribing audio: {chunk}")
        if chunk.endswith(".mp3"):
            transcribe_audio(audio_temp + chunk)
