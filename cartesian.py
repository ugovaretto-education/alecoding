from random import randint
from math import sqrt

type Position = tuple[int, int]

# Return random 2D coordinates.
def rand_coord(max_coord: int) -> tuple[int, int]:
    return (randint(-max_coord, max_coord), randint(-max_coord, max_coord))

# Compute the square of the distance between two points (Pythagora's theorem).
def distance_sq(a: Position, b: Position) -> float:
    return (a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2

# Compute the distamce between two points.
def distance(a: tuple[int, int], b: tuple[int, int]) -> float:
    return sqrt(distance_sq(a, b))


# Given octant code from 1 to 8 and a and b triangle sides
# return the x and y coordinates sucn that x*x + y*y == a*a + b*b
# with the right signs to fit in the quandrant.
def ab_to_xy(ab: tuple[int, int], octant: int) -> tuple[int, int]:
    a, b = ab
    
    if octant == 1: # 0-45 degrees
        if a > b:
            return (a, b)
        else:
            return (b, a)
    elif octant == 2: # 45-90 degrees
        if b > a:
            return (a, b)
        else:
            return (b, a)
    elif octant == 3: # 90 - 135 degrees
        if b > a:
            return (b, -a)
        else:
            return (-a, b)
    elif octant == 4: # 135 - 180 degrees
        if a > b:
            return (-a, b)
        else:
            return (b, -a)
    elif octant == 5: # 180 - 225 degrees 
        if a > b:
            return (-a, -b)
        else:
            return (-b, -a)
    elif octant == 6: # 225 - 270 degrees
        if b > a:
            return (-a, -b)
        else:
            return (-b, -a)
    elif octant == 7: # 270 - 315 degrees
        if b > a:
            return (a, -b)
        else:
            return (-b, a)
    elif octant == 8: # 270 - 360 degrees
        if a > b:
            return (a, -b)
        else:
            return (-b, a)

    # We never get here, just to make the warning about returning from all code paths go away
    return (0, 0)
