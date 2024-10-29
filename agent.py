import random

from contants import MOVE_MAP
from cube import Cube
from enums import Move
from io import load_q_table, write_q_table
from utils import shuffle


class Agent:

    def __init__(self):
        self._alpha = 0.1  # learning rate
        self._gamma = 0.9  # discount factor
        self._epsilon = 1.0  # exploration rate
        self._q_table = {}

    def train(self, shuffle_count: int, moves_count: int, episodes: int):
        self._epsilon = 1.0 # reset epsilon between training sessions
        solved = 0
        for episode in range(episodes):
            cube = shuffle(Cube(), shuffle_count)
            state = cube.serialize()
            for _ in range(moves_count):
                action = self._choose_action(state)
                face, direction = MOVE_MAP[action]
                next_cube = cube.apply_move(face, direction)
                next_state = next_cube.serialize()
                reward = 100 if next_cube.is_solved() else -1
                self._update_q_value(state, action, reward, next_state)
                cube, state = next_cube, next_state
                if cube.is_solved():
                    solved += 1
                    break

            # print('moves:', moves_count, 'episode:', episode, 'solved:', solved, 'epsilon:', self._epsilon)

            # decay, but prevent the exploration rate from reaching zero
            self._epsilon = max(0.1, self._epsilon * 0.9999)

    def _choose_action(self, state: str):
        if random.random() < self._epsilon:
            return random.choice(list(Move))

        state_actions = self._q_table.get(state, {})
        if not state_actions:
            return random.choice(list(Move))

        best_move = max(state_actions, key=state_actions.get)
        return Move[best_move]

    def _update_q_value(self, state: str, action: Move, reward: float, next_state: str):
        self._add_state_if_not_present(state)
        self._add_state_if_not_present(next_state)

        # q learning formula
        current_q = self._q_table[state][action.name]
        max_future_q = max(self._q_table[next_state].values())
        new_q = current_q + self._alpha * (reward + self._gamma * max_future_q - current_q)
        self._q_table[state][action.name] = new_q

    def _add_state_if_not_present(self, state: str):
        if state not in self._q_table:
            self._q_table[state] = {move.name: 0.0 for move in Move}

    def load_data(self):
        print('importing q table')
        self._q_table = load_q_table()
        print('imported q table with', len(self._q_table), 'entries')

    def export_data(self):
        print('exporting q table with', len(self._q_table), 'entries')
        write_q_table(self._q_table)
        print('q table exported')

    def get_q_table(self):
        return self._q_table
