from gym.envs.registration import register

register(
    id='MultiArmedBanditEnv-v0',
    entry_point='gym.envs.gbaptista.multi_armed_bandit_env:'
                'MultiArmedBanditEnv'
)
