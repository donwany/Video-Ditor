import argparse

from loguru import logger

from .utils import Args, cut_video, validate_args


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

    # Create an instance of Args
    input_args = Args(
        input_vid=args.input_vid,
        output_vid=args.output_vid,
        start_time=args.start_time,
        end_time=args.end_time,
    )

    # Validate the input arguments
    validate_args(input_args)

    logger.info("Cutting video ...")
    cut_video(
        input_vid=input_args.input_vid,
        start_time=input_args.start_time,
        end_time=input_args.end_time,
        output_vid=input_args.output_vid,
    )


if __name__ == "__main__":
    cli()
