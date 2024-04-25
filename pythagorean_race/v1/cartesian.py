from random import randint
from math import sqrt

type Position = tuple[int, int]
type Grid = list[list[str]]

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

    if octant == 1:  # 0-45 degrees
        if a > b:
            return (a, b)
        else:
            return (b, a)
    elif octant == 2:  # 45-90 degrees
        if b > a:
            return (a, b)
        else:
            return (b, a)
    elif octant == 3:  # 90 - 135 degrees
        if b > a:
            return (-a, b)
        else:
            return (-b, a)
    elif octant == 4:  # 135 - 180 degrees
        if a > b:
            return (-a, b)
        else:
            return (-b, a)
    elif octant == 5:  # 180 - 225 degrees
        if a > b:
            return (-a, -b)
        else:
            return (-b, -a)
    elif octant == 6:  # 225 - 270 degrees
        if b > a:
            return (-a, -b)
        else:
            return (-b, -a)
    elif octant == 7:  # 270 - 315 degrees
        if b > a:
            return (a, -b)
        else:
            return (-b, a)
    elif octant == 8:  # 270 - 360 degrees
        if a > b:
            return (a, -b)
        else:
            return (-b, a)

    # We never get here, just to make the warning about returning from all code
    # paths go away
    return (0, 0)


def add_points(p1: Position, p2: Position) -> Position:
    return (p1[0] + p2[0], p1[1] + p2[1])


def sub_points(p1: Position, p2: Position) -> Position:
    return (p1[0] - p2[0], p1[1] - p2[1])


def grad(start: Position, end: Position) -> float:
    grad = (end[1] - start[1]) / (end[0] - start[0])
    return grad


def midpoint(p1: Position, p2: Position) -> Position:
    mid_point = ((p1[0] + p2[0]) / 2.0, (p1[1] + p2[1]) / 2.0)
    return mid_point


def scale(p: Position, minp: Position, maxp: Position,
          outmin: Position, outmax: Position) -> Position:
    p2 = sub_points(p, minp)
    d = sub_points(maxp, minp)
    s = (float(p2[0]) / float(d[0]), float(p2[1]) / float(d[1]))
    dout = sub_points(outmax, outmin)
    return (int(s[0]*dout[0]), int(s[1]*dout[1]))


def gen_grid(h: int, v: int) -> Grid:
    g: list[list[str]] = []
    for _ in range(h):
        row = []
        for _ in range(v):
            row.append('.')
        g.append(row)
    return g


def set_grid_elem(x: int, y: int, elem: str, grid: Grid) -> Grid:
    grid[y][x] = elem
    return grid


def print_grid(grid: Grid) -> None:
    for r in grid:
        print(" ".join(r))
