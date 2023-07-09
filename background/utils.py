from moviepy.editor import *
from loguru import logger


def add_background_video(
    back_video: str,
    overlay_video: str,
    output_video: str,
    over_pos: int,
    back_vol: float,
    over_vol: float,
):
    """adding background and overlay videos"""

    if back_video.lower().endswith(".mp4") and overlay_video.lower().endswith(".mp4"):
        # Load the videos
        background_clip = VideoFileClip(back_video)
        overlay_clip = VideoFileClip(overlay_video)

        # Increase the volume of the background clip to 100%
        if back_vol is not None:
            background_clip = background_clip.volumex(back_vol)

        # Reduce the volume of the overlay clip to 10%
        if over_vol is not None:
            overlay_clip = overlay_clip.volumex(over_vol)

        # Get the audio of the background video and set its volume to 0 for 3 seconds
        # background_audio = background_clip.audio
        # # background_audio_muted = background_audio.set_duration(180).volumex(0.0)
        # background_audio_muted = background_audio.volumex(0.1)
        #
        # # Extract the portion of the background audio that comes after the 26-second mute interval
        # background_audio_continued = background_audio.subclip(0.0, 4.00)
        #
        # # Concatenate the muted and continued audio clips
        # background_audio_final = CompositeAudioClip(
        #     [background_audio_muted, background_audio_continued]
        # )
        overlay_position = (None, None)
        if over_pos is not None:
            # Set the position of the overlay clip
            overlay_position = (over_pos, over_pos)  # pixels from top-left corner

        # Resize the overlay clip to match the size of the background clip
        overlay_clip = overlay_clip.resize(height=background_clip.h * 0.3)

        # Replace the original audio of the background video with the final audio clip
        # background = background_clip.set_audio(background_audio)

        # Overlay the clips
        final_clip = CompositeVideoClip(
            [background_clip, overlay_clip.set_pos(overlay_position)]
        )

        logger.info("Writing video to file ...")
        final_clip.write_videofile(
            output_video,
            codec="libx264",
            audio_codec="aac",
            fps=60,
            preset="ultrafast",
            temp_audiofile="temp-audio.m4a",
            remove_temp=True,
        )
    else:
        logger.error("Videos not in a valid format ...")
        sys.exit(1)
