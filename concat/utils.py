import sys

from loguru import logger
from moviepy.editor import VideoFileClip, concatenate_videoclips


def concatenate_videos(video_clips, output_path, method="compose"):
    """Concatenate videos"""
    if len(video_clips) == 1:
        logger.warning("Only one video clip provided for concatenation. Need at least one video.")
        sys.exit(1)

    clips = [VideoFileClip(clip) for clip in video_clips]

    if method == "reduce":
        # Calculate minimum width & height across all clips
        min_height = min(c.h for c in clips)
        min_width = min(c.w for c in clips)
        # Resize the videos to the minimum
        clips = [c.resize(newsize=(min_width, min_height)) for c in clips]

    # Concatenate the videos
    final_clip = concatenate_videoclips(clips, method=method)

    logger.info("Writing video to file...")
    final_clip.write_videofile(
        filename=output_path,
        codec="libx264",
        audio_codec="aac",
        fps=30,
        temp_audiofile="temp-audio.m4a",
        remove_temp=True,
    )
