
import random

from contants import MOVE_MAP
from cube import Cube
from enums import Move


def shuffle(cube: Cube, moves_count: int):
    shuffle_moves = []
    for _ in range(moves_count):
        move = random.choice(list(Move))
        face, direction = MOVE_MAP[move]
        cube = cube.apply_move(face, direction)
        shuffle_moves.append(move)
    return cube
