import yt_dlp as youtube_dl

def download_video(url, save_path):
    ydl_opts = {
        'outtmpl': f'{save_path}/%(title)s.%(ext)s',
        # For the best quality available
        'format': 'bestvideo+bestaudio/best',
        # The most common format for me
        'merge_output_format': 'mp4',
    }
    
    try:
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        print("Video downloaded successfully.")
    # In case something goes wrong
    except Exception as e:
        print(e)

url = "youtbe-link" # We replace the url of the video we want to download
save_path = "your_path+the-folder-I-created" #the path to save the video, I use pwd to make it easier and defined a folder in the root called videos.

download_video(url, save_path)