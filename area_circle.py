import math
## area of circle

## contract on slide 6.26 of course notes, CS116

## area_circle: float -> float
def area_circle (radius):
    return (math.pi * radius * radius)

## Testing
print "test radius=1"
actual = area_circle(1.0)
print actual == 3.14159265
print actual == math.pi


## close: float float -> boolean
## produces true is abs(x-y) < 0.000001, false otherwise
## example (1.2,1.3) => false, close (1.2,1.20000001) => true

def close(x,y):
    return abs(x-y) < 0.000001

print "test radius 1 again"
print close(actual, 3.14159265)
