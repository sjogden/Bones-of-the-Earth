import pygame
from spritesheet import SpriteSheet

class Platform(pygame.sprite.Sprite):
    """Platform sprite"""
    sheet = SpriteSheet("data/sprites/spritesheet.png")
    block = sheet.getSprite(49, 256, 21, 21)
    blockTop = sheet.getSprite(72, 233, 21, 21)
    door = sheet.getSprite(394, 95, 21, 21)
    doorTop = sheet.getSprite(371, 95, 21, 21)
    blockTypes = {"b":block, "bt":blockTop, "d":door, "dt":doorTop}

    def __init__(self, x, y, blockType):
        pygame.sprite.Sprite.__init__(self)
        if blockType in Platform.blockTypes:
            self.image = Platform.blockTypes[blockType]
        else:
            self.image = Platform.blockTypes["b"]

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    
