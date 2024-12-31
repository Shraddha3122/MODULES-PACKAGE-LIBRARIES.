# Submodule: Rotating
class Rotator:
    @staticmethod
    def rotate(image, degrees):
        return image.rotate(degrees, expand=True)
