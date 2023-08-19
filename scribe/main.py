from src.transcribe_audio import transcribe_audio
from src.convert_audio import process_audio
import loguru
from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi.exceptions import HTTPException
from fastapi.middleware.cors import CORSMiddleware
from elevenlabs import APIError
from uvicorn.server import Server
from uvicorn.config import Config


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


@app.post("/transcription", tags=["voice_generation"])
def main(data):
    audio_file = data["audio_file"]
    audio_path = "./src/in/input_audio.mp3"
    with open(audio_path, "wb") as file:
        file.write(audio_file)
    audio_file = process_audio()
    try:
        return transcribe_audio(audio_file_name=audio_file)
    except HTTPException as erorr:
        logger.exception(f"API request failed: \n{erorr}\n{audio_file}")
        return JSONResponse(status_code=500, content={"error": str(erorr)})
    except APIError as erorr:
        logger.exception(f"API request failed: \n{erorr}\n{audio_file}")
        return JSONResponse(status_code=401, content={"error": str(erorr)})


@app.post("/minutes", tags=["minutes"])
def minutes(data):
    audio_data = data["audio_file"]
    audio_path = "./src/in/input_audio.mp3"
    with open(audio_path, "wb") as file:
        file.write(audio_data)


if __name__ == "__main__":
    server = Server(Config(app=app, host="localhost", port=8010, reload=True))
    server.run()
