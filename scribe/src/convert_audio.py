import os
from moviepy.editor import AudioFileClip
import loguru


logger = loguru.logger


def process_audio():
    try:
        in_dir = "./src/in/"
        in_dir = os.path.abspath(in_dir)
        movie_suffix = [".mp4", ".mkv"]
        audio_suffix = [".mp3", ".wav"]
        audio_file_path = None
        for file in os.listdir(in_dir):
            video_file_path = os.path.join(in_dir, file)

            if any(file.endswith(suffix) for suffix in movie_suffix):
                video = AudioFileClip(video_file_path)
                audio_file_path = os.path.join(in_dir, f"{os.path.splitext(file)[0]}.mp3")
                video.write_audiofile(audio_file_path)
            elif any(file.endswith(suffix) for suffix in audio_suffix):
                audio_file_path = os.path.join(in_dir, file)

            if audio_file_path:
                return audio_file_path
    except FileNotFoundError as error:
        logger.exception(f"No file found {audio_file_path}{error}.")

if __name__ == "__main__":
    process_audio()
    