import argparse

from loguru import logger

from .utils import Args, add_background_video, validate_args


def cli():
    parser = argparse.ArgumentParser(
        description="add background video to overly videos"
    )
    parser.add_argument(
        "--back_vid", "-b", type=str, required=True, help="background video"
    )
    parser.add_argument(
        "--overlay_vid", "-o", type=str, required=True, help="overlay video"
    )
    parser.add_argument(
        "--output_vid", "-x", type=str, required=True, help="output video"
    )
    parser.add_argument(
        "--over_pos",
        "-p",
        default=150,
        type=int,
        required=True,
        help="overlay video position",
    )
    parser.add_argument(
        "--over_vol",
        "-v",
        default=0.10,
        type=float,
        required=True,
        help="overlay video volume",
    )
    parser.add_argument(
        "--back_vol",
        "-bv",
        default=1.0,
        type=float,
        required=True,
        help="background video volume",
    )
    args = parser.parse_args()

    # Create an instance of Args
    input_args = Args(
        back_vid=args.back_vid,
        overlay_vid=args.overlay_vid,
        output_vid=args.output_vid,
        over_pos=args.over_pos,
        over_vol=args.over_vol,
        back_vol=args.back_vol,
    )

    # Validate the input arguments
    validate_args(input_args)

    # back_vid = args.back_vid
    # overlay_vid = args.overlay_vid
    # output_vid = args.output_vid
    # overlay_pos = args.over_pos
    # over_volume = args.over_vol
    # back_vol = args.back_vol

    logger.info("adding background video and overlay video ...")
    add_background_video(
        back_video=input_args.back_vid,
        overlay_video=input_args.overlay_vid,
        output_video=input_args.output_vid,
        over_pos=input_args.over_pos,
        back_vol=input_args.back_vol,
        over_vol=input_args.over_vol,
    )


if __name__ == "__main__":
    cli()
