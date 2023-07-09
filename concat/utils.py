from moviepy.editor import *
from loguru import logger


def concatenate_videos(video_clips, output_path, method="compose"):
    """concatenate videos"""
    global final_clip
    clips = [VideoFileClip(clip) for clip in video_clips]

    if method == "reduce":
        # calculate minimum width & height across all clips
        min_height = min([c.h for c in clips])
        min_width = min([c.w for c in clips])
        # resize the videos to the minimum
        clips = [c.resize(newsize=(min_width, min_height)) for c in clips]
        # Concatenate the videos
        final_clip = concatenate_videoclips(clips)
    elif method == "compose":
        # concatenate the final video with the compose method provided by moviepy
        final_clip = concatenate_videoclips(clips, method="compose")

    logger.info("Writing video to file ...")
    final_clip.write_videofile(
        filename=output_path,
        codec="libx264",
        audio_codec="aac",
        fps=30,
        temp_audiofile="temp-audio.m4a",
        remove_temp=True,
    )
