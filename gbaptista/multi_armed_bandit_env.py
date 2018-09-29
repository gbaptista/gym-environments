from io import StringIO

import sys

import numpy as np

import gym


class MultiArmedBanditEnv(gym.Env):
    # Observation Space: 1 because you never move.

    # Action Space: 2
    # Action 0: Play Bandit A
    # Action 1: Play Bandit B
    # Action 2: Play Bandit C

    def __init__(self):
        self.observation_space = gym.spaces.Discrete(1)
        self.action_space = gym.spaces.Discrete(3)

        self.bandit_machines_true_means = {0: 1.0, 1: 2.0, 2: 3.0}

    def step(self, action):
        true_mean = self.bandit_machines_true_means[action]

        reward = np.random.randn() + true_mean

        return (0, reward, True, {})  # new_state, reward, is_done, info

    def reset(self):
        return 0  # current_state

    def render(self, mode='human'):
        out_file = StringIO() if mode == 'ansi' else sys.stdout

        out_file.write('Multi-armed Bandit')

        return out_file
