import pytest
from models.deck import Deck
from models.player import Player

deck = Deck()
list_players = list()
list_players.append(Player("TestPlayer"))

def test_create_deck():
    assert len(deck.get_players_deck()) == 6
    assert len(deck.get_players_deck()[0]) == 6
    assert len(deck.get_rule_deck()) == 24


def test_give_cards():
    deck.give_cards(list_players)
    assert list_players[0].get_hand_deck() != []

def test_remove_rule_card():
    len_old = len(deck.get_rule_deck())
    deck.remove_rule_card_from_deck()
    assert len_old != len(deck.get_rule_deck())

