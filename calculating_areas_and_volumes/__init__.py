#  Create a package named geometry with submodules for 2D and 3D shapes. 
#Add functions for calculating areas and volumes.

# geometry/__init__.py
from .shapes2d import rectangle_area, circle_area, triangle_area
from .shapes3d import cube_volume, sphere_volume, cylinder_volume