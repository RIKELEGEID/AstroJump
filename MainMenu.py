import pygame
import sys
from Settings import WINDOW_WIDTH, WINDOW_HEIGHT, button_height, button_width, button_gap


class Menu:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption("AstroJump")
        bg = pygame.image.load()
        self.screen.blit(bg, (0, 0))

        # Set up colors
        self.black = (0, 0, 0)
        self.white = (255, 255, 255)
        self.button_color = (50, 50, 50)
        self.quit_button_color = (125, 50, 50)
        self.hover_color = (100, 100, 100)

        # Create a font object
        self.font = pygame.font.Font(None, 36)

    def draw_text(self, text, font, color, x, y):
        text_obj = font.render(text, True, color)
        text_rect = text_obj.get_rect(center=(x, y))
        self.screen.blit(text_obj, text_rect)

    def draw_button(self, text, rect, color):
        pygame.draw.rect(self.screen, color, rect)
        text_surface = self.font.render(text, True, self.white)
        text_rect = text_surface.get_rect(center=rect.center)
        self.screen.blit(text_surface, text_rect)

    def main_menu(self):
        while True:
            self.screen.fill(self.black)

            self.draw_text("Main Menu", self.font, self.white, WINDOW_WIDTH // 2, 200)

            mx, my = pygame.mouse.get_pos()

            button_resume = pygame.Rect(WINDOW_WIDTH // 2 - button_width // 2, 300, button_width, button_height)
            button_editor = pygame.Rect(WINDOW_WIDTH // 2 - button_width // 2, 400, button_width, button_height)
            button_quit = pygame.Rect(WINDOW_WIDTH // 2 - button_width // 2, 500, button_width, button_height)

            resume_hovered = button_resume.collidepoint((mx, my))
            editor_hovered = button_editor.collidepoint((mx, my))
            quit_hovered = button_quit.collidepoint((mx, my))

            self.draw_button("Resume", button_resume, self.hover_color if resume_hovered else self.button_color)
            self.draw_button("Settings", button_editor, self.hover_color if editor_hovered else self.button_color)
            self.draw_button("Quit Game", button_quit, self.hover_color if quit_hovered else self.quit_button_color)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if resume_hovered:
                        selected_level = self.level_select()
                        print(f"Selected Level: {selected_level}")
                    elif editor_hovered:
                        print("Settings clicked")
                    elif quit_hovered:
                        pygame.quit()
                        sys.exit()

            pygame.display.update()

    def level_select(self):
        while True:
            self.screen.fill(self.black)

            self.draw_text("Select a Level", self.font, self.white, WINDOW_WIDTH // 2, 100)

            mx, my = pygame.mouse.get_pos()

            level1 = pygame.Rect((WINDOW_WIDTH - 3 * button_width - 2 * button_gap) // 2, 200, button_width, button_height)
            level2 = pygame.Rect(level1.right + button_gap, 200, button_width, button_height)
            level3 = pygame.Rect(level2.right + button_gap, 200, button_width, button_height)

            if level1.collidepoint((mx, my)):
                if pygame.mouse.get_pressed()[0]:
                    print("Level 1 Selected")
                    return 1
            if level2.collidepoint((mx, my)):
                if pygame.mouse.get_pressed()[0]:
                    print("Level 2 Selected")
                    return 2
            if level3.collidepoint((mx, my)):
                if pygame.mouse.get_pressed()[0]:
                    print("Level 3 Selected")
                    return 3

            pygame.draw.rect(self.screen, self.button_color, level1)
            pygame.draw.rect(self.screen, self.button_color, level2)
            pygame.draw.rect(self.screen, self.button_color, level3)

            self.draw_text("Level 1", self.font, self.white, level1.centerx, level1.centery)
            self.draw_text("Level 2", self.font, self.white, level2.centerx, level2.centery)
            self.draw_text("Level 3", self.font, self.white, level3.centerx, level3.centery)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            pygame.display.update()


