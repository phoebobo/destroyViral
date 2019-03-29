import pygame
from pygame.sprite import Sprite

#这是子弹类
class Bullet(pygame.sprite.Sprite):
    """A class to manage bullets fired from the ship."""

    def __init__(self, screen, ship):
        """Create a bullet object, at the ship's current position."""
        super().__init__()
        self.screen = screen
        self.image = pygame.image.load('./bullet.png')
        self.damage = 2  #子弹每一发的伤害
        # Create bullet rect at (0, 0), then set correct position.
        self.rect = self.image.get_rect()
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top
        self.speed = 1

    def update(self):
        """Move the bullet up the screen."""
        # Update the decimal position of the bullet.
        self.rect.y -= self.speed
        if self.rect.top < -self.rect.height:
            self.kill()
