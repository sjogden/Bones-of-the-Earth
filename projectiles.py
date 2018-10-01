import pygame
import const
from spritesheet import SpriteSheet

class Laser(pygame.sprite.Sprite):
    """Sprite controller for laser"""
    def __init__(self, x, y, right):
        pygame.sprite.Sprite.__init__(self)
        self.frame = 0
        self.right = right
        if self.right:
            self.dx = 10
        else:
            self.dx = -10
        sheet = SpriteSheet('data\sprites\player1.bmp')
        self.spLaserLoc = [{"x":464, "y":83, "wid":24, "hei":24, "flip":False},
                           {"x":493, "y":83, "wid":24, "hei":24, "flip":False}]
        self.spLaser = sheet.getSet(self.spLaserLoc)
        self.image = self.spLaser[0]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self):
        self.rect.x += self.dx

        if self.frame >= len(self.spLaser)*3:
            self.frame = 0
        self.image = self.spLaser[self.frame // 3]
        self.frame += 1

class Arrow(pygame.sprite.Sprite):
    """Sprite controller for arrow"""
    def __init__(self, x, y, right):
        pygame.sprite.Sprite.__init__(self)
        self.right = right
        if self.right:
            self.dx = 10
        else:
            self.dx = -10
        sheet = SpriteSheet('data\sprites\skeleton.png')
        self.spArrow = sheet.getSprite(260, 23, 43, 8, not right)
        self.image = self.spArrow
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self):
        self.rect.x += self.dx


class SwordBox(pygame.sprite.Sprite):
    """hitbox for sword swing"""
    def __init__(self, player):
        pygame.sprite.Sprite.__init__(self)
        self.rect = pygame.Rect(player.rect.x - 20, player.rect.y, player.rect.width + 40, player.rect.height)
        self.player = player

    def update(self):
        if not self.player.hitBox:
            self.kill()
        self.rect.x = self.player.rect.x - 20
        self.rect.width = self.player.rect.width + 40
