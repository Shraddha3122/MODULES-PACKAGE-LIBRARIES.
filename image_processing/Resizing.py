# Submodule: Resizing
class Resizer:
    @staticmethod
    def resize(image, width=None, height=None):
        if not width and not height:
            raise ValueError("Either width or height must be specified")

        original_width, original_height = image.size
        
        if not width:
            width = int((height / original_height) * original_width)
        elif not height:
            height = int((width / original_width) * original_height)

        return image.resize((width, height))