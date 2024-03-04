import pygame
from Settings import player_colour, player_speed


class Player:
    def __init__(self, x, y, width, height, screen, graphics=None):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.screen = screen
        self.graphics = graphics
        self.speed = player_speed
        self.move_left = False
        self.move_right = False
        self.move_up = False
        self.move_down = False
        self.is_jumping = False
        self.jump_count = 0
        self.max_jump_count = 10  # Adjust as needed

        # Gravity attributes
        self.gravity = 1

    def draw(self):
        rect = pygame.Rect(self.x, self.y, self.width, self.height)
        pygame.draw.rect(self.screen, player_colour, rect)

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                self.move_left = True
            if event.key == pygame.K_d:
                self.move_right = True
            if event.key == pygame.K_w:
                self.move_up = True
            if event.key == pygame.K_s:
                self.move_down = True

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                self.move_left = False
            if event.key == pygame.K_d:
                self.move_right = False
            if event.key == pygame.K_w:
                self.move_up = False
            if event.key == pygame.K_s:
                self.move_down = False

    def is_moving(self):
        return self.move_left or self.move_right or self.move_up or self.move_down

    def move(self):
        if self.move_left:
            self.x -= self.speed
        if self.move_right:
            self.x += self.speed
        if self.move_up:
            self.y -= self.speed
        if self.move_down:
            self.y += self.speed

    def apply_gravity(self):
        self.y += self.gravity

    def jump(self):
        if self.is_on_ground() and not self.is_jumping:
            self.is_jumping = True
            self.jump_count = self.max_jump_count

    def is_on_ground(self):
        # Assuming the game_map is a 2D array representing the tiles in the game
        # You may need to adjust this logic based on your specific implementation
        player_bottom = self.y + self.height
        tile_size = 64  # Adjust if needed

        # Check the tile below the player's feet
        row = int(player_bottom // tile_size)
        col = int(self.x // tile_size)

        # Check if the tile is solid (not 0)
        return game_map[row][col] != 0

    def is_falling(self):
        # Check if the player is currently in a falling state
        return not self.is_on_ground()
