class Game:
    def __init__(self, pg):
        """ Создание дисплея с настройками """
        self.screen_width, self.screen_height = 1300, 1000
        self.FPS = 60
        self.clock = pg.time.Clock()
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

    def start(self, pg):
        isRunning = True
        while isRunning:
            isRunning = self.event_processing(pg)
        pg.quit()

