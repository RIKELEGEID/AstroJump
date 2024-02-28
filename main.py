import pygame
from Settings import WINDOW_WIDTH, WINDOW_HEIGHT, volume
from MainMenu import Menu


class Main:
    def __init__(self):
        pygame.init()
        self.display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        self.clock = pygame.time.Clock()
        self.menu = Menu()
        self.bg_music = "Sounds/BG_music.mp3"

    def run(self):
        while True:
            dt = self.clock.tick() / 1000
            pygame.mixer.music.load(self.bg_music)
            pygame.mixer.music.set_volume(volume)
            pygame.mixer.music.play(-1)

            self.menu.main_menu()  # Call the main_menu method of the Menu class
            pygame.display.update()


if __name__ == "__main__":
    main = Main()
    main.run()
