import os
import json
import requests
from dotenv import load_dotenv
from pydub import AudioSegment
from voices import Voice, Voices
from pydub.playback import play
from typing import Dict, List, Optional

load_dotenv()

CHUNK_SIZE = 1024


class VoiceGeneration(Voices):
    api_key: str = os.environ.get("ELEVEN_LABS_API_KEY")
    data: Dict[str, str] = {}
    base_url: str = "https://api.elevenlabs.io/v1/text-to-speech/"
    headers: Dict[str, str] = {
        "Accept": "audio/mpeg",
        "Content-Type": "application/json",
    }
    url: str = ""

    def set_url(self, voice_id):
        url = self.get_url(voice_id=voice_id)
        return url

    def get_url(self, voice_id):
        v_id = voice_id or "2EiwWnXFnvU5JabPnv8n"
        return f"{self.base_url}{v_id}/stream"

    def get_data(self, text):
        data = {
            "text": text,
            "model_id": "eleven_monolingual_v1",
            "voice_settings": {"stability": 0.5, "similarity_boost": 0.5},
        }
        return data

    def api_requests(self, text, voice_id):
        self.data = self.get_data(text=text)
        self.url = self.get_url(voice_id=voice_id)
        return requests.get(
            url=self.url, json=self.data, headers=self.headers, timeout=10000
        )

    def generate_voice(self, text, voice_id):
        if not voice_id:
            voice_id = "2EiwWnXFnvU5JabPnv8n"
        generate_response = self.api_requests(voice_id=voice_id, text=text)

        audio_data = b""
        for chunk in generate_response.iter_content(chunk_size=CHUNK_SIZE):
            audio_data += chunk

        audio = AudioSegment.from_mp3(audio_data)
        play(audio)
        with open("audio/out/output.mp3", "wb") as f:
            f.write(audio_data)
        if isinstance(audio_data, str):
            audio_data = audio_data.encode("utf-8")
        return audio_data

    def request_voice_list(self):
        json_string = requests.get(
            url=self.url, headers=self.headers, timeout=10000
        ).json()
        self.download_voices(json_string=json_string)

    def download_voices(self, json_string):
        filenames = []
        voice_data = []
        with open("audio/voices.json", "r", encoding="utf-8") as file:
            json_string = file.read()
            data_dict = json.loads(json_string)

        for download_voice in data_dict["voices"]:
            voice_data.append(download_voice)

            name = name.replace(" ", "_")

            os.makedirs("audio/voice_samples", exist_ok=True)

            voice_id = voice["voice_id"]

            url = self.get_url(voice_id)

            download_response = requests.get(url, timeout=10000)
            if response.status_code != 200:
                continue
            if download_response.status_code == 200:
                filename = f"audio/voice_samples/{name}_{voice_id}.mp3"

                with open(filename, "wb") as files:
                    files.write(response.content)
                filenames.append(filename)
        self.add_voices(voice_data)
        return f"files saved to {filenames}"

    def add_voice(self, voices_data):
        for voice_data in voices_data:
            added_voice = Voice(
                name=voice_data["name"],
                voice_id=voice_data["voice_id"],
                age=voice_data["labels"].get("age"),
                gender=voice_data["labels"].get("gender"),
                accent=voice_data["labels"].get("accent"),
                description=voice_data.get("description"),
                use_case=voice_data["labels"].get("use_case"),
            )
        self.voices.append(added_voice)
        return added_voice

    def get_voice_index_map(self, index):
        return self.voice_index_map[index]

    def get_voices(self):
        return self.voices

    def get_voice(self, index: int) -> Voice:
        """Returns the voice object at the specified index."""
        return self.voices[index]

    def get_voice_id(self, index: int) -> str:
        """Returns the voice ID of the voice at the specified index."""
        return self.get_voice(index).voice_id

    def get_voice_name(self, index: int) -> str:
        """Returns the name of the voice at the specified index."""
        return self.get_voice(index).name

    def get_voice_description(self, index: int) -> str:
        """Returns the description of the voice at the specified index."""
        return self.get_voice(index).description

    def get_voice_use_case(self, index: int) -> str:
        """Returns the use case of the voice at the specified index."""
        return self.get_voice(index).use_case


if __name__ == "__main__":
    voice = VoiceGeneration()
    response = voice.generate_voice(text="hello", voice_id="D38z5RcWu1voky8WS1ja")
