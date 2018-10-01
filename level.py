import pygame
import const
from camera import *
from platforms import Platform
from enemies import *
from collision import *

class Level():
    """Generic class for levels, drives main updates/draws"""
    def __init__(self, platformLoc, skeletonLoc, zombieLoc, player, endLoc):
        self.endLoc = endLoc
        self.background = Background()
        self.platformSprites = pygame.sprite.RenderPlain()
        self.enemySprites = pygame.sprite.RenderPlain()
        self.arrowSprites = pygame.sprite.RenderPlain()
        self.playerSprite = pygame.sprite.RenderPlain(player)
        self.laserSprites = player.laserSprites
        self.swordBoxSprites = player.swordBoxSprites

        for platform in platformLoc:
            self.platformSprites.add(Platform(platform[0], platform[1], platform[2]))
        for skeleton in skeletonLoc:
            self.enemySprites.add(Skeleton(skeleton[0], skeleton[1], self.arrowSprites, self.platformSprites))
        for zombie in zombieLoc:
            self.enemySprites.add(Zombie(zombie[0], zombie[1], self.platformSprites))

        self.camera = Camera(self.enemySprites, self.platformSprites, self.arrowSprites, self.laserSprites, player, self.background)

    def update(self):
        self.enemySprites.update()
        self.arrowSprites.update()
        self.playerSprite.update()
        self.laserSprites.update()
        self.swordBoxSprites.update()
        checkDamage(self.playerSprite, self.enemySprites, self.laserSprites, self.arrowSprites, self.swordBoxSprites)
        projectileWallCol(self.laserSprites, self.arrowSprites, self.platformSprites)
        self.camera.update()
        
    def draw(self, screen):
        self.background.update(screen)
        self.platformSprites.draw(screen)
        self.enemySprites.draw(screen)
        self.arrowSprites.draw(screen)
        self.playerSprite.draw(screen)
        self.laserSprites.draw(screen)


class Tutorial(Level):
    """specialized class for tutorial level to display text"""
    def __init__(self, platformLoc, skeletonLoc, zombieLoc, player, endLoc):
        Level.__init__(self, platformLoc, skeletonLoc, zombieLoc, player, endLoc)
        font = pygame.font.Font("data\\fonts\LCD_Solid.ttf", 20)
        self.instructions = {font.render("Use 'A' and 'D' to Move", 1, const.WHITE):0,
                             font.render("'W' to Jump", 1, const.WHITE):500,
                             font.render("Swing your sword with 'J'", 1, const.WHITE):800,
                             font.render("Shoot with 'K'", 1, const.WHITE):1400,
                             font.render("Go through the door to move on to the next level", 1, const.WHITE):1850}
    def draw(self, screen):
        Level.draw(self, screen)
        for text in self.instructions:
            screen.blit(text, (self.instructions[text] - self.camera.displacement, 300))


class BossLevel(Level):
    """specialized class for boss level, can't move on til area is cleared"""
    def __init__(self, platformLoc, skeletonLoc, zombieLoc, player, endLoc, bossLoc):
        Level.__init__(self, platformLoc, skeletonLoc, zombieLoc, player, endLoc)
        self.realEndLoc = self.endLoc
        self.endLoc += 100
        self.enemySprites.add(Boss(bossLoc[0], bossLoc[1], self.arrowSprites, self.platformSprites))

    def update(self):
        Level.update(self)
        if not self.enemySprites:
            self.endLoc = self.realEndLoc

