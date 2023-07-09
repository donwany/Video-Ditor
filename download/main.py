import argparse

import yt_dlp
from loguru import logger


def download_video(url):
    ydl_opts = {
        'outtmpl': '%(title)s.%(ext)s',
        'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best',
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])


def cli():
    parser = argparse.ArgumentParser(
        description="download youtube video"
    )
    parser.add_argument(
        "--url", "-u", type=str, required=True, help="youtube video url"
    )

    args = parser.parse_args()

    video_url = args.url
    logger.info(f"Downloading from : {video_url}")
    download_video(video_url)


if __name__ == '__main__':
    cli()
