from typing import Optional
import pydantic


class Data(pydantic.BaseModel):
    audio_file: str
    voice_id: Optional[str]

    @pydantic.validator("audio_file")
    @classmethod
    def audio_file_valid(cls, audio_file):
        if audio_file == "":
            raise ValueError("audio_file cannot be empty")
        else:
            return audio_file

