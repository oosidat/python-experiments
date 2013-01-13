import math

## Computing vol of cone, formula of volume = pi*h*r^2
# cone_volume: float float -> float

def cone_vol (radius, height):
    area_circle = math.pi*radius*radius
    return (1.0/3 * area_circle * height)
#1.0/3 is used to avoid the floater problem, 1/3 = 0

