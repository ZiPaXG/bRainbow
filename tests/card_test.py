import pytest
from models.card import Card

card = Card('зеленый', 'красный', 'розовый', 'asdf')
card1 = Card('bRainbow', '', '', 'asdf', 'bRainbow')
card2 = Card('розовый', 'зеленый', 'желтый', 'asdf', 'черный')


def test_create_card():
    assert str(card) == 'зеленый:красный:розовый'
    assert str(card1) == 'bRainbow'
    assert str(card1) != 'bRainbow:: - bRainbow'
    assert str(card2) == 'розовый:зеленый:желтый - черный'
    assert str(card2) != 'розовый:зеленый:желтый'
