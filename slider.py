import pygame


class Slider:
    def __init__(self, x, y, w, h, min_val, max_val, start_val):
        self.rect = pygame.Rect(x, y, w, h)
        self.min_val = min_val
        self.max_val = max_val
        self.value = start_val
        self.handle_rect = pygame.Rect(x, y, h, h)
        self.dragging = False

    def draw(self, screen):
        pygame.draw.rect(screen, (200, 200, 200), self.rect, border_radius=15)
        pygame.draw.rect(screen, (150, 150, 150), self.handle_rect, border_radius=15)

    def handle_event(self, event, mx, my):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.handle_rect.collidepoint((mx, my)):
                self.dragging = True

        elif event.type == pygame.MOUSEBUTTONUP:
            self.dragging = False

        elif event.type == pygame.MOUSEMOTION and self.dragging:
            self.handle_rect.x = max(self.rect.x, min(mx, self.rect.x + self.rect.width - self.handle_rect.width))
            self.value = self.min_val + (self.max_val - self.min_val) * (
                        (self.handle_rect.x - self.rect.x) / self.rect.width)
