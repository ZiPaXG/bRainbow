class Card:
    def __init__(self, name, fg_color, bg_color, img_path, is_game_rule=False):
        self.name = name
        self.bgColor = bg_color
        self.fgColor = fg_color
        self.img_path = img_path
        self.isGameRule = is_game_rule
    def __repr__(self):
        if self.name == 'bRainbow':
            return f'{self.name}'
        return f'{self.name}:{self.fgColor}:{self.bgColor}'
