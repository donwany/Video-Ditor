from moviepy.editor import VideoFileClip, TextClip, CompositeVideoClip
import argparse


def tuple_type(s):
    try:
        # Assuming the tuple-like value is provided in the format "value1,value2"
        values = s.split(",")
        # Convert values to a tuple
        tuple_values = tuple(values)
        return tuple_values
    except Exception as e:
        raise argparse.ArgumentTypeError(f"Invalid tuple-like format: {s}") from e


def text_add(
    input_vid: str,
    output_vid: str,
    screen_text: str,
    font_size: int,
    text_color: str,
    text_pos: str,
):
    # Load the video clip
    video = VideoFileClip(input_vid)

    # Create a TextClip
    text_clip = TextClip(screen_text, fontsize=font_size, color=text_color, font='Arial-Bold')

    # Position the text on the video
    text_clip = text_clip.set_position(text_pos).set_duration(video.duration)

    # Composite the video and text
    final_clip = CompositeVideoClip([video, text_clip])

    # # Step 4: Create a TextClip
    # text_clip = TextClip(
    #     screen_text, fontsize=font_size, color=text_color, font="Arial-Bold"
    # )
    #
    # # Step 5: Position the text on the video
    # text_clip = text_clip.set_position((text_pos, "bottom")).set_duration(
    #     video.duration
    # )
    #
    # # Step 6: Add a background to the text
    # background_clip = TextClip(
    #     "", fontsize=55, color="blue", font="Arial-Bold"
    # ).set_duration(video.duration)
    #
    # background_clip = background_clip.set_position(("center", "bottom")).set_opacity(0.5)
    #
    # # Step 7: Composite the video and text
    # final_clip = CompositeVideoClip([video, background_clip, text_clip])

    final_clip.write_videofile(
        output_vid,
        codec="libx264",
        audio_codec="aac",
        fps=60,
        temp_audiofile="temp-audio.mp4",
        remove_temp=True,
    )
