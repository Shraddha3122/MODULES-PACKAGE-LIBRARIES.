
from image_processor import ImageProcessor, Resizer, Rotator, FilterApplier

if __name__ == "__main__":
    try:
        # Initialize processor
        image_processor = ImageProcessor("C:/Users/iTA/Desktop/trend.png")
        
        # Resize image
        resized_image = Resizer.resize(image_processor.image, width=200)
        image_processor.image = resized_image
        image_processor.save("resized_image.jpg")

        # Rotate image
        rotated_image = Rotator.rotate(image_processor.image, 45)
        image_processor.image = rotated_image
        image_processor.save("rotated_image.jpg")

        # Apply filter
        filtered_image = FilterApplier.apply_filter(image_processor.image, "BLUR")
        image_processor.image = filtered_image
        image_processor.save("filtered_image.jpg")
    
    except Exception as e:
        print(f"An error occurred: {e}")
