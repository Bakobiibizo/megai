import openai
from dotenv import load_dotenv
from typing import Optional
import os

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")
def transcribe_audio(audio_file_name) -> str:
    out_file = "./src/out/transcript.txt"
    try:
        lines = []
        with open(audio_file_name, "rb") as audio_file:
            transcript_dict = openai.Audio.transcribe("whisper-1", audio_file)
            transcription: str = transcript_dict["text"]

            lines = transcription.split(".")       
            with open (out_file, "w", encoding="utf-8") as file:
                for line in lines:
                    file.writelines(line.split(".")[0]+".\n")
        return out_file

    except FileNotFoundError:
        print(f"File {out_file} not found.")
        return None
    