def has_image_extension(filename, extensions):
    """Check if a filename ends with any of the specified image extensions."""
    return any(filename.lower().endswith(ext) for ext in extensions)
