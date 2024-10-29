from enum import Enum

class Color(Enum):
    GREEN = 1
    BLUE = 2
    RED = 3
    YELLOW = 4
    WHITE = 5
    ORANGE = 6

class Face(Enum):
    FRONT = 1
    RIGHT = 2
    LEFT = 3
    TOP = 4
    BOTTOM = 5
    BACK = 6

class Direction(Enum):
    CLOCKWISE = 1
    COUNTER_CLOCKWISE = 2

class Move(Enum):
    U = 1
    D = 2
    R = 3
    L = 4
    F = 5
    B = 6
    U1 = 7
    D1 = 8
    R1 = 9
    L1 = 10
    F1 = 11
    B1 = 12