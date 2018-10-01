import pygame
pygame.init()
import const
from spritesheet import SpriteSheet
from projectiles import Arrow, Laser
import random

class Enemy(pygame.sprite.Sprite):
    """Parent class for all enemies"""
    def __init__(self, x, y, platformSprites):
        pygame.sprite.Sprite.__init__(self)
        self.level = platformSprites
        self.dx = 0
        self.dy = 0
        self.right = False
        self.moving = True
        self.shoot = False
        self.attacking = False
        self.falling = False
        self.frame = 0
        self.hp = 100
        self.animation = []
                
    def update(self):
        if self.frame >= len(self.animation)*6:
            self.frame = 0
            if self.attacking:
                self.attacking = False
                self.shoot = False
        self.image = self.animation[self.frame // 6]
        self.frame += 1


        self.move()
        if not self.onGround():
            self.falling = True
            self.dy += 1
        else:
            self.falling = False
            self.dy = 0
        if self.rect.top > const.SCR_HEI:
            self.kill()

    def onGround(self):
        self.rect.y += 1
        abovePlat = pygame.sprite.spritecollide(self, self.level, False)
        self.rect.y -= 1
        if abovePlat:
            return True
        return False

    def move(self):
        temp = self.rect.x
        self.rect.x += self.dx
        plats = pygame.sprite.spritecollide(self, self.level, False)
        if plats:
            if temp < plats[0].rect.x:
                self.rect.right = plats[0].rect.left
            else:
                self.rect.left = plats[0].rect.right

        temp = self.rect.y
        self.rect.y += self.dy
        plats = pygame.sprite.spritecollide(self, self.level, False)
        if plats:
            if temp > plats[0].rect.y:
                self.rect.top = plats[0].rect.bottom
                self.dy = 0
            else:
                self.rect.bottom = plats[0].rect.top
        
    def damage(self, damage, right):
        self.hp -= damage
        temp = self.rect.x
        if right:
            self.rect.x += 50
        else:
            self.rect.x -= 50
        plats = pygame.sprite.spritecollide(self, self.level, False)
        if plats:
            if temp < plats[0].rect.x:
                self.rect.right = plats[0].rect.left
            else:
                self.rect.left = plats[0].rect.right

        if self.hp <= 0:
            self.kill()


class Skeleton(Enemy):
    """sprite for skeleton enemy"""
    arrowSound = pygame.mixer.Sound("data\\sounds\\arrowSound.wav")
    def __init__(self, x, y, arrowSprites, platformSprites):
        Enemy.__init__(self, x, y, platformSprites)
        self.arrowSprites = arrowSprites
        self.spMoveLeft = []
        self.spMoveRight = []
        self.spShootLeft = []
        self.spShootRight = []
        
        self.spMoveLeftLoc = [{'x':0, 'y':0, 'wid':62, 'hei':62, 'flip':True},
                              {'x':62, 'y':0, 'wid':62, 'hei':62, 'flip':True},
                              {'x':124, 'y':0, 'wid':62, 'hei':62, 'flip':True},
                              {'x':186, 'y':0, 'wid':62, 'hei':62, 'flip':True}]

        self.spMoveRightLoc = [{'x':0, 'y':0, 'wid':62, 'hei':62, 'flip':False},
                               {'x':62, 'y':0, 'wid':62, 'hei':62, 'flip':False},
                               {'x':124, 'y':0, 'wid':62, 'hei':62, 'flip':False},
                               {'x':186, 'y':0, 'wid':62, 'hei':62, 'flip':False}]

        self.spShootLeftLoc = [{'x':0, 'y':62, 'wid':62, 'hei':62, 'flip':True},
                               {'x':62, 'y':62, 'wid':62, 'hei':62, 'flip':True},
                               {'x':124, 'y':62, 'wid':62, 'hei':62, 'flip':True},
                               {'x':186, 'y':62, 'wid':62, 'hei':62, 'flip':True},
                               {'x':248, 'y':62, 'wid':62, 'hei':62, 'flip':True}]

        self.spShootRightLoc = [{'x':0, 'y':62, 'wid':62, 'hei':62, 'flip':False},
                                {'x':62, 'y':62, 'wid':62, 'hei':62, 'flip':False},
                                {'x':124, 'y':62, 'wid':62, 'hei':62, 'flip':False},
                                {'x':186, 'y':62, 'wid':62, 'hei':62, 'flip':False},
                                {'x':248, 'y':62, 'wid':62, 'hei':62, 'flip':False}]
        
        sheet = SpriteSheet('data\sprites\skeleton.png')
        self.spMoveLeft = sheet.getSet(self.spMoveLeftLoc)
        self.spMoveRight = sheet.getSet(self.spMoveRightLoc)
        self.spShootLeft = sheet.getSet(self.spShootLeftLoc)
        self.spShootRight = sheet.getSet(self.spShootRightLoc)

        self.image = self.spMoveLeft[0]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        
    def update(self):
        #randomly determine action
        if not self.attacking:
            r = random.randint(0, 40)
            if r == 0:
                self.right = not self.right
            if self.moving:
                if self.right:
                    self.animation = self.spMoveRight
                    self.dx = 1
                else:
                    self.animation = self.spMoveLeft
                    self.dx = -1
            r = random.randint(0, 180)
            if r == 0 and not self.falling:
                self.shoot = True

        if self.shoot:
            self.dx = 0
            self.dy = 0
            if not self.attacking:
                self.frame = 0
                self.attacking = True
                Skeleton.arrowSound.play()
            if self.right:
                self.animation = self.spShootRight
                if self.frame == 18:
                    arrow = Arrow(self.rect.x + 44, self.rect.y + 24, self.right)
                    self.arrowSprites.add(arrow)
            else:
                self.animation = self.spShootLeft
                if self.frame == 18:
                    arrow = Arrow(self.rect.x + 18, self.rect.y + 24, self.right)
                    self.arrowSprites.add(arrow)

        Enemy.update(self)


class Zombie(Enemy):
    """Sprite for zombie enemy"""
    def __init__(self, x, y, platformSprites):
        Enemy.__init__(self, x, y, platformSprites)
        self.spMoveLeft = []
        self.spMoveRight = []
        
        self.spMoveLeftLoc = [{'x':0, 'y':0, 'wid':31, 'hei':45, 'flip':False},
                              {'x':33, 'y':0, 'wid':30, 'hei':45, 'flip':False},
                              {'x':64, 'y':0, 'wid':31, 'hei':45, 'flip':False}]

        self.spMoveRightLoc = [{'x':0, 'y':0, 'wid':31, 'hei':45, 'flip':True},
                               {'x':33, 'y':0, 'wid':30, 'hei':45, 'flip':True},
                               {'x':64, 'y':0, 'wid':31, 'hei':45, 'flip':True}]

        sheet = SpriteSheet('data\sprites\zombie.gif')
        self.spMoveLeft = sheet.getSet(self.spMoveLeftLoc)
        self.spMoveRight = sheet.getSet(self.spMoveRightLoc)

        self.image = self.spMoveLeft[0]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        
    def update(self):
        #randomly determine direction
        r = random.randint(0, 40)
        if r == 0:
            self.right = not self.right
        if self.moving:
            if self.right:
                self.animation = self.spMoveRight
                self.dx = 2
            else:
                self.animation = self.spMoveLeft
                self.dx = -2

        Enemy.update(self)


class Boss(Enemy):
    """sprite for boss (mirror image of player)"""
    laserSound = pygame.mixer.Sound("data\\sounds\\laserSound.wav")
    def __init__(self, x, y, arrowSprites, platformSprites):
        Enemy.__init__(self, x, y, platformSprites)
        self.hp = 500
        self.font = pygame.font.Font("data\\fonts\LCD_Solid.ttf", 16)
        self.arrowSprites = arrowSprites
        self.spMoveLeft = []
        self.spMoveRight = []
        self.spShootLeft = []
        self.spShootRight = []

        self.spMoveLeftLoc = [{'x':2, 'y':122, 'wid':52, 'hei':47, 'flip':True},
                              {'x':55, 'y':122, 'wid':52, 'hei':47, 'flip':True},
                              {'x':107, 'y':122, 'wid':52, 'hei':47, 'flip':True},
                              {'x':160, 'y':122, 'wid':52, 'hei':47, 'flip':True},
                              {'x':216, 'y':122, 'wid':52, 'hei':47, 'flip':True},
                              {'x':269, 'y':122, 'wid':52, 'hei':47, 'flip':True},
                              {'x':324, 'y':122, 'wid':52, 'hei':47, 'flip':True},
                              {'x':377, 'y':122, 'wid':52, 'hei':47, 'flip':True},]

        self.spMoveRightLoc = [{'x':2, 'y':122, 'wid':52, 'hei':47, 'flip':False},
                               {'x':55, 'y':122, 'wid':52, 'hei':47, 'flip':False},
                               {'x':107, 'y':122, 'wid':52, 'hei':47, 'flip':False},
                               {'x':160, 'y':122, 'wid':52, 'hei':47, 'flip':False},
                               {'x':216, 'y':122, 'wid':52, 'hei':47, 'flip':False},
                               {'x':269, 'y':122, 'wid':52, 'hei':47, 'flip':False},
                               {'x':324, 'y':122, 'wid':52, 'hei':47, 'flip':False},
                               {'x':377, 'y':122, 'wid':52, 'hei':47, 'flip':False},]

        self.spFallLeftLoc = [{'x':415, 'y':169, 'wid':49, 'hei':62, 'flip':True},
                              {'x':466, 'y':169, 'wid':49, 'hei':62, 'flip':True}]

        self.spFallRightLoc = [{'x':415, 'y':169, 'wid':49, 'hei':62, 'flip':False},
                              {'x':466, 'y':169, 'wid':49, 'hei':62, 'flip':False}]

        self.spShootLeftLoc = [{'x':8, 'y':307, 'wid':49, 'hei':52, 'flip':True},
                               {'x':59, 'y':307, 'wid':51, 'hei':52, 'flip':True},
                               {'x':111, 'y':307, 'wid':51, 'hei':52, 'flip':True},
                               {'x':164, 'y':307, 'wid':55, 'hei':52, 'flip':True},
                               {'x':220, 'y':307, 'wid':57, 'hei':52, 'flip':True},
                               {'x':279, 'y':307, 'wid':61, 'hei':52, 'flip':True},
                               {'x':343, 'y':307, 'wid':60, 'hei':52, 'flip':True},
                               {'x':405, 'y':307, 'wid':60, 'hei':52, 'flip':True},
                               {'x':469, 'y':307, 'wid':62, 'hei':52, 'flip':True},
                               {'x':537, 'y':307, 'wid':63, 'hei':52, 'flip':True},
                               {'x':603, 'y':307, 'wid':61, 'hei':52, 'flip':True}]

        self.spShootRightLoc = [{'x':8, 'y':307, 'wid':49, 'hei':52, 'flip':False},
                                {'x':59, 'y':307, 'wid':51, 'hei':52, 'flip':False},
                                {'x':111, 'y':307, 'wid':51, 'hei':52, 'flip':False},
                                {'x':164, 'y':307, 'wid':55, 'hei':52, 'flip':False},
                                {'x':220, 'y':307, 'wid':57, 'hei':52, 'flip':False},
                                {'x':279, 'y':307, 'wid':61, 'hei':52, 'flip':False},
                                {'x':343, 'y':307, 'wid':60, 'hei':52, 'flip':False},
                                {'x':405, 'y':307, 'wid':60, 'hei':52, 'flip':False},
                                {'x':469, 'y':307, 'wid':62, 'hei':52, 'flip':False},
                                {'x':537, 'y':307, 'wid':63, 'hei':52, 'flip':False},
                                {'x':603, 'y':307, 'wid':61, 'hei':52, 'flip':False}]

        sheet = SpriteSheet('data\sprites\player1.bmp')
        self.spMoveLeft = sheet.getSet(self.spMoveLeftLoc)
        self.spMoveRight = sheet.getSet(self.spMoveRightLoc)
        self.spFallLeft = sheet.getSet(self.spFallLeftLoc)
        self.spFallRight = sheet.getSet(self.spFallRightLoc)
        self.spShootLeft = sheet.getSet(self.spShootLeftLoc)
        self.spShootRight = sheet.getSet(self.spShootRightLoc)

        self.image = self.spMoveLeft[0]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        
    def update(self):
        #randomly determine action
        if not self.attacking:
            r = random.randint(0, 40)
            if r == 0:
                self.right = not self.right
            if self.moving:
                if self.right:
                    self.animation = self.spMoveRight
                    self.dx = 2
                else:
                    self.animation = self.spMoveLeft
                    self.dx = -2
            r = random.randint(0, 60)
            if r == 0 and not self.falling:
                self.shoot = True

        if self.falling:
            if self.right:
                self.animation = self.spFallRight
            else:
                self.animation = self.spFallLeft

        if self.shoot:
            self.dx = 0
            self.dy = 0
            if not self.attacking:
                self.frame = 0
                self.attacking = True
            if self.right:
                self.animation = self.spShootRight
                if self.frame == 18:
                    laser = Laser(self.rect.x + 32, self.rect.y, self.right)
                    self.arrowSprites.add(laser)
                    Boss.laserSound.play()
            else:
                self.animation = self.spShootLeft
                if self.frame == 18:
                    laser = Laser(self.rect.x -4, self.rect.y, self.right)
                    self.arrowSprites.add(laser)
                    Boss.laserSound.play()

        Enemy.update(self)

    def draw(self, screen):
        pygame.sprite.Sprite.draw(self, screen)
        hpBlit = self.font.render(self.hp, 1, const.RED)
        screen.blit(hpBlit, (self.rect.x, self.rect.y + 16))
