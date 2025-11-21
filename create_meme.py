"""
Create the final statistics meme by assembling all four panels.
This function creates a professional-looking four-panel meme demonstrating selection bias.
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec


def create_statistics_meme(
    original_img: np.ndarray,
    stipple_img: np.ndarray,
    block_letter_img: np.ndarray,
    masked_stipple_img: np.ndarray,
    output_path: str,
    dpi: int = 150,
    background_color: str = "white"
) -> None:
    """
    Create a four-panel statistics meme demonstrating selection bias.
    
    Parameters
    ----------
    original_img : np.ndarray
        Original grayscale image (Reality panel)
    stipple_img : np.ndarray
        Stippled image (Your Model panel)
    block_letter_img : np.ndarray
        Block letter image (Selection Bias panel)
    masked_stipple_img : np.ndarray
        Masked stippled image (Estimate panel)
    output_path : str
        Path where the meme PNG file will be saved
    dpi : int
        Resolution (dots per inch) for the output image. Default 150.
    background_color : str
        Background color for the figure. Default "white".
    
    Returns
    -------
    None
        Saves the meme as a PNG file to output_path.
    """
    # Panel labels
    labels = ["Reality", "Your Model", "Selection Bias", "Estimate"]
    images = [original_img, stipple_img, block_letter_img, masked_stipple_img]
    
    # Create figure with 1 row and 4 columns
    fig = plt.figure(figsize=(16, 4), facecolor=background_color, dpi=dpi)
    gs = GridSpec(1, 4, figure=fig, wspace=0.15, hspace=0.1,
                  left=0.02, right=0.98, top=0.92, bottom=0.08)
    
    # Create subplots and display images
    for i, (img, label) in enumerate(zip(images, labels)):
        ax = fig.add_subplot(gs[0, i])
        ax.imshow(img, cmap='gray', vmin=0, vmax=1)
        ax.axis('off')
        
        # Add label above each panel
        ax.set_title(label, fontsize=16, fontweight='bold', pad=10, color='black')
    
    # Save the figure
    plt.savefig(output_path, dpi=dpi, bbox_inches='tight', 
                facecolor=background_color, edgecolor='none')
    plt.close()
    
    print(f"Statistics meme saved to: {output_path}")


# Example usage (for testing):
if __name__ == "__main__":
    # Create dummy images for testing
    test_img = np.ones((100, 100)) * 0.5
    create_statistics_meme(
        original_img=test_img,
        stipple_img=test_img,
        block_letter_img=test_img,
        masked_stipple_img=test_img,
        output_path="test_meme.png",
        dpi=150,
        background_color="white"
    )
    print("Test meme created successfully!")

