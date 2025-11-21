"""
Step 5: Create a masked stipple image by applying a block letter mask.
This function applies a block letter mask to a stippled image and returns a masked image.
"""

import numpy as np

def create_masked_stipple(stipple_img: np.ndarray, mask_img: np.ndarray, threshold: float = 0.5) -> np.ndarray:
    """
    Apply a block letter mask to a stippled image.
    
    Args:
        stipple_img (np.ndarray): 2D array of stippled image values in [0,1].
        mask_img (np.ndarray): 2D array of mask values in [0,1].
        threshold (float): Threshold below which mask is considered "dark" (mask area).
    
    Returns:
        np.ndarray: Masked stipple image (same shape as inputs).
                    - Where mask < threshold → set to 1.0 (white, stipples removed).
                    - Where mask >= threshold → keep stipple values.
    """
    if stipple_img.shape != mask_img.shape:
        raise ValueError(f"Shape mismatch: stipple_img {stipple_img.shape} vs mask_img {mask_img.shape}")

    # Apply mask: dark areas become white (1.0), light areas keep stipples
    masked_img = np.where(mask_img < threshold, 1.0, stipple_img)

    return masked_img


# Example usage (for testing):
if __name__ == "__main__":
    # Create dummy stipple image (random dots)
    stipple = np.random.choice([0.0, 1.0], size=(64, 64), p=[0.2, 0.8])
    # Create dummy mask (center square dark)
    mask = np.ones((64, 64))
    mask[16:48, 16:48] = 0.0  # black square mask
    
    masked = create_masked_stipple(stipple, mask, threshold=0.5)
    print(masked.shape, masked.min(), masked.max())  # should be (64,64), 0.0, 1.0
