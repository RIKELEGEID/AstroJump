import pygame
from settings import player_speed, jump_force, gravity, vertical_velocity
from animation import load_images, Animation


class Player:
    def __init__(self, x, y, width, height, screen, graphics=None):
        self.x = x
        self.y = y
        self.initial_x = x
        self.initial_y = y
        self.width = width
        self.height = height
        self.screen = screen
        self.graphics = graphics
        self.speed = player_speed
        self.move_left = False
        self.move_right = False
        self.move_up = False
        self.is_jumping = False
        self.is_falling = False
        self.can_jump = True
        self.jump_force = jump_force
        self.gravity = gravity
        self.vertical_velocity = vertical_velocity
        self.rect = pygame.Rect(x, y, width, height)
        self.facing_right = True
        self.assets = {
            "player_idle": Animation(load_images("Idle"), img_dur=10),
            "player_jump": Animation(load_images("Jump")),
            "player_run": Animation(load_images("run"), img_dur=4),
            "player_fall": Animation(load_images("fall"))
        }
        self.current_animation = 'player_idle'

    def update_animation(self):
        if self.is_jumping:
            self.current_animation = "player_jump"
        elif self.move_left or self.move_right:
            self.current_animation = "player_run"
        elif self.is_falling:
            self.current_animation = "player_fall"
        else:
            self.current_animation = "player_idle"

    def draw(self, camera):
        current_animation = self.assets[self.current_animation]  # Access the current animation
        current_animation.update()  # Update the animation frame
        current_frame = current_animation.img()  # Get the current frame
        if not self.facing_right:
            current_frame = pygame.transform.flip(current_frame, True, False)

        rect = camera.apply(self.rect)
        self.screen.blit(current_frame, rect.topleft)

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                self.move_left = True
                self.facing_right = False
            if event.key == pygame.K_d:
                self.move_right = True
                self.facing_right = True
            if event.key == pygame.K_SPACE:
                if not self.is_jumping and self.can_jump:
                    self.is_jumping = True
                    self.can_jump = False
                    self.vertical_velocity = -self.jump_force

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                self.move_left = False
            if event.key == pygame.K_d:
                self.move_right = False

    def is_moving(self):
        return self.move_left or self.move_right or self.is_jumping or self.is_falling

    def calculate_new_position(self):
        new_x = self.x
        new_y = self.y

        if self.move_left:
            new_x -= self.speed
        if self.move_right:
            new_x += self.speed

        if self.is_jumping or self.is_falling:
            new_y += self.vertical_velocity
            self.vertical_velocity += self.gravity

            if self.vertical_velocity > 1:
                self.is_falling = True
                self.is_jumping = False
            else:
                self.is_falling = False

        return new_x, new_y

    def update_position(self, new_x, new_y):
        self.x = new_x
        self.y = new_y
        self.rect = pygame.Rect(new_x, new_y, self.width, self.height)
