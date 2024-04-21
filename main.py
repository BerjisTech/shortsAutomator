from video_editor import VideoEditor
from content_fetcher import ContentFetcher
from voice_generator import VoiceGenerator
from music_selector import MusicSelector

def main():
    # Initialize components
    content_fetcher = ContentFetcher()
    voice_generator = VoiceGenerator()
    music_selector = MusicSelector()
    video_editor = VideoEditor()

    # Fetch content
    gameplay_video = content_fetcher.get_gameplay_video()
    lifestyle_images = content_fetcher.get_lifestyle_images()
    voiceover_text = "Quotes or stories surrounding Black American communities."
    voiceover_audio = voice_generator.generate_voiceover(voiceover_text)
    background_music = music_selector.select_music()

    # Create video
    video_editor.create_split_screen_video(gameplay_video, lifestyle_images)
    video_editor.add_voiceover(voiceover_audio)
    video_editor.add_background_music(background_music)
    video_editor.export_video("output_video.mp4")

if __name__ == "__main__":
    main()