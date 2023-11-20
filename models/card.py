class Card:
    def __init__(self, name: str, fg_color: str, bg_color: str, img_path: str, game_rule=''):
        self.name = name
        self.bgColor = bg_color
        self.fgColor = fg_color
        self.img_path = img_path
        self.gameRule = game_rule

    def __repr__(self):
        if self.gameRule != "":
            if self.name == "bRainbow":
                return f'{self.name}'
            else:
                return f'{self.name}:{self.fgColor}:{self.bgColor} - {self.gameRule}'

        return f'{self.name}:{self.fgColor}:{self.bgColor}'
