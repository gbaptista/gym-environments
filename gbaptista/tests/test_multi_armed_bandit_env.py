from ..multi_armed_bandit_env import MultiArmedBanditEnv


def test_step():
    env = MultiArmedBanditEnv()

    new_state, reward, is_done, info = env.step(0)

    assert new_state == 0
    assert isinstance(reward, float)
    assert is_done
    assert info == {}


def test_reset():
    env = MultiArmedBanditEnv()

    assert env.reset() == 0


def test_render():
    env = MultiArmedBanditEnv()

    assert env.render()
