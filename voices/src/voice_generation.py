import os
import json
import requests
from dotenv import load_dotenv
from pydub import AudioSegment
from voices import VoiceGenerations, Voice
from pydub.playback import play

load_dotenv()

CHUNK_SIZE = 1024

class VoiceGeneration(VoiceGenerations):
    def __init__(self):
        super().__init__(Voice())
        self.url = self.get_url
        self.api_key = os.environ.get("ELEVEN_LABS_API_KEY")

    def get_url(self, voice_id):
        voice_id = voice_id or "2EiwWnXFnvU5JabPnv8n"
        return self.url(f"{self.base_url}text-to-speech/{voice_id}/stream")
    
    def get_data(self, text):
        self.data = {
          "text": text,
          "model_id": "eleven_monolingual_v1",
          "voice_settings": {
            "stability": 0.5,
            "similarity_boost": 0.5
          }
        }
        return self.data
    
    def requests(self):
        response = requests.get(url=self.url, json=self.data, headers=self.headers)
        return response
    
    def generate_voice(self, text, voice_id):
        if not voice_id:
            voice_id = "2EiwWnXFnvU5JabPnv8n"
        self.url = self.get_url(voice_id=voice_id)
        self.data = self.get_data(text=text)
        
        response = self.requests()

        audio_data = b""
        for chunk in response.iter_content(chunk_size=self.CHUNK_SIZE):
            audio_data += chunk
        
        audio = AudioSegment.from_mp3(audio_data)
        play(audio)
        with open("/output/voice.mp3", "wb") as f:
            f.write(audio_data)
        if isinstance(audio_data, str):
            audio_data = audio_data.encode('utf-8')
        return audio_data

    def request_voice_list(self):
        response = requests()
        json_string = response.json()
        self.download_voices(json_string=json_string)   

    def download_voices(self, json_string):

        with open("voices.json", "r") as f:
            json_string = f.read()
            data_dict = json.loads(json_string)

        for voice in data_dict['voices']:
            self.add_voice(voice=voice)
                       
            name = name.replace(" ", "_")
            
            os.makedirs('voice/voice_samples', exist_ok=True)
            
            url = self.get_url(voice_id=voice['voice_id'])
            
                              
            response = requests.get(url)
            if response.status_code != 200:
                continue
            if response.status_code == 200:
                filename = f'voice/voice_samples/{name}_{voice_id}.mp3'
            
                with open(filename, 'wb') as f:
                    f.write(response.content)
            
            return f"files saved to {filename}"
         

    def add_voice(self, voice):
        voice = self.voice(
            name = voice['name'],
            voice_id = voice['voice_id'],
            age = voice['labels'].get('age'),
            gender = voice['labels'].get('gender'),
            accent = voice['labels'].get('accent'),
            description = voice.get('description'),
            use_case = voice['labels'].get('use case')
        )
        with open("voices/voice_choices.json", "a") as f:
            f.write(json.dumps(self.voices))
        
        self.voices.voices.append(voice)
        return voice
    
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

    def model_dump(self):
        return {
            "name": self.name,
            "voice_id": self.voice_id,
            "age": self.age,
            "gender": self.gender,
            "accent": self.accent,
            "description": self.description,
            "use_case": self.use_case
        }
    
    def model_load(self, json_string):
        self.name = json_string["name"]
        self.voice_id = json_string["voice_id"]
        self.age = json_string["age"]
        self.gender = json_string["gender"]
        self.accent = json_string["accent"]
        self.description = json_string["description"]
        self.use_case = json_string["use_case"]
        

        
if __name__ == "__main__":
   voice = VoiceGeneration()
   response = voice.generate_voice(text="hello", voice_id="D38z5RcWu1voky8WS1ja")