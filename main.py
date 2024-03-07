import pygame
from settings import WINDOW_WIDTH, WINDOW_HEIGHT
from game import Game


class Main:
    def __init__(self):
        pygame.init()
        self.display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT), pygame.FULLSCREEN)
        self.clock = pygame.time.Clock()
        self.game = Game()

    def run(self):
        while True:
            dt = self.clock.tick() / 1000

            self.game.main_menu()  # Call the main_menu method of the Menu class
            pygame.display.update()


if __name__ == "__main__":
    main = Main()
    main.run()
