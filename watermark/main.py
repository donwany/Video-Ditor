import argparse

from loguru import logger
from moviepy.editor import *

from .utils import has_image_extension, tuple_type


def cli():
    parser = argparse.ArgumentParser(description="Add watermark videos/image")
    parser.add_argument("--input_vid", '-i', type=str, required=True, help="input video")
    parser.add_argument("--watermark", '-w', type=str, required=True, help="watermark image")
    parser.add_argument("--img_height", '-x', type=int, default=500, required=True, help="image height")
    parser.add_argument("--output_vid", '-o', type=str, required=True, help="output video")
    parser.add_argument("--position",
                        '-p',
                        type=tuple_type,
                        default="left,bottom",
                        # choices=["left", "center", "right", "top"],
                        help="watermark position")
    args = parser.parse_args()

    # List of image extensions to check
    image_extensions = ['.jpg', '.jpeg', '.png']

    # Load the video
    input_video = args.input_vid
    if input_video.lower().endswith(".mp4"):
        video = VideoFileClip(input_video)
        logger.info("Input video loaded successfully.")
    else:
        logger.info("Invalid video extension. Only .mp4 file format allowed.")
        return

    # Load the watermark image
    watermark = args.watermark
    if has_image_extension(watermark, image_extensions):
        watermark = ImageClip(watermark).resize(height=args.img_height)
        logger.info("Watermark image loaded successfully.")
    else:
        logger.info(f"Invalid watermark image. Only {image_extensions} allowed.")
        return

    # Set the duration of the watermark clip
    watermark = watermark.set_duration(video.duration)

    # Add the watermark to the video
    watermark_pos = args.position
    video_with_watermark = CompositeVideoClip(
        [video, watermark.set_position(watermark_pos)],
    )

    # Write the output video
    logger.info("Writing output video file...")
    video_with_watermark.write_videofile(
        args.output_vid,
        codec="libx264",
        audio_codec="aac",
        fps=60,
        temp_audiofile="temp-audio.mp4",
        remove_temp=True,
    )


if __name__ == "__main__":
    cli()
