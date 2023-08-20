import os
from src.convert_audio import check_audio
from src.segment_audio import split_file
from src.transcribe_audio import transcribe_audio
import loguru

logger = loguru.logger


def process_audio(file_path: str):
    logger.info(f"Processing audio: {file_path}")
    audio_file = check_audio(audio_path=file_path)
    audio_file_paths = split_file(audio_file)
    for audio_file_path in audio_file_paths:
        transcribe_audio(audio_file_path)
        os.remove(audio_file_path)
    logger.info("Processing complete")
    with open("src/out/transcript.txt", "r", encoding="utf-8") as file:
        transcript = file.read()
    return transcript
