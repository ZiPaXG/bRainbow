class Player:
    def __init__(self, name='Player'):
        self._name = name
        self._score = 0
        self._wins = 0
        self._hand_deck = []

    def __repr__(self):
        return f'{self._name}'

    def add_score(self, count_score):
        self._score += count_score

    def get_score(self):
        return self._score

    def add_win(self):
        self._wins += 1

    def get_win(self):
        return self._wins

    def get_name(self):
        return self._name

    def get_hand_deck(self):
        return self._hand_deck

    def set_hand_deck(self, hand_deck):
        self._hand_deck = hand_deck
