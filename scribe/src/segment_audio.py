import os
import loguru
from pydub import AudioSegment

logger = loguru.logger


def split_file(file_path_str: str, chunk_length_ms: int = 10 * 40 * 512):
    logger.info(f"Splitting file: {file_path_str}")
    if not os.path.exists(file_path_str):
        raise FileNotFoundError(f"File {file_path_str} not found.")

    audio = AudioSegment.from_mp3(file_path_str)
    audio_files = []

    for i, chunk in enumerate(audio[::chunk_length_ms]):
        chunk_file_name = f"src/audio_temp/chunk_{i + 1}.mp3"
        chunk.export(chunk_file_name, format="mp3")
        audio_files.append(chunk_file_name)
    logger.info("Split complete")
    return audio_files


if __name__ == "__main__":
    split_file("./src/in/input_audio.mp3")
