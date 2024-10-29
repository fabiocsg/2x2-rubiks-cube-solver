from enums import Face, Move, Direction

FACE_INDEXES_DICT = {
    Face.FRONT: [4, 5, 6, 7, 2, 3, 20, 22, 8, 9, 17, 19],
    Face.RIGHT: [20, 21, 22, 23, 3, 1, 13, 15, 11, 9, 7, 5],
    Face.LEFT: [16, 17, 18, 19, 0, 2, 4, 6, 8, 10, 12, 14],
    Face.TOP: [0, 1, 2, 3, 14, 15, 21, 20, 5, 4, 17, 16],
    Face.BOTTOM: [8, 9, 10, 11, 6, 7, 22, 23, 13, 12, 18, 19],
    Face.BACK: [12, 13, 14, 15, 10, 11, 23, 21, 1, 0, 16, 18],
}

MOVE_MAP = {
    Move.U: (Face.TOP, Direction.CLOCKWISE),
    Move.D: (Face.BOTTOM, Direction.CLOCKWISE),
    Move.R: (Face.RIGHT, Direction.CLOCKWISE),
    Move.L: (Face.LEFT, Direction.CLOCKWISE),
    Move.F: (Face.FRONT, Direction.CLOCKWISE),
    Move.B: (Face.BACK, Direction.CLOCKWISE),
    Move.U1: (Face.TOP, Direction.COUNTER_CLOCKWISE),
    Move.D1: (Face.BOTTOM, Direction.COUNTER_CLOCKWISE),
    Move.R1: (Face.RIGHT, Direction.COUNTER_CLOCKWISE),
    Move.L1: (Face.LEFT, Direction.COUNTER_CLOCKWISE),
    Move.F1: (Face.FRONT, Direction.COUNTER_CLOCKWISE),
    Move.B1: (Face.BACK, Direction.COUNTER_CLOCKWISE),
}
