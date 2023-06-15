"""Utilities
"""
import io
import re
import base64

from PIL import Image


def base64_to_pil(img_base64):
    """
    Convert base64 image data to PIL image
    """
    image_data = re.sub('^data:image/.+;base64,', '', img_base64)
    image_bytes = base64.b64decode(image_data)
    with io.BytesIO(image_bytes) as stream:
        pil_image = Image.open(stream)
        pil_image = pil_image.convert("RGB")  # Convert to RGB mode if needed
        return pil_image
