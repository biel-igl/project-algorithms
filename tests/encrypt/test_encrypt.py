import pytest
from challenges.challenge_encrypt_message import encrypt_message


def test_encrypt_message():
    with pytest.raises(TypeError, match="tipo inválido para key"):
        encrypt_message(3, "gabrie")
    with pytest.raises(TypeError, match="tipo inválido para key"):
        encrypt_message("oi", "gabrie")
    with pytest.raises(TypeError, match="tipo inválido para message"):
        encrypt_message(5, 5)
    assert encrypt_message("gabrie", 3) == "bag_eir"
    assert encrypt_message("gabriel", 4) == "lei_rbag"
    assert encrypt_message("gabriel", 77) == "leirbag"
