
import random

from contants import MOVE_MAP
from cube import Cube
from enums import Move
from io import load_q_table
from utils import shuffle


class Solver:
    _q_table = {}

    def __init__(self, q_table):
        self._q_table = load_q_table() if not q_table else q_table

    def try_solve_cube(self, shuffle_count: int, moves_allowed: int):
        cube = shuffle(Cube(), shuffle_count)
        solved = False
        moves_count = 0
        for _ in range(moves_allowed):
            moves_count += 1
            state = cube.serialize()
            move_ratings = self._q_table.get(state, {})
            if not move_ratings:
                move = random.choice(list(Move))
            else:
                best_move = max(move_ratings, key=move_ratings.get)
                move = Move[best_move]

            face, direction = MOVE_MAP[move]
            cube = cube.apply_move(face, direction)
            solved = cube.is_solved()
            if solved:
                break

        return solved