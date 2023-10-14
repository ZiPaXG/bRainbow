class Player:
    def __init__(self, name="Player"):
        self.name = name
        self.score = 0
        self.wins = 0

    def set_score(self, count_score):
        self.score += count_score

    def get_score(self):
        return self.score

    def set_win(self):
        self.wins += 1

    def get_win(self):
        return self.wins