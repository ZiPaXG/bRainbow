class Player:
    def __init__(self, name="Player"):
        self.name = name
        self._score = 0
        self.wins = 0
        self.hand_deck = []

    def __repr__(self):
        return f'{self.name}'

    def add_score(self, count_score):
        self._score += count_score

    def get_score(self):
        return self._score

    def set_win(self):
        self.wins += 1

    def get_win(self):
        return self.wins
