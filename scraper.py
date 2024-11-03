import yt_dlp
import os

class TikTokScaper:
    def __init__(self, output_dir):
        self.output_dir = output_dir 

    def download_videos(self, video_url_list):
            
        output_filename = "%(title)s.mp4"  # This will save with the video title and .mp4 extension

        # Create the downloads directory if it doesn't exist
        os.makedirs(self.output_dir, exist_ok=True)

        # Set options for yt-dlp
        ydl_opts = {
            'format': 'mp4',  # Prioritize MP4 format
            'outtmpl': os.path.join(self.output_dir, output_filename),  # Define the output path with .mp4 extension
            'quiet': False,
            'no_warnings': True,
        }
        

        for video_url in video_url_list:


            try:
                with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                    print(f"Downloading TikTok video from {video_url}")
                    info = ydl.extract_info(video_url, download=True)
                    print("Download complete.")
                    print("Video saved at:", os.path.join(self.output_dir, f"{info['title']}.mp4"))

            except Exception as e:
                print("Error downloading video:", str(e))

scraper_obj = TikTokScaper("doownloads")


video_urls = ["https://www.tiktok.com/@mrbeast/video/7428620743832784158?lang=en", "https://www.tiktok.com/@mrbeast/video/7427550814698360094?lang=en"]

scraper_obj.download_videos(video_urls)