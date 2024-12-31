# Create a package named geometry with submodules for 2D and 3D shapes. 
#Add functions for calculating areas and volumes.




import math

def rectangle_area(length, width):
    """Calculate the area of a rectangle."""
    return length * width

def circle_area(radius):
    """Calculate the area of a circle."""
    return math.pi * radius ** 2

def triangle_area(base, height):
    """Calculate the area of a triangle."""
    return 0.5 * base * height