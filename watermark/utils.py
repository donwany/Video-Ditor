import argparse


def has_image_extension(filename, extensions):
    """Check if a filename ends with any of the specified image extensions."""
    return any(filename.lower().endswith(ext) for ext in extensions)


def tuple_type(s):
    try:
        # Assuming the tuple-like value is provided in the format "value1,value2"
        values = s.split(",")
        # Convert values to a tuple
        tuple_values = tuple(values)
        return tuple_values
    except Exception as e:
        raise argparse.ArgumentTypeError(f"Invalid tuple-like format: {s}") from e
