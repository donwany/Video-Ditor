import argparse

from loguru import logger
from moviepy.editor import *
from .utils import has_image_extension


def cli():
    parser = argparse.ArgumentParser(description="Add watermark videos/image")
    parser.add_argument("--input_vid", '-i', type=str, required=True, help="input video")
    parser.add_argument("--watermark", '-w', type=str, required=True, help="watermark image")
    parser.add_argument("--img_height", '-x', type=int, default=500, required=True, help="image height")
    parser.add_argument("--output_vid", '-o', type=str, required=True, help="output video")
    parser.add_argument("--position",
                        '-p',
                        type=str,
                        default="left",
                        choices=["left", "center", "right", "top"],
                        help="watermark position")
    args = parser.parse_args()

    input_video = args.input_vid
    watermark = args.watermark
    img_height = args.img_height
    output_vid = args.output_vid
    watermark_pos = args.position

    # List of image extensions to check
    image_extensions = ['.jpg', '.jpeg', '.png']

    # Load the video
    if input_video.lower().endswith(".mp4"):
        video = VideoFileClip(input_video)
        logger.info("Video extension valid ...")
    else:
        logger.info("Video extension not valid ...")
        sys.exit(1)
    # Load the watermark image
    if has_image_extension(watermark, image_extensions):
        watermark = ImageClip(watermark).resize(height=img_height)
        logger.info("filename is an image file ...")
    else:
        logger.info("filename is not an image file ...")
        sys.exit(1)

    # Set the duration of the watermark clip
    watermark = watermark.set_duration(video.duration)
    # Add the watermark to the video
    video_with_watermark = CompositeVideoClip(
        [video, watermark.set_position((watermark_pos, "bottom"))]
    )

    # Write the output video
    logger.info("Writing video file ...")
    video_with_watermark.write_videofile(
        output_vid,
        codec="libx264",
        audio_codec="aac",
        fps=60,
        temp_audiofile="temp-audio.mp4",
        remove_temp=True,
    )


if __name__ == "__main__":
    cli()
