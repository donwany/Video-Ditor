import argparse

from loguru import logger

from .utils import concatenate_videos


def cli():
    parser = argparse.ArgumentParser(
        description="Video Concatenation"
    )
    parser.add_argument(
        "-c", "--clips",
        required=True,
        nargs="+",
        help="List of audio or video clip paths"
    )
    parser.add_argument(
        "-r",
        "--reduce",
        action="store_true",
        help="Whether to use the `reduce` method to reduce to the lowest quality on the resulting clip",
    )
    parser.add_argument(
        "-o",
        "--output",
        type=str,
        required=True,
        help="Output file name"
    )

    args = parser.parse_args()

    clips = args.clips
    output_path = args.output
    reduce = args.reduce

    method = "reduce" if reduce else "compose"

    logger.info("Joining list of videos ...")
    try:
        concatenate_videos(video_clips=clips, output_path=output_path, method=method)
    except Exception as e:
        logger.error(f"error: {e}")


if __name__ == "__main__":
    cli()
