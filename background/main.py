from .utils import add_background_video
import argparse
from loguru import logger


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

    back_vid = args.back_vid
    overlay_vid = args.overlay_vid
    output_vid = args.output_vid
    overlay_pos = args.over_pos
    over_volume = args.over_vol
    back_vol = args.back_vol

    logger.info("adding background video and overlay video ...")
    add_background_video(
        back_video=back_vid,
        overlay_video=overlay_vid,
        output_video=output_vid,
        over_pos=overlay_pos,
        back_vol=back_vol,
        over_vol=over_volume,
    )


if __name__ == "__main__":
    cli()
