import pygame

class Background():
    """Background image that can scroll infinitely"""
    def __init__(self):
        self.image = pygame.image.load("data/background/Background.png")
        self.x1 = 0
        self.x2 = 1000

    def update(self, screen):
        #if about to scroll off the screen, move back to center
        if self.x1 < -900:
            self.x1 = self.x2
            self.x2 += 1000
        if self.x1 > -100:
            self.x2 = self.x1
            self.x1 -= 1000
        #draw
        screen.blit(self.image, (self.x1, 0))
        screen.blit(self.image, (self.x2, 0))

    def shift(self, diff):
        self.x1 += diff
        self.x2 += diff


class Camera():
    """Moves the stage and background when the player moves too close to the edge"""
    def __init__(self, enemies, platforms, arrows, lasers, player, background):
        #gets copies of all game items
        self.items = [enemies, platforms, arrows, lasers]
        self.player = player
        self.background = background
        self.displacement = 0

    def update(self):
        #checks player position on screen
        if self.player.rect.right > 500:
            diff = 500 - self.player.rect.right
            self.player.rect.right = 500
            self.shift(diff)
        if self.player.rect.left < 300:
            diff = 300 - self.player.rect.left
            self.player.rect.left = 300
            self.shift(diff)

    def shift(self, diff):
        #shifts level & enemies & background
        for item in self.items:
            for sprite in item:
                sprite.rect.x += diff
        self.background.shift(diff // 2)
        self.displacement -= diff
