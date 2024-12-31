## Create a package named geometry with submodules for 2D and 3D shapes. 
#Add functions for calculating areas and volumes.


import math

def cube_volume(side):
    """Calculate the volume of a cube."""
    return side ** 3

def sphere_volume(radius):
    """Calculate the volume of a sphere."""
    return (4/3) * math.pi * radius ** 3

def cylinder_volume(radius, height):
    """Calculate the volume of a cylinder."""
    return math.pi * radius ** 2 * height

