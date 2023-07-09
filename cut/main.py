import argparse
from .utils import cut_video
from loguru import logger


def cli():
    parser = argparse.ArgumentParser(description="cut videos")
    parser.add_argument(
        "--input_vid", "-i", type=str, required=True, help="input video"
    )
    parser.add_argument(
        "--output_vid", "-o", type=str, required=True, help="output video"
    )
    parser.add_argument(
        "--start_time", "-s", type=str, required=True, help="start time in (seconds)"
    )
    parser.add_argument(
        "--end_time", "-e", type=str, required=True, help="end time in (seconds)"
    )
    args = parser.parse_args()

    input_vid = args.input_vid
    output_vid = args.output_vid
    start = args.start_time
    end = args.end_time

    logger.info("Cutting video ...")
    cut_video(
        input_vid=input_vid, start_time=start, end_time=end, output_vid=output_vid
    )


if __name__ == "__main__":
    cli()
