from moviepy.video.io.VideoFileClip import VideoFileClip
from loguru import logger


def cut_video(input_vid, start_time, end_time, output_vid):
    # Load the video clip
    clip = VideoFileClip(input_vid)

    # Cut the video from 00:01:30 to 00:02:30
    # start_time = 90  # in seconds
    # end_time = 150   # in seconds
    cut_clip = clip.subclip(start_time, end_time)

    # Save the cut clip to a file
    logger.info("Saving the cut video to file ...")
    cut_clip.write_videofile(output_vid,
                             codec='libx264',
                             audio_codec='aac',
                             fps=60,
                             preset="ultrafast", )
    logger.info("SUCCESS")
