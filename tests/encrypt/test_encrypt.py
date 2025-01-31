from challenges.challenge_encrypt_message import encrypt_message
import pytest


def test_encrypt_message():

    with pytest.raises(TypeError, match="tipo inválido para key"):
        encrypt_message('message', 'message')
    with pytest.raises(TypeError, match="tipo inválido para message"):
        encrypt_message(1, 1)

    assert encrypt_message('message', -1) == 'egassem'
    assert encrypt_message('message', 3) == 'sem_egas'
    assert encrypt_message('message', 4) == 'ega_ssem'
