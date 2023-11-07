from models.card import Card
from models.player import Player

class Game:
    def __init__(self, pg):
        self.screen_width, self.screen_height = 1300, 1000
        self.FPS = 60
        self.clock = pg.time.Clock()
        # Добавления поля display в класс
        self.display = None

    def start_display(self, pg):
        self.display = pg.display.set_mode((self.screen_width, self.screen_height))
        pg.display.set_caption('bRainbow')
        self.loadStart(pg)

    def event_processing(self, pg):
        isRunning = True
        for event in pg.event.get():
            # Нажатие на крестик
            if (event.type == pg.QUIT):
                isRunning = False
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_q:
                    isRunning = False

        self.clock.tick(self.FPS)
        return isRunning

    def loadStart(self, pg):
        self.display.fill([255, 0, 0])
        pg.display.update()

    @staticmethod
    def get_rools():
        print("Всего будет 24 раунда. Каждому игроку будет выдана колода из 6 карт")
        print("Также есть общая колода карт (24 карты). Они будут вытягиваться поочереди. К ним применяются следующие правила: ")
        print("Правило 1: На карте из общей колоды указано <Цвет> - берем карту, название которой есть цвет окраски основного слова")
        print("Правило 2: На карте из общей колоды название написано черным - берем карту, название которой есть цвет фона")
        print("Правило 3: Выпала карта bRainbow - нужно быстрее всех забрать ее")
        print("Правило 4: На карте из общей колоды указано <Название> - берем карту с цветом названия основного слова, который указан")

    def check_selected_card(self, player: Player, deck_card: Card, player_cards: list[Card], numCard):
        if numCard != -1:
            if deck_card.fgColor == "черный":
                if player_cards[numCard].name != deck_card.bgColor:
                    player.add_score(3)
            elif deck_card.gameRule == "цвет":
                if player_cards[numCard].name != deck_card.fgColor:
                    player.add_score(3)
            elif deck_card.gameRule == "название":
                if player_cards[numCard].fgColor != deck_card.name:
                    player.add_score(3)
            elif deck_card.gameRule == "bRainbow":
                if numCard != 6:
                    player.add_score(3)
        else:
            if deck_card.fgColor == "черный":
                for i in range(len(player_cards)):
                    if deck_card.bgColor == player_cards[i].name:
                        player.add_score(3)
                        break
            elif deck_card.gameRule == "цвет":
                for i in range(len(player_cards)):
                    if deck_card.fgColor == player_cards[i].name:
                        player.add_score(3)
                        break
            elif deck_card.gameRule == "название":
                for i in range(len(player_cards)):
                    if deck_card.name == player_cards[i].fgColor:
                        player.add_score(3)
                        break
            elif deck_card.gameRule == "bRainbow":
                player.add_score(3)



    def start(self, pg):
        isRunning = True
        while isRunning:
            isRunning = self.event_processing(pg)
        pg.quit()

