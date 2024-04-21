from gtts import gTTS

class VoiceGenerator:
    def generate_voiceover(self, text):
        tts = gTTS(text=text, lang='en')
        tts.save("voiceover.mp3")
        return "voiceover.mp3"