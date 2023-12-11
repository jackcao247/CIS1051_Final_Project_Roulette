import pygame
from random import randrange

class Wheel(pygame.sprite.Sprite):
    def __init__(self, game, x, y, filename, scale=1):
        pygame.sprite.Sprite.__init__(self)
        self.game = game
        self.default_image = pygame.image.load(filename).convert_alpha()
        orig_width, orig_height = self.default_image.get_size()
        self.default_image = pygame.transform.scale(self.default_image, (int(orig_width * scale), int(orig_height * scale)))
        self.image = self.default_image
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.spin_velocity = 0
        self.angle = 0
        self.wheel_friction = -0.005

    def update(self):
        if self.spin_velocity > 0:
            self.angle += self.spin_velocity % 360
            self.image = pygame.transform.rotate(self.default_image, self.angle)
            self.rect = self.image.get_rect()
            self.rect.center = self.game.game_width // 2, self.game.game_height // 2
            self.spin_velocity = (1 + self.wheel_friction) * self.spin_velocity
            if self.spin_velocity <= 0.5:
                self.spin_velocity = 0

class Static(pygame.sprite.Sprite):
    def __init__(self, game, x, y, filename, children_filename=None, movable=True, scale=1):
        pygame.sprite.Sprite.__init__(self)
        self.game = game
        self.image = pygame.image.load(filename).convert_alpha()
        orig_width, orig_height = self.image.get_size()
        self.image = pygame.transform.scale(self.image, (int(orig_width * scale), int(orig_height * scale)))
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.children_filename = children_filename
        self.movable = movable
        self.clicked = False

    def update(self):
        if self.clicked:
            self.rect.center = pygame.mouse.get_pos()

    def generate_child(self):
        child_sprite = Static(self.game, self.rect.centerx, self.rect.bottom, filename=self.children_filename)
        self.game.all_sprites.add(child_sprite)
