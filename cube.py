from contants import FACE_INDEXES_DICT
from enums import Direction, Color, Face


class Cube:
    def __init__(self, state: [] = None):
        self._state = _INITIAL_STATE if state is None else state

    def __getitem__(self, i):
        return self._state[i].name[0]

    def apply_move(self, face: Face, direction: Direction):
        clone = Cube(self._state.copy())
        face_indexes = FACE_INDEXES_DICT[face]
        match direction:
            case Direction.CLOCKWISE:
                clone._state[face_indexes[1]] = self._state[face_indexes[0]]
                clone._state[face_indexes[2]] = self._state[face_indexes[1]]
                clone._state[face_indexes[3]] = self._state[face_indexes[2]]
                clone._state[face_indexes[0]] = self._state[face_indexes[3]]
                clone._state[face_indexes[6]] = self._state[face_indexes[4]]
                clone._state[face_indexes[7]] = self._state[face_indexes[5]]
                clone._state[face_indexes[8]] = self._state[face_indexes[6]]
                clone._state[face_indexes[9]] = self._state[face_indexes[7]]
                clone._state[face_indexes[10]] = self._state[face_indexes[8]]
                clone._state[face_indexes[11]] = self._state[face_indexes[9]]
                clone._state[face_indexes[4]] = self._state[face_indexes[10]]
                clone._state[face_indexes[5]] = self._state[face_indexes[11]]

            case Direction.COUNTER_CLOCKWISE:
                clone._state[face_indexes[0]] = self._state[face_indexes[1]]
                clone._state[face_indexes[1]] = self._state[face_indexes[2]]
                clone._state[face_indexes[2]] = self._state[face_indexes[3]]
                clone._state[face_indexes[3]] = self._state[face_indexes[0]]
                clone._state[face_indexes[4]] = self._state[face_indexes[6]]
                clone._state[face_indexes[5]] = self._state[face_indexes[7]]
                clone._state[face_indexes[6]] = self._state[face_indexes[8]]
                clone._state[face_indexes[7]] = self._state[face_indexes[9]]
                clone._state[face_indexes[8]] = self._state[face_indexes[10]]
                clone._state[face_indexes[9]] = self._state[face_indexes[11]]
                clone._state[face_indexes[10]] = self._state[face_indexes[4]]
                clone._state[face_indexes[11]] = self._state[face_indexes[5]]

        return clone

    def is_solved(self):
        face_size = len(self._state) // 6
        faces = [self._state[i:i + face_size] for i in range(0, len(self._state), face_size)]
        return all(len(set(face)) == 1 for face in faces)

    def print(self):
        print('\t', self[0], self[1], '\t')
        print('\t', self[2], self[3], '\t')
        print(self[16], self[17], self[4], self[5], self[20], self[21])
        print(self[18], self[19], self[6], self[7], self[22], self[23])
        print('\t', self[8], self[9], '\t')
        print('\t', self[10], self[11], '\t')
        print('\t', self[12], self[13], '\t')
        print('\t', self[14], self[15], '\t')
        print()

    def serialize(self):
        return ''.join(color.name[0] for color in self._state)

    def _value_at(self, position: int):
        return self._state[position].name


_INITIAL_STATE = [
    Color.RED,
    Color.RED,
    Color.RED,
    Color.RED,
    Color.YELLOW,
    Color.YELLOW,
    Color.YELLOW,
    Color.YELLOW,
    Color.GREEN,
    Color.GREEN,
    Color.GREEN,
    Color.GREEN,
    Color.WHITE,
    Color.WHITE,
    Color.WHITE,
    Color.WHITE,
    Color.ORANGE,
    Color.ORANGE,
    Color.ORANGE,
    Color.ORANGE,
    Color.BLUE,
    Color.BLUE,
    Color.BLUE,
    Color.BLUE,
]
