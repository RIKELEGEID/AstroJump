import pygame
from settings import WINDOW_WIDTH, WINDOW_HEIGHT


class Camera:
    def __init__(self, width, height):
        self.camera = pygame.Rect(0, 0, width, height)
        self.width = width
        self.height = height

    def apply(self, entity):
        return entity.move(self.camera.topleft)

    def update(self, target):
        x = -target.x + int(WINDOW_WIDTH / 2)
        y = -target.y + int(WINDOW_HEIGHT / 2)

        # Limit scrolling to map size
        x = min(0, x)  # Left
        y = min(0, y)  # Top
        x = max(-(self.width - WINDOW_WIDTH), x)  # Right
        y = max(-(self.height - WINDOW_HEIGHT), y)  # Bottom

        self.camera = pygame.Rect(x, y, self.width, self.height)






