import os
import pickle

_q_table_file_name = 'data.pickle'

def load_q_table():
    if not os.path.exists(_q_table_file_name):
        return {}

    with open(_q_table_file_name, 'rb') as file:
        return pickle.load(file)

def write_q_table(q_table):
    with open(_q_table_file_name, 'wb') as file:
        pickle.dump(q_table, file, pickle.HIGHEST_PROTOCOL)