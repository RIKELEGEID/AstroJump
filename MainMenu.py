import pygame
import sys
from Settings import *


class Menu:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption("AstroJump")

        # colors
        self.black = (0, 0, 0)
        self.white = (255, 255, 255)
        self.button_color = (50, 50, 50)
        self.quit_button_color = (125, 50, 50)
        self.hover_color = (100, 100, 100)

        # fonts
        self.font_custom = pygame.font.Font("Graphics/fonts/pixel_font.ttf", 36)

        # sounds
        self.button_sound = pygame.mixer.Sound("Sounds/button_sound3.mp3")
        self.button_sound.set_volume(button_volume)

    def draw_text(self, text, font, color, x, y):
        text_obj = font.render(text, True, color)
        text_rect = text_obj.get_rect(center=(x, y))
        self.screen.blit(text_obj, text_rect)

    def draw_button(self, text, rect, color):
        pygame.draw.rect(self.screen, color, rect)
        text_surface = self.font_custom.render(text, True, self.white)
        text_rect = text_surface.get_rect(center=rect.center)
        self.screen.blit(text_surface, text_rect)

    def main_menu(self):
        while True:
            bg = pygame.image.load("Graphics/backgrounds/BG.png")
            self.screen.blit(bg, (0, 0))

            self.draw_text("Astro Jump", self.font_custom, self.white, WINDOW_WIDTH // 2, 200)

            mx, my = pygame.mouse.get_pos()

            button_play = pygame.Rect(WINDOW_WIDTH // 2 - button_width // 2, 300, button_width, button_height)
            button_tutorial = pygame.Rect(WINDOW_WIDTH // 2 - button_width // 2, 400, button_width, button_height)
            button_settings = pygame.Rect(WINDOW_WIDTH // 2 - button_width // 2, 500, button_width, button_height)
            button_quit = pygame.Rect(WINDOW_WIDTH // 2 - button_width // 2, 600, button_width, button_height)

            play_hovered = button_play.collidepoint((mx, my))
            tutorial_hovered = button_tutorial.collidepoint((mx, my))
            settings_hovered = button_settings.collidepoint((mx, my))
            quit_hovered = button_quit.collidepoint((mx, my))

            self.draw_button("Play", button_play, self.hover_color if play_hovered else self.button_color)
            self.draw_button("Tutorial", button_tutorial, self.hover_color if tutorial_hovered else self.button_color)
            self.draw_button("Settings", button_settings, self.hover_color if settings_hovered else self.button_color)
            self.draw_button("Quit Game", button_quit, self.hover_color if quit_hovered else self.quit_button_color)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if play_hovered:
                        self.button_sound.play()
                        selected_level = self.level_select()
                        print(f"Selected Level: {selected_level}")
                    elif tutorial_hovered:
                        self.button_sound.play()
                        self.tutorial()
                    elif settings_hovered:
                        self.button_sound.play()
                        self.settings()
                    elif quit_hovered:
                        pygame.quit()
                        sys.exit()

            pygame.display.update()

    def level_select(self):
        while True:
            level_bg = pygame.image.load("Graphics/backgrounds/Level_BG.png")
            self.screen.blit(level_bg, (0, 0))

            self.draw_text("Select a Level", self.font_custom, self.white, WINDOW_WIDTH // 2, 100)

            mx, my = pygame.mouse.get_pos()

            return_button = pygame.Rect(WINDOW_WIDTH // 2 - button_width // 2, 700, button_width, button_height)
            level1 = pygame.Rect((WINDOW_WIDTH - 3 * button_width - 2 * button_gap) // 2, 200, button_width, button_height)
            level2 = pygame.Rect(level1.right + button_gap, 200, button_width, button_height)
            level3 = pygame.Rect(level2.right + button_gap, 200, button_width, button_height)

            if level1.collidepoint((mx, my)):
                if pygame.mouse.get_pressed()[0]:
                    self.button_sound.play()
                    print("Level 1 Selected")
                    return 1
            if level2.collidepoint((mx, my)):
                if pygame.mouse.get_pressed()[0]:
                    self.button_sound.play()
                    print("Level 2 Selected")
                    return 2
            if level3.collidepoint((mx, my)):
                if pygame.mouse.get_pressed()[0]:
                    self.button_sound.play()
                    print("Level 3 Selected")
                    return 3
            if return_button.collidepoint((mx, my)):
                if pygame.mouse.get_pressed()[0]:
                    self.button_sound.play()
                    return

            pygame.draw.rect(self.screen, self.button_color, return_button)
            pygame.draw.rect(self.screen, self.button_color, level1)
            pygame.draw.rect(self.screen, self.button_color, level2)
            pygame.draw.rect(self.screen, self.button_color, level3)

            self.draw_text("Return", self.font_custom, self.white, return_button.centerx, return_button.centery)
            self.draw_text("Level 1", self.font_custom, self.white, level1.centerx, level1.centery)
            self.draw_text("Level 2", self.font_custom, self.white, level2.centerx, level2.centery)
            self.draw_text("Level 3", self.font_custom, self.white, level3.centerx, level3.centery)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            pygame.display.update()

    def tutorial(self):
        while True:
            tutorial_bg = pygame.image.load("Graphics/backgrounds/Level_BG.png")
            self.screen.blit(tutorial_bg, (0, 0))

            self.draw_text("Tutorial", self.font_custom, self.white, WINDOW_WIDTH // 2, 100)

            mx, my = pygame.mouse.get_pos()

            return_button = pygame.Rect(WINDOW_WIDTH // 2 - button_width // 2, 700, button_width, button_height)
            page1 = pygame.Rect(100, 200, 500, 400)
            page2 = pygame.Rect(700, 200, 500, 400)

            if return_button.collidepoint((mx, my)):
                if pygame.mouse.get_pressed()[0]:
                    self.button_sound.play()
                    return

            pygame.draw.rect(self.screen, self.button_color, return_button)
            pygame.draw.rect(self.screen, self.button_color, page1)
            pygame.draw.rect(self.screen, self.button_color, page2)

            self.draw_text("Return", self.font_custom, self.white, return_button.centerx, return_button.centery)
            self.draw_text("First text", self.font_custom, self.white, page1.centerx, page1.centery)
            self.draw_text("Second text", self.font_custom, self.white, page2.centerx, page2.centery)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            pygame.display.update()

    def settings(self):
        while True:
            tutorial_bg = pygame.image.load("Graphics/backgrounds/Level_BG.png")
            self.screen.blit(tutorial_bg, (0, 0))

            self.draw_text("Settings", self.font_custom, self.white, WINDOW_WIDTH // 2, 100)

            mx, my = pygame.mouse.get_pos()

            return_button = pygame.Rect(WINDOW_WIDTH // 2 - button_width // 2, 700, button_width, button_height)
            sfx_slider = pygame.Rect(WINDOW_WIDTH // 2 - slider_width // 2, 200, slider_width, slider_height)

            if return_button.collidepoint((mx, my)):
                if pygame.mouse.get_pressed()[0]:
                    self.button_sound.play()
                    return

            pygame.draw.rect(self.screen, self.button_color, return_button)
            pygame.draw.rect(self.screen, self.button_color, sfx_slider)

            self.draw_text("Return", self.font_custom, self.white, return_button.centerx, return_button.centery)
            self.draw_text("SFX slider", self.font_custom, self.white, sfx_slider.centerx, sfx_slider.centery)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            pygame.display.update()
