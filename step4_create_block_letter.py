"""
Step 4: Create a block letter "S" matching image dimensions.
This function creates a block letter "S" inside a numpy array and returns it as a 2D array with values in [0, 1].
"""

import numpy as np
from PIL import Image, ImageDraw, ImageFont
import os

def create_block_letter_s(height: int, width: int, letter: str = "S", font_size_ratio: float = 0.9) -> np.ndarray:
    """
    Create a block letter (default 'S') inside a numpy array.
    
    Args:
        height (int): Height of the output image.
        width (int): Width of the output image.
        letter (str): The letter to render (default "S").
        font_size_ratio (float): Ratio of font size relative to image height.
    
    Returns:
        np.ndarray: 2D array (height × width) with values in [0, 1].
                    Background = 1.0 (white), Letter = 0.0 (black).
    """
    # Create a white background image
    img = Image.new("L", (width, height), color=255)  # grayscale, white background
    draw = ImageDraw.Draw(img)

    # Estimate font size based on height
    font_size = int(height * font_size_ratio)

    # Try multiple font paths for bold sans-serif style
    possible_fonts = [
        "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",  # Linux
        "/Library/Fonts/Arial Bold.ttf",                        # macOS
        "C:/Windows/Fonts/arialbd.ttf",                         # Windows
    ]

    font = None
    for font_path in possible_fonts:
        if os.path.exists(font_path):
            try:
                font = ImageFont.truetype(font_path, font_size)
                break
            except Exception:
                continue

    # Fallback: default PIL font
    if font is None:
        font = ImageFont.load_default()

    # Get text bounding box
    text_bbox = draw.textbbox((0, 0), letter, font=font)
    text_width = text_bbox[2] - text_bbox[0]
    text_height = text_bbox[3] - text_bbox[1]

    # Center the text
    x = (width - text_width) // 2
    y = (height - text_height) // 2

    # Draw the letter (black = 0)
    draw.text((x, y), letter, font=font, fill=0)

    # Convert to numpy array, normalize to [0,1]
    arr = np.array(img, dtype=np.float32) / 255.0

    return arr


# Example usage (for testing):
if __name__ == "__main__":
    arr = create_block_letter_s(128, 128)
    print(arr.shape, arr.min(), arr.max())  # should be (128,128), 0.0, 1.0
