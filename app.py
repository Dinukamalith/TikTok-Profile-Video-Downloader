import os
import yt_dlp

def download_tiktok_profile_videos(profile_url, download_path='downloads'):
    # Ensure the download directory exists
    if not os.path.exists(download_path):
        os.makedirs(download_path)

    # yt-dlp options
    ydl_opts = {
        'outtmpl': os.path.join(download_path, '%(uploader)s_%(upload_date)s_%(id)s.%(ext)s'),
        'format': 'bestvideo+bestaudio/best',
        'merge_output_format': 'mp4',
        'noplaylist': False,  # Ensure playlists are downloaded
        'extract_flat': True,  # Get video URLs without downloading
        'quiet': False,
        'no_warnings': True,
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        # Extract video information
        result = ydl.extract_info(profile_url, download=False)
        if 'entries' in result:
            # It's a playlist or a profile with multiple videos
            video_urls = [entry['url'] for entry in result['entries']]
            print(f'Found {len(video_urls)} videos. Starting download...')
            for video_url in video_urls:
                try:
                    ydl.download([video_url])
                except Exception as e:
                    print(f'Error downloading {video_url}: {e}')
        else:
            # Single video
            print('Found a single video. Starting download...')
            ydl.download([profile_url])

if __name__ == "__main__":
    tiktok_profile_url = input("Enter the TikTok profile URL: ")
    download_directory = input("Enter the download directory (default is 'downloads'): ") or 'downloads'
    download_tiktok_profile_videos(tiktok_profile_url, download_directory)
