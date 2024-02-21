from globals import *
from scene import Scene


class Game:
    def __init__(self):
        pygame.init()
        self.display = pygame.display.set_mode((SCREENWIDTH, SCREENHEIGHT))
        pygame.display.set_caption("Caasje Productions")
        self.clock = pygame.time.Clock()
        self.scene = Scene()

        self.running = True

    def run(self):
        while self.running:
            dt = self.clock.tick(FPS) / 1000
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
            self.scene.run(dt)
            pygame.display.update()
        pygame.quit()
        sys.exit()


if __name__ == '__main__':
    game = Game()
    game.run()
