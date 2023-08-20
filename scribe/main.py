from src.process_audio import process_audio
import loguru
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from uvicorn.server import Server
from uvicorn.config import Config
import os


logger = loguru.logger

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


def save_audio(file_path: str):
    with open(file_path, "rb") as file:
        audio_file = file.read()
    audio_file_path = "./src/in/input_audio.mp3"
    with open(audio_file_path, "wb") as file:
        file.write(audio_file)
    return audio_file_path


def save_transcript(file_path: str, transcript: str):
    path = f"{os.path.splitext(file_path)[0]}.txt"
    with open(
        f"C:/Users/richa/OneDrive/Documents/{path}", "w", encoding="utf-8"
    ) as file:
        file.write(transcript)
    os.remove(file_path)


@app.post("/transcription", tags=["voice_generation"])
def main(data):
    logger.info(f"Processing audio: {data.audio_file_path}")
    file_path = save_audio(data.audio_file_path)
    transcript = process_audio(file_path=file_path)
    save_transcript(data.audio_file_path, transcript)
    return transcript


@app.post("/minutes", tags=["minutes"])
def minutes(data):
    audio_data = data["audio_file"]
    audio_path = "./src/in/input_audio.mp3"
    with open(audio_path, "wb") as file:
        file.write(audio_data)


if __name__ == "__main__":
    server = Server(Config(app=app, host="localhost", port=8010, reload=True))
    server.run()
