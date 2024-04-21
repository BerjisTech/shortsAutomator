from gtts import gTTS
import os

class NarrationGenerator:
    """Generates AI voice narrations."""
    
    @staticmethod
    def generate_narration(text, output_path):
        """Generates a narration from the given text."""
        tts = gTTS(text=text, lang='en')
        tts.save(output_path)