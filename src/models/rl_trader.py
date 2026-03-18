import numpy as np

class SimpleRLTrader:
    def __init__(self):
        self.q_table = {}

    def get_state(self, row):
        return (round(row["returns"], 3), round(row["volatility"], 3))

    def choose_action(self, state):
        return np.random.choice([0, 1])  # explore

    def update(self, state, action, reward):
        self.q_table[(state, action)] = reward