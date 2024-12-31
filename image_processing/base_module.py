# Build a package for image processing with submodules for resizing, rotating, and applying filters to images.
import os
from PIL import Image, ImageFilter

# Base module
class ImageProcessor:
    def __init__(self, image_path):
        if not os.path.exists(image_path):
            raise FileNotFoundError(f"Image file not found: {image_path}")
        self.image = Image.open(image_path)

    def save(self, output_path):
        self.image.save(output_path)
        
        
        
       