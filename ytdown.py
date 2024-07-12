import yt_dlp as youtube_dl

def download_video(url, save_path):
    ydl_opts = {
        'outtmpl': f'{save_path}/%(title)s.%(ext)s',
        'format': 'bestvideo+bestaudio/best',
        'merge_output_format': 'mp4',
    }
    
    try:
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        print("Video downloaded successfully.")
    except Exception as e:
        print(e)

url = "https://www.youtube.com/watch?v=KlyPKbrlBsQ"
save_path = "/Users/hckmar/Documents/Code/python/automations/yt-downloader/videos"

download_video(url, save_path)