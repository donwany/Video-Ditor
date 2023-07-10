from .utils import text_add, tuple_type
import argparse


def cli():
    parser = argparse.ArgumentParser(description="add text to video")
    parser.add_argument(
        "--input_vid", "-i", type=str, required=True, help="input video"
    )
    parser.add_argument(
        "--output_vid", "-o", type=str, required=True, help="output video"
    )
    parser.add_argument(
        "--screen_text", "-s", type=str, required=True, help="text to display on screen"
    )
    parser.add_argument(
        "--font_size", "-f", type=int, default=50, required=True, help="font size of text"
    )
    parser.add_argument(
        "--text_color", "-t", type=str, default="white", required=True, help="text color"
    )
    parser.add_argument(
        "--text_pos",
        "-p",
        type=tuple_type,
        default="center,top",
        # choices=["left", "center", "top", "right"],
        # required=True,
        help="position of text"
    )
    args = parser.parse_args()

    text_add(
        args.input_vid,
        args.output_vid,
        args.screen_text,
        args.font_size,
        args.text_color,
        args.text_pos,
    )


if __name__ == "__main__":
    cli()
