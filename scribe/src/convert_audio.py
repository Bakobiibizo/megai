import os
from typing import List
from moviepy.editor import AudioFileClip
import loguru


logger = loguru.logger


def convert_audio(
    file_path: str, audio_file_path: str, supported_suffix: List[str]
) -> str:
    logger.info(f"Checking and converting to audio: {file_path}")
    audio_file_path = ""

    for suffix in supported_suffix:
        if file_path.endswith(suffix):
            file = AudioFileClip(file_path)
            audio_file_path = file_path.replace(suffix, "mp3")
            file.write_audiofile(audio_file_path)
            file.close()
    if file_path.endswith(".mp3") is False:
        raise TypeError(f"{file_path} is not a valid file type.")
    logger.info("Conversion check complete")
    return audio_file_path


def check_audio(audio_path: str) -> str:
    supported_suffix = [
        "m4a",
        "mp3",
        "webm",
        "mp4",
        "mpga",
        "wav",
        "mpeg",
        "ogg",
        "oga",
        "flac",
    ]
    logger.info("Checking audio files")
    folder_path = "./src/out/"
    audio_file_path = convert_audio(
        file_path=audio_path,
        audio_file_path=folder_path,
        supported_suffix=supported_suffix,
    )
    logger.info("Check complete")
    return audio_file_path


if __name__ == "__main__":
    check_audio("src/in/input_audio.mp3")
