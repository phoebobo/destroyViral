import pygame
from bullet import Bullet

class Airplane(pygame.sprite.Sprite):
    def __init__(self,screen):
        pygame.sprite.Sprite.__init__(self)
        self.screen = screen
        self.image = pygame.image.load('./airplane.jpg')
        self.rect = self.image.get_rect()
        self.rect.centerx = 300
        self.rect.top = 800 - 54
        self.speed = 2

        # 根据按键事件来移动
    def update(self, pressed_keys):
            # 按键事件
        if pressed_keys[pygame.K_LEFT] or pressed_keys[pygame.K_a]:
            if self.rect.left > 0:
                self.rect.left -= self.speed
        elif pressed_keys[pygame.K_RIGHT] or pressed_keys[pygame.K_d]:
            if self.rect.left < 600 - self.image.get_width():
                self.rect.left += self.speed
        if pressed_keys[pygame.K_UP] or pressed_keys[pygame.K_w]:
            if self.rect.top > 0:
                self.rect.top -= self.speed
        elif pressed_keys[pygame.K_DOWN] or pressed_keys[pygame.K_s]:
            if self.rect.top < 800 - self.image.get_height():
                self.rect.top += self.speed


