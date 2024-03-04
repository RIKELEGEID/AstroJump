import pygame
import sys
from Settings import *
import csv
from Player import Player


class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption("AstroJump")
        self.tile_images = [pygame.image.load(f'Graphics/tiles/tile{i}.png') for i in
                            range(0, 14)]  # todo: dynamické nářítaní libovolného počtu tilů    

        # colors
        self.black = (0, 0, 0)
        self.white = (255, 255, 255)
        self.button_color = (50, 50, 50)
        self.quit_button_color = (125, 50, 50)
        self.hover_color = (100, 100, 100)
        self.slider_handle_color = (125, 50, 50)

        # player
        self.player = Player(100, 100, 50, 50, self.screen)

        # fonts
        self.font_custom = pygame.font.Font("Graphics/fonts/pixel_font.ttf", 36)

        # sounds
        self.button_sound = pygame.mixer.Sound("Sounds/button_sound3.mp3")
        self.bg_music = "Sounds/BG_music.mp3"
        pygame.mixer.music.load(self.bg_music)
        pygame.mixer.music.play(-1)

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
                        if selected_level == 1:
                            self.show_map()

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
            level1 = pygame.Rect((WINDOW_WIDTH - 3 * button_width - 2 * button_gap) // 2, 200, button_width,
                                 button_height)
            level2 = pygame.Rect(level1.right + button_gap, 200, button_width, button_height)
            level3 = pygame.Rect(level2.right + button_gap, 200, button_width, button_height)

            pygame.draw.rect(self.screen, self.button_color, return_button)
            pygame.draw.rect(self.screen, self.button_color, level1)
            pygame.draw.rect(self.screen, self.button_color, level2)
            pygame.draw.rect(self.screen, self.button_color, level3)

            self.draw_text("Return", self.font_custom, self.white, return_button.centerx, return_button.centery)
            self.draw_text("Level 1", self.font_custom, self.white, level1.centerx, level1.centery)
            self.draw_text("Level 2", self.font_custom, self.white, level2.centerx, level2.centery)
            self.draw_text("Level 3", self.font_custom, self.white, level3.centerx, level3.centery)

            if level1.collidepoint((mx, my)):
                if pygame.mouse.get_pressed()[0]:
                    self.button_sound.play()
                    self.show_map("levels/level1.csv")

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

            pygame.draw.rect(self.screen, self.button_color, return_button)
            pygame.draw.rect(self.screen, self.button_color, page1)
            pygame.draw.rect(self.screen, self.button_color, page2)

            self.draw_text("Return", self.font_custom, self.white, return_button.centerx, return_button.centery)
            self.draw_text("First text", self.font_custom, self.white, page1.centerx, page1.centery)
            self.draw_text("Second text", self.font_custom, self.white, page2.centerx, page2.centery)

            if return_button.collidepoint((mx, my)):
                if pygame.mouse.get_pressed()[0]:
                    self.button_sound.play()
                    return

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            pygame.display.update()

    def settings(self):
        while True:
            tutorial_bg = pygame.image.load("Graphics/backgrounds/Level_BG.png")
            self.screen.blit(tutorial_bg, (0, 0))

            mx, my = pygame.mouse.get_pos()

            return_button = pygame.Rect(WINDOW_WIDTH // 2 - button_width // 2, 700, button_width, button_height)
            sfx_vol1 = pygame.Rect(200, 300, button_width, button_height)
            sfx_vol2 = pygame.Rect(200, 400, button_width, button_height)
            sfx_vol3 = pygame.Rect(200, 500, button_width, button_height)
            sfx_vol4 = pygame.Rect(200, 600, button_width, button_height)
            music_vol1 = pygame.Rect(900, 300, button_width, button_height)
            music_vol2 = pygame.Rect(900, 400, button_width, button_height)
            music_vol3 = pygame.Rect(900, 500, button_width, button_height)
            music_vol4 = pygame.Rect(900, 600, button_width, button_height)

            pygame.draw.rect(self.screen, self.button_color, return_button)
            pygame.draw.rect(self.screen, self.button_color, sfx_vol1)
            pygame.draw.rect(self.screen, self.button_color, sfx_vol2)
            pygame.draw.rect(self.screen, self.button_color, sfx_vol3)
            pygame.draw.rect(self.screen, self.button_color, sfx_vol4)
            pygame.draw.rect(self.screen, self.button_color, music_vol1)
            pygame.draw.rect(self.screen, self.button_color, music_vol2)
            pygame.draw.rect(self.screen, self.button_color, music_vol3)
            pygame.draw.rect(self.screen, self.button_color, music_vol4)

            self.draw_text("Settings", self.font_custom, self.white, WINDOW_WIDTH // 2, 100)
            self.draw_text("SFX volume", self.font_custom, self.white, 300, 200)
            self.draw_text("Music volume", self.font_custom, self.white, 1000, 200)
            self.draw_text("Return", self.font_custom, self.white, return_button.centerx, return_button.centery)
            self.draw_text("4", self.font_custom, self.white, sfx_vol1.centerx, sfx_vol1.centery)
            self.draw_text("3", self.font_custom, self.white, sfx_vol2.centerx, sfx_vol2.centery)
            self.draw_text("2", self.font_custom, self.white, sfx_vol3.centerx, sfx_vol3.centery)
            self.draw_text("1", self.font_custom, self.white, sfx_vol4.centerx, sfx_vol4.centery)
            self.draw_text("4", self.font_custom, self.white, music_vol1.centerx, music_vol1.centery)
            self.draw_text("3", self.font_custom, self.white, music_vol2.centerx, music_vol2.centery)
            self.draw_text("2", self.font_custom, self.white, music_vol3.centerx, music_vol3.centery)
            self.draw_text("1", self.font_custom, self.white, music_vol4.centerx, music_vol4.centery)

            if sfx_vol1.collidepoint((mx, my)):
                if pygame.mouse.get_pressed()[0]:
                    self.button_sound.play()
                    self.button_sound.set_volume(1)

            if sfx_vol2.collidepoint((mx, my)):
                if pygame.mouse.get_pressed()[0]:
                    self.button_sound.play()
                    self.button_sound.set_volume(0.7)

            if sfx_vol3.collidepoint((mx, my)):
                if pygame.mouse.get_pressed()[0]:
                    self.button_sound.play()
                    self.button_sound.set_volume(0.4)

            if sfx_vol4.collidepoint((mx, my)):
                if pygame.mouse.get_pressed()[0]:
                    self.button_sound.play()
                    self.button_sound.set_volume(0.2)

            if music_vol1.collidepoint((mx, my)):
                if pygame.mouse.get_pressed()[0]:
                    self.button_sound.play()
                    pygame.mixer.music.set_volume(1)

            if music_vol2.collidepoint((mx, my)):
                if pygame.mouse.get_pressed()[0]:
                    self.button_sound.play()
                    pygame.mixer.music.set_volume(0.6)

            if music_vol3.collidepoint((mx, my)):
                if pygame.mouse.get_pressed()[0]:
                    self.button_sound.play()
                    pygame.mixer.music.set_volume(0.3)

            if music_vol4.collidepoint((mx, my)):
                if pygame.mouse.get_pressed()[0]:
                    self.button_sound.play()
                    pygame.mixer.music.set_volume(0.05)

            if return_button.collidepoint((mx, my)):
                if pygame.mouse.get_pressed()[0]:
                    self.button_sound.play()
                    return

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            pygame.display.update()

    def show_map(self, map_filename=None):  # todo: rozkouskovat na map nebo level class
        while True:
            if map_filename is None:
                map_filename = "levels/level1.csv"

            # Load the map from the CSV file
            game_map = []
            with open("levels/level1.csv", 'r') as file:
                reader = csv.reader(file)
                for row in reader:
                    game_map.append([int(tile_id) for tile_id in row])

            tile_size = 64
            for row in range(len(game_map)):
                for col in range(len(game_map[row])):
                    tile_id = game_map[row][col]
                    tile_image = self.tile_images[tile_id]
                    tile_rect = tile_image.get_rect(topleft=(col * tile_size, row * tile_size))
                    self.screen.blit(tile_image, tile_rect)

            self.player.draw()

            for event in pygame.event.get():
                self.player.handle_event(event)
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            if self.player.is_moving():
                self.player.move()

            pygame.display.update()


