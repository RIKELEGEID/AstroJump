import pygame
from settings import player_speed, jump_force, gravity, vertical_velocity


class Player:
    def __init__(self, x, y, width, height, screen, graphics=None):
        super().__init__()
        self.x = x
        self.y = y
        self.animations = {
            'idle_left': [],
        }
        self.load_images()
        self.state = 'idle_left'  # The initial state
        self.current_frame = 0
        self.image = self.animations[self.state][self.current_frame]
        self.rect = self.image.get_rect(topleft=(x, y))
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

    def load_images(self):
        # Load idle_left animation images
        for i in range(1, 12):
            image_path = f'Graphics/player/idle_left/player-1-{i}.png'
            image = pygame.image.load(image_path).convert_alpha()
            self.animations['idle_left'].append(image)

    def animate(self, dt):
        self.current_frame += 3 * dt  # Animation speed control
        if self.current_frame >= len(self.animations[self.state]):
            self.current_frame = 0
        self.image = self.animations[self.state][int(self.current_frame)]

    def draw(self, camera):
        self.screen.blit(self.image, camera.apply(self.rect))

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                self.move_left = True
                self.state = "idle_left"
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


