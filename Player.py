import pygame
from Settings import player_colour, player_speed, jump_force, gravity, vertical_velocity


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
        self.is_jumping = False
        self.jump_force = jump_force
        self.gravity = gravity
        self.vertical_velocity = vertical_velocity

    def draw(self):
        rect = pygame.Rect(self.x, self.y, self.width, self.height)
        pygame.draw.rect(self.screen, player_colour, rect)

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                self.move_left = True
            if event.key == pygame.K_d:
                self.move_right = True
            if event.key == pygame.K_SPACE:
                if not self.is_jumping:
                    self.is_jumping = True
                    self.vertical_velocity = -self.jump_force

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                self.move_left = False
            if event.key == pygame.K_d:
                self.move_right = False

    def is_moving(self):
        return self.move_left or self.move_right or self.is_jumping

    def calculate_new_position(self):
        new_x = self.x
        new_y = self.y

        if self.move_left:
            new_x -= self.speed
        if self.move_right:
            new_x += self.speed

        if self.is_jumping:
            new_y += self.vertical_velocity
            self.vertical_velocity += self.gravity
            if self.vertical_velocity > 0:  # This condition ensures that we know when the player is falling
                self.is_jumping = False  # Optionally reset jump here or upon collision detection with the ground

        return new_x, new_y

    def update_position(self, new_x, new_y):
        self.x = new_x
        self.y = new_y
