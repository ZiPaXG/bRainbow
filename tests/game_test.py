import pytest

from models.card import Card
from models.deck import Deck
from models.player import Player
from models.game import Game

deck = Deck()
player = Player("TestPlayer")
player.set_hand_deck(deck.get_players_deck()[0])


def test_check_card():

    # Проверка карты bRainbow
    Game.check_selected_card(player, Card("bRainbow", "", "", "", "bRainbow"), player.get_hand_deck(), 6)
    assert player.get_score() == 0
    Game.check_selected_card(player, Card("bRainbow", "", "", "", "bRainbow"), player.get_hand_deck(), 5)
    assert player.get_score() == 3

    # Проверка карты с правилом <Цвет>
    Game.check_selected_card(player, Card("зеленый", "фиолетовый", "желтый", "", "цвет"), player.get_hand_deck(), 4)
    assert player.get_score() == 3
    Game.check_selected_card(player, Card("зеленый", "фиолетовый", "желтый", "", "цвет"), player.get_hand_deck(), 1)
    assert player.get_score() == 6

    # Проверка карты с правилом <Название>
    Game.check_selected_card(player, Card("оранжевый", "зеленый", "розовый", "", "название"), player.get_hand_deck(), 2)
    assert player.get_score() == 6
    Game.check_selected_card(player, Card("оранжевый", "зеленый", "розовый", "", "название"), player.get_hand_deck(), 4)
    assert player.get_score() == 9

    # Проверка карты с правилом <Цвет> или <Название>, написанное черным цветом
    Game.check_selected_card(player, Card("синий", "черный", "красный", "", "черный"), player.get_hand_deck(), 5)
    assert player.get_score() == 9
    Game.check_selected_card(player, Card("синий", "черный", "красный", "", "черный"), player.get_hand_deck(), 1)
    assert player.get_score() == 12
