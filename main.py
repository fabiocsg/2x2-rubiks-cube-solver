from agent import Agent
from solver import Solver

print('Starting Q-table training with the agent...')

# Initialize and train the agent
agent = Agent()
agent.load_data()

# Training loop
for i in range(1, 11):
    agent.train(i, i, i*100_000)

agent.export_data()

print('Training completed.')
print()
print('Testing the Q-table on different shuffle counts:')

# Initialize solver with trained Q-table
solver = Solver(agent.get_q_table())
max_shuffle = 10
max_tries = 1000

# Testing loop
for m in range(1, max_shuffle + 1):
    solved_count = 0
    for i in range(1, max_tries + 1):
        if solver.try_solve_cube(m, m):
            solved_count += 1
    success_rate = (solved_count / max_tries) * 100
    print(f'Shuffles count: {m}, Success rate: {success_rate:.2f}% over {max_tries} tries')

print()
print('Done.')
