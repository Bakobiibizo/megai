from typing import Dict, List, Optional
from pydantic import BaseModel


class Voice(BaseModel):
    name: str
    voice_id: str
    age: str
    gender: str
    accent: Optional[str] = None
    description: Optional[str] = None
    use_case: Optional[str] = None


class Voices(BaseModel):
    voice: Voice = Voice(
        name="Rachel",
        voice_id="21m00Tcm4TlvDq8ikWAM",
        age="young",
        gender="female",
        accent="american",
        description="low energy mid ranged female voice, good for npcs and characters not enjoying what they are doing",
        use_case="npc voice",
    )
    voices: list[Voice] = [voice]
    voice_index_map: list[Dict[str, str]] = []

    def get_url(self, voice_id: Optional[str]) -> str:
        pass

    def get_data(self, text: str) -> Dict[str, str]:
        pass

    def api_requests(self) -> str:
        pass

    def request_voice_list(self) -> List[Voice]:
        pass

    def download_voices(self, json_string) -> None:
        pass

    def generate_voice(self, text: str, voice_id: Optional[str]) -> bytes:
        pass

    def add_voice(self, voice_data: str) -> Voice:
        pass

    def get_voice_index_map(self, index: int) -> Dict[str, str]:
        pass

    def get_voices(self) -> List[Voice]:
        pass
