class Card:
    def __init__(self, name, color, img_path, is_game_rule=False):
        self.name = name
        self.color = color
        self.isGameRule = is_game_rule
        self.img_path = img_path
