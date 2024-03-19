import pygame
import sys
from settings import *
import csv
from player import Player
from camera import Camera
from slider import Slider


class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption("AstroJump")

        num_tiles = 15
        self.tile_images = [pygame.image.load(f'Graphics/tiles/{i}.png') for i in range(num_tiles)]

        # colors
        self.white = (255, 255, 255)
        self.button_color = (0, 7, 78)
        self.quit_button_color = (125, 50, 50)
        self.quit_button_hover_color = (200, 50, 50)
        self.hover_color = (0, 50, 125)

        # player
        self.player = Player(100, 100, 50, 50, self.screen)
        self.initial_player_position = (self.player.x, self.player.y)

        # camera
        self.camera = Camera(MAP_WIDTH, MAP_HEIGHT)

        # sliders
        self.sfx_slider = Slider(810, 400, 300, 40, 0, 1, 0.5)
        self.music_slider = Slider(810, 500, 300, 40, 0, 1, 0.5)

        # fonts
        self.font_custom = pygame.font.Font("Graphics/fonts/pixel_font.ttf", 50)

        # sounds
        self.button_sound = pygame.mixer.Sound("Sounds/button_sound3.mp3")
        self.bg_music = "Sounds/BG_music2.mp3"
        pygame.mixer.music.load(self.bg_music)
        pygame.mixer.music.play(-1)

    def draw_text(self, text, font, color, x, y):
        text_obj = font.render(text, True, color)
        text_rect = text_obj.get_rect(center=(x, y))
        self.screen.blit(text_obj, text_rect)

    def draw_button(self, text, rect, color):
        pygame.draw.rect(self.screen, color, rect, border_radius=30)
        text_surface = self.font_custom.render(text, True, self.white)
        text_rect = text_surface.get_rect(center=rect.center)
        self.screen.blit(text_surface, text_rect)

    def main_menu(self):
        while True:
            bg = pygame.image.load("Graphics/backgrounds/BG.png")
            self.screen.blit(bg, (0, 0))

            self.draw_text("Astro Jump", self.font_custom, self.white, WINDOW_WIDTH // 2, 300)

            mx, my = pygame.mouse.get_pos()

            play_button = pygame.Rect(WINDOW_WIDTH // 2 - button_width // 2, 400, button_width, button_height)
            tutorial_button = pygame.Rect(WINDOW_WIDTH // 2 - button_width // 2, 500, button_width, button_height)
            settings_button = pygame.Rect(WINDOW_WIDTH // 2 - button_width // 2, 600, button_width, button_height)
            quit_button = pygame.Rect(WINDOW_WIDTH // 2 - button_width // 2, 700, button_width, button_height)

            play_hovered = play_button.collidepoint((mx, my))
            tutorial_hovered = tutorial_button.collidepoint((mx, my))
            settings_hovered = settings_button.collidepoint((mx, my))
            quit_hovered = quit_button.collidepoint((mx, my))

            self.draw_button("Play", play_button, self.hover_color if play_hovered else self.button_color)
            self.draw_button("Tutorial", tutorial_button, self.hover_color if tutorial_hovered else self.button_color)
            self.draw_button("Settings", settings_button, self.hover_color if settings_hovered else self.button_color)
            self.draw_button("Quit Game", quit_button, self.quit_button_hover_color if quit_hovered else self.quit_button_color)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if play_button.collidepoint((mx, my)):
                    if pygame.mouse.get_pressed()[0]:
                        self.button_sound.play()
                        self.level_select()

                if tutorial_button.collidepoint((mx, my)):
                    if pygame.mouse.get_pressed()[0]:
                        self.button_sound.play()
                        self.tutorial()

                if settings_button.collidepoint((mx, my)):
                    if pygame.mouse.get_pressed()[0]:
                        self.button_sound.play()
                        self.settings()

                if quit_button.collidepoint((mx, my)):
                    if pygame.mouse.get_pressed()[0]:
                        pygame.quit()
                        sys.exit()

            pygame.display.update()

    def level_select(self):
        while True:
            level_bg = pygame.image.load("Graphics/backgrounds/Level_BG.png")
            self.screen.blit(level_bg, (0, 0))

            self.draw_text("Select a Level", self.font_custom, self.white, WINDOW_WIDTH // 2, 175)

            mx, my = pygame.mouse.get_pos()

            return_button = pygame.Rect(WINDOW_WIDTH // 2 - button_width // 2, 800, button_width, button_height)
            level1 = pygame.Rect((WINDOW_WIDTH - 3 * button_width - 2 * button_gap) // 2, 250, button_width, button_height)
            level2 = pygame.Rect(level1.right + button_gap, 250, button_width, button_height)
            level3 = pygame.Rect(level2.right + button_gap, 250, button_width, button_height)

            return_hovered = return_button.collidepoint((mx, my))
            level1_hovered = level1.collidepoint((mx, my))
            level2_hovered = level2.collidepoint((mx, my))
            level3_hovered = level3.collidepoint((mx, my))

            self.draw_button("Return", return_button, self.hover_color if return_hovered else self.button_color)
            self.draw_button("Level 1", level1, self.hover_color if level1_hovered else self.button_color)
            self.draw_button("Level 2", level2, self.hover_color if level2_hovered else self.button_color)
            self.draw_button("Level 3", level3, self.hover_color if level3_hovered else self.button_color)

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

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        return

            pygame.display.update()

    def tutorial(self):
        while True:
            tutorial_bg = pygame.image.load("Graphics/backgrounds/Level_BG.png")
            self.screen.blit(tutorial_bg, (0, 0))

            mx, my = pygame.mouse.get_pos()

            return_button = pygame.Rect(WINDOW_WIDTH // 2 - button_width // 2, 900, button_width, button_height)
            page1 = pygame.Rect(250, 300, 500, 400)
            page2 = pygame.Rect(1170, 300, 500, 400)

            return_hovered = return_button.collidepoint((mx, my))

            self.draw_button("Return", return_button, self.hover_color if return_hovered else self.button_color)
            pygame.draw.rect(self.screen, self.button_color, page1, border_radius=30)
            pygame.draw.rect(self.screen, self.button_color, page2, border_radius=30)

            self.draw_text("Tutorial", self.font_custom, self.white, WINDOW_WIDTH // 2, 175)
            self.draw_text("Return", self.font_custom, self.white, return_button.centerx, return_button.centery)
            self.draw_text("A - move left", self.font_custom, self.white, page1.centerx, 350)
            self.draw_text("D - move right", self.font_custom, self.white, page1.centerx, 450)
            self.draw_text("Space - jump", self.font_custom, self.white, page1.centerx, 550)

            if return_button.collidepoint((mx, my)):
                if pygame.mouse.get_pressed()[0]:
                    self.button_sound.play()
                    return

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        return

            pygame.display.update()

    def settings(self):
        while True:
            tutorial_bg = pygame.image.load("Graphics/backgrounds/Level_BG.png")
            self.screen.blit(tutorial_bg, (0, 0))

            mx, my = pygame.mouse.get_pos()

            return_button = pygame.Rect(WINDOW_WIDTH // 2 - button_width // 2, 900, button_width, button_height)

            return_hovered = return_button.collidepoint((mx, my))

            self.draw_button("Return", return_button, self.hover_color if return_hovered else self.button_color)

            self.draw_text("Settings", self.font_custom, self.white, WINDOW_WIDTH // 2, 175)

            self.sfx_slider.draw(self.screen)
            self.music_slider.draw(self.screen)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                self.sfx_slider.handle_event(event, mx, my)
                self.music_slider.handle_event(event, mx, my)

                if event.type == pygame.MOUSEBUTTONUP:
                    self.button_sound.set_volume(self.sfx_slider.value)
                    pygame.mixer.music.set_volume(self.music_slider.value)

                if return_button.collidepoint((mx, my)):
                    if pygame.mouse.get_pressed()[0]:
                        self.button_sound.play()
                        return

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        return

            pygame.display.update()

    def respawn(self):
        main_menu_button = pygame.Rect(WINDOW_WIDTH // 2 - button_width // 2 - 20, 500, 300, button_height)
        respawn_button = pygame.Rect(WINDOW_WIDTH // 2 - button_width // 2, 400, button_width, button_height)

        mx, my = pygame.mouse.get_pos()
        main_menu_hovered = main_menu_button.collidepoint((mx, my))
        respawn_hovered = respawn_button.collidepoint((mx, my))

        if self.player.y > 1800:
            self.screen.fill((0, 0, 0))
            self.draw_text("You fell into the abyss", self.font_custom, self.quit_button_color, WINDOW_WIDTH // 2, 175)
            self.draw_button("Main menu", main_menu_button, self.hover_color if main_menu_hovered else self.button_color)
            self.draw_button("Respawn", respawn_button, self.hover_color if respawn_hovered else self.button_color)

            if respawn_button.collidepoint((mx, my)):
                if pygame.mouse.get_pressed()[0]:
                    self.player.x = self.player.initial_x
                    self.player.y = self.player.initial_y
                    self.player.vertical_velocity = 0
                    self.player.is_jumping = False
                    self.button_sound.play()

            if main_menu_button.collidepoint((mx, my)):
                if pygame.mouse.get_pressed()[0]:
                    self.player.x = self.player.initial_x
                    self.player.y = self.player.initial_y
                    self.player.vertical_velocity = 0
                    self.player.is_jumping = False
                    self.button_sound.play()
                    self.main_menu()
                    return

    # todo: it should be a game_menu_loop class
    def create_game_menu(self):

        while True:
            mx, my = pygame.mouse.get_pos()

            resume_button = pygame.Rect(WINDOW_WIDTH // 2 - button_width // 2, 400, button_width, button_height)
            quit_button = pygame.Rect(WINDOW_WIDTH // 2 - button_width // 2, 600, button_width, button_height)

            resume_hovered = resume_button.collidepoint((mx, my))
            quit_hovered = quit_button.collidepoint((mx, my))

            self.screen.fill((0, 0, 0))
            self.draw_button("Resume", resume_button, self.hover_color if resume_hovered else self.button_color)
            self.draw_button("Quit", quit_button, self.quit_button_hover_color if quit_hovered else self.quit_button_color)

            if resume_button.collidepoint((mx, my)):
                if pygame.mouse.get_pressed()[0]:
                    self.button_sound.play()
                    return

            if quit_button.collidepoint((mx, my)):
                if pygame.mouse.get_pressed()[0]:
                    self.button_sound.play()
                    self.main_menu()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            pygame.display.update()

    def show_map(self, map_filename=None):

        non_coll_tiles = [0]
        if map_filename is None:
            map_filename = "levels/level1.csv"

            # Load the map from the CSV file
        game_map = []
        with open(map_filename, 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                game_map.append([int(tile_id) for tile_id in row])

        tile_size = 64
        clock = pygame.time.Clock()
        self.camera = Camera(MAP_WIDTH, MAP_HEIGHT)

        while True:
            map_bg = pygame.image.load("Graphics/backgrounds/Level_BG.png").convert_alpha()
            self.screen.blit(map_bg, (0, 0))
            self.player.update_animation()

            # Handle events
            for event in pygame.event.get():
                self.handle_event(event)

            # Apply gravity
            new_x, new_y = self.apply_gravity()

            # Horizontal Collision Check
            for row_index, row in enumerate(game_map):
                for col_index, tile_id in enumerate(row):
                    if tile_id not in non_coll_tiles:
                        tile_rect = pygame.Rect(col_index * tile_size, row_index * tile_size, tile_size, tile_size)
                        player_rect = pygame.Rect(new_x, self.player.y, self.player.width,
                                                  self.player.height)  # Check horizontal movement first

                        if player_rect.colliderect(tile_rect):
                            if new_x > self.player.x:  # Moving right
                                new_x = tile_rect.left - self.player.width
                            elif new_x < self.player.x:  # Moving left
                                new_x = tile_rect.right

            # Vertical Collision Check
            for row_index, row in enumerate(game_map):
                for col_index, tile_id in enumerate(row):
                    if tile_id not in non_coll_tiles:
                        tile_rect = pygame.Rect(col_index * tile_size, row_index * tile_size, tile_size, tile_size)
                        player_rect = pygame.Rect(self.player.x, new_y, self.player.width, self.player.height)

                        if player_rect.colliderect(tile_rect):
                            if new_y > self.player.y:  # Falling down
                                new_y = tile_rect.top - self.player.height
                                self.player.vertical_velocity = 0
                                self.player.is_jumping = False
                                self.player.can_jump = True
                            elif new_y < self.player.y:  # Jumping up
                                new_y = tile_rect.bottom
                                self.player.vertical_velocity = 0

            self.player.update_position(new_x, new_y)
            self.camera.update(self.player)

            for row_index, row in enumerate(game_map):
                for col_index, tile_id in enumerate(row):
                    if tile_id not in non_coll_tiles:
                        tile_image = self.tile_images[tile_id]
                        tile_rect = pygame.Rect(col_index * TILE_SIZE, row_index * TILE_SIZE, TILE_SIZE, TILE_SIZE)
                        self.screen.blit(tile_image, self.camera.apply(tile_rect))

            self.respawn()
            self.player.draw(self.camera)
            pygame.display.update()
            clock.tick(60)

    def apply_gravity(self):
        if not self.player.is_jumping or self.player.vertical_velocity > 0:
            self.player.vertical_velocity += self.player.gravity
            self.player.is_jumping = True
        new_x, new_y = self.player.calculate_new_position()
        return new_x, new_y

    def handle_event(self, event):
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        self.player.handle_event(event)
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            self.create_game_menu()
