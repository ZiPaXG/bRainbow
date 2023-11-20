import pytest
from models.player import Player

player = Player()
player1 = Player('testN')


def test_create_player():
    assert str(player) != ''
    assert str(player) == 'Player'
    assert str(player1) == 'testN'
    assert player.get_score() == 0
    assert player.get_win() == 0
    assert len(player.get_hand_deck()) == 0


def test_add_score():
    player.add_score(10)
    player1.add_score(-10)
    assert player.get_score() == 10
    assert player.get_score() != 0
    assert player1.get_score() == -10
    assert player1.get_score() != 0
    with pytest.raises(TypeError):
        player.add_score('10')


def test_add_win():
    player.add_win()
    player.add_win()
    player.add_win()
    player1.add_win()
    assert player.get_win() == 3
    assert player.get_win() != 0
    assert player1.get_win() == 1
    assert player1.get_win() != 0
