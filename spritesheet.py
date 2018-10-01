import pygame
import const

class SpriteSheet():
    """class to collect sprites from a spritesheet"""
    def __init__(self, file):
        #load image to pull sprites from
        self.sheet = pygame.image.load(file)

    def getSprite(self, x, y, wid, hei, flip = False):
        #grabs a single sprite from the sheet
        sprite = pygame.Surface([wid, hei])
        sprite.blit(self.sheet, (0,0), (x, y, wid, hei))
        sprite.set_colorkey(self.sheet.get_at((0,0)))
        if flip:
            sprite = pygame.transform.flip(sprite, True, False)
        return sprite

    def getSet(self, locations):
        #grabs multiple sprites, using the getSprite function
        spriteSet = []
        for loc in locations:
            sprite = self.getSprite(loc['x'], loc['y'], loc['wid'], loc['hei'], loc['flip'])
            spriteSet.append(sprite)
        return spriteSet
