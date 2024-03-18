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
        self.can_jump = True
        self.jump_force = jump_force
        self.gravity = gravity
        self.vertical_velocity = vertical_velocity
        self.rect = pygame.Rect(x, y, width, height)
        self.assets = {
            "player_idle": Animation(load_images("Idle_right"), img_dur=10),
            "player_jump": Animation(load_images("Jump_right")),
            # "player_run": Animation(load_images("Graphics/player/run"), img_dur=4)
        }
        self.current_animation = 'player_idle'

    def update_animation(self):
        if self.is_jumping:
            self.current_animation = 'player_jump'
        # elif self.move_left or self.move_right:
        # self.current_animation = 'player_run'
        else:
            self.current_animation = 'player_idle'

    def draw(self, camera):
        current_animation = self.assets[self.current_animation]  # Access the current animation
        current_animation.update()  # Update the animation frame
        current_frame = current_animation.img()  # Get the current frame

        rect = camera.apply(self.rect)
        self.screen.blit(current_frame, rect.topleft)

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                self.move_left = True
            if event.key == pygame.K_d:
                self.move_right = True
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
            if self.vertical_velocity > 0:
                self.is_jumping = False

        return new_x, new_y

    def update_position(self, new_x, new_y):
        self.x = new_x
        self.y = new_y
        self.rect = pygame.Rect(new_x, new_y, self.width, self.height)
