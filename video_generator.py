from video_editor import VideoEditor
from narration_generator import NarrationGenerator
from media_downloader import MediaDownloader
from pytube import YouTube

class VideoGenerator:
    """Orchestrates the video creation process."""
    
    def __init__(self):
        # Initialize components
        self.video_editor = VideoEditor()
        self.narration_generator = NarrationGenerator()
        self.media_downloader = MediaDownloader()

    def download_youtube_video(self, url, output_path):
        YouTube(url).streams.first().download(output_path)

    def download_youtube_audio(self, url, output_path):
        YouTube(url).streams.filter(only_audio=True).first().download(output_path)

    def generate_video(self, gameplay_video_url, image_url, music_url, narration_text, output_path):
        """Generates a YouTube shorts video."""
        # Download media
        gameplay_video_path = "temp_gameplay.mp4"
        self.media_downloader.download_file(gameplay_video_url, gameplay_video_path)
        
        image_path = "temp_image.jpg"
        self.media_downloader.download_file(image_url, image_path)
        
        music_path = "temp_music.mp3"
        self.media_downloader.download_file(music_url, music_path)
        
        # Generate narration
        narration_path = "temp_narration.mp3"
        self.narration_generator.generate_narration(narration_text, narration_path)
        
        # Create split-screen video
        split_screen_path = "temp_split_screen.mp4"
        self.video_editor.create_split_screen(gameplay_video_path, image_path, split_screen_path)
        
        # Add background music
        self.video_editor.add_background_music(split_screen_path, music_path, output_path)
        
        # Cleanup temporary files
        # os.remove(gameplay_video_path)
        # os.remove(image_path)
        # os.remove(music_path)
        # os.remove(narration_path)
        # os.remove(split_screen_path)

if __name__ == "__main__":
    generator = VideoGenerator()

    generator.download_youtube_video('https://www.youtube.com/watch?v=iZHwRpRCo1o&ab_channel=DarkViperAU', 'gameplay.mp4')
    generator.download_youtube_audio('https://www.youtube.com/watch?v=H7_sqdkaAfo&ab_channel=whitneyhoustonVEVO', 'music.mp3')

    generator.generate_video(
        gameplay_video_path="gameplay.mp4",
        image_url="https://www.census.gov/content/dam/Census/library/stories/2023/10/2020-census-dhc-a-black-population/black-or-african-american.jpg",
        music_path="music.mp3",
        narration_text="Some inspirational quotes or stories",
        output_path="final_video.mp4"
    )