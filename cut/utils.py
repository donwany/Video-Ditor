import datetime
import os
from dataclasses import dataclass

from loguru import logger
from moviepy.video.io.VideoFileClip import VideoFileClip


@dataclass
class Args:
    input_vid: str
    output_vid: str
    start_time: str
    end_time: str


def validate_args(args: Args):
    # Validate file paths
    if not os.path.isfile(args.input_vid):
        raise ValueError("Invalid input video file path.")
    if os.path.isfile(args.output_vid):
        raise ValueError("Output video file already exists.")

    # Validate start and end times
    try:
        start_time = datetime.datetime.strptime(args.start_time, "%H:%M:%S")
        end_time = datetime.datetime.strptime(args.end_time, "%H:%M:%S")
    except ValueError:
        raise ValueError("Start time and end time must be in the format HH:MM:SS.")

    if start_time > end_time:
        raise ValueError("Start time must be before end time.")


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
