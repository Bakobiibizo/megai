from src.voice_generation import VoiceGeneration

class Voice():
    def __init__(self):
        self.eleven_labs = VoiceGeneration()
        self.voices = self.eleven_labs.voices

    def generate(self, text, voice_id="2EiwWnXFnvU5JabPnv8n"):
        self.eleven_labs.generate_voice(text=text, voice_id=voice_id)
        

if __name__ == "__main__":
    with open("input/input.txt") as file:
        text = file.read()
    
    voice = Voice()
    voice.generate(text=text, voice_id="2EiwWnXFnvU5JabPnv8n")