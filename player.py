import pygame
pygame.init()
import const
from spritesheet import SpriteSheet
from projectiles import *

class Player(pygame.sprite.Sprite):
    """Sprite controller for player"""
    #keybindings
    cont = {"left":pygame.K_a,
            "right":pygame.K_d,
            "jump":pygame.K_w,
            "melee":pygame.K_j,
            "shoot":pygame.K_k}
    swordSound = pygame.mixer.Sound("data\\sounds\swordSwing.wav")
    laserSound = pygame.mixer.Sound("data\\sounds\laserSound.wav")
    
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.font = pygame.font.Font("data\\fonts\LCD_Solid.ttf", 16)
        self.laserSprites = pygame.sprite.RenderPlain()
        self.swordBoxSprites = pygame.sprite.RenderPlain()
        self.dx = 0
        self.dy = 0
        self.right = True
        self.idle = True
        self.moving = False
        self.falling = False
        self.melee = False
        self.shoot = False
        self.attacking = False
        self.hitBox = False
        self.frame = 0
        self.hp = 100
        self.ammo = 10
        self.killScore = 0
        self.level = None

        #sets up sprite collection lists
        self.animation = []
        self.spIdleLeft = []
        self.spIdleRight = []
        self.spMoveLeft = []
        self.spMoveRight = []
        self.spFallLeft = []
        self.spFallRight = []
        self.spMeleeLeft = []
        self.spMeleeRight = []
        self.spShootLeft = []
        self.spShootRight = []

        #define locations to send to spritesheet for sprites
        self.spIdleLeftLoc = [{'x':1, 'y':2, 'wid':47, 'hei':55, 'flip':True},
                              {'x':49, 'y':3, 'wid':47, 'hei':55, 'flip':True},
                              {'x':97, 'y':3, 'wid':48, 'hei':55, 'flip':True},
                              {'x':147, 'y':3, 'wid':48, 'hei':55, 'flip':True},
                              {'x':197, 'y':3, 'wid':48, 'hei':55, 'flip':True},
                              {'x':246, 'y':3, 'wid':47, 'hei':55, 'flip':True},
                              {'x':294, 'y':3, 'wid':45, 'hei':55, 'flip':True},
                              {'x':340, 'y':3, 'wid':44, 'hei':55, 'flip':True},
                              {'x':384, 'y':3, 'wid':42, 'hei':55, 'flip':True},
                              {'x':427, 'y':3, 'wid':42, 'hei':55, 'flip':True},
                              {'x':470, 'y':3, 'wid':44, 'hei':55, 'flip':True}]

        self.spIdleRightLoc = [{'x':1, 'y':2, 'wid':47, 'hei':55, 'flip':False},
                               {'x':49, 'y':3, 'wid':47, 'hei':55, 'flip':False},
                               {'x':97, 'y':3, 'wid':48, 'hei':55, 'flip':False},
                               {'x':147, 'y':3, 'wid':48, 'hei':55, 'flip':False},
                               {'x':197, 'y':3, 'wid':48, 'hei':55, 'flip':False},
                               {'x':246, 'y':3, 'wid':47, 'hei':55, 'flip':False},
                               {'x':294, 'y':3, 'wid':45, 'hei':55, 'flip':False},
                               {'x':340, 'y':3, 'wid':44, 'hei':55, 'flip':False},
                               {'x':384, 'y':3, 'wid':42, 'hei':55, 'flip':False},
                               {'x':427, 'y':3, 'wid':42, 'hei':55, 'flip':False},
                               {'x':470, 'y':3, 'wid':44, 'hei':55, 'flip':False}]

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

        self.spMeleeLeftLoc = [{'x':3, 'y':231, 'wid':47, 'hei':62, 'flip':True},
                               {'x':53, 'y':231, 'wid':48, 'hei':62, 'flip':True},
                               {'x':103, 'y':231, 'wid':45, 'hei':62, 'flip':True},
                               {'x':150, 'y':231, 'wid':39, 'hei':62, 'flip':True},
                               {'x':195, 'y':231, 'wid':33, 'hei':62, 'flip':True},
                               {'x':233, 'y':231, 'wid':40, 'hei':62, 'flip':True},
                               {'x':275, 'y':231, 'wid':46, 'hei':62, 'flip':True},
                               {'x':322, 'y':231, 'wid':70, 'hei':62, 'flip':True},
                               {'x':395, 'y':231, 'wid':69, 'hei':62, 'flip':True},
                               {'x':465, 'y':231, 'wid':47, 'hei':62, 'flip':True},
                               {'x':518, 'y':231, 'wid':39, 'hei':62, 'flip':True},
                               {'x':559, 'y':231, 'wid':50, 'hei':62, 'flip':True},
                               {'x':612, 'y':231, 'wid':47, 'hei':62, 'flip':True}]

        self.spMeleeRightLoc = [{'x':3, 'y':231, 'wid':47, 'hei':62, 'flip':False},
                                {'x':53, 'y':231, 'wid':48, 'hei':62, 'flip':False},
                                {'x':103, 'y':231, 'wid':45, 'hei':62, 'flip':False},
                                {'x':150, 'y':231, 'wid':39, 'hei':62, 'flip':False},
                                {'x':195, 'y':231, 'wid':33, 'hei':62, 'flip':False},
                                {'x':233, 'y':231, 'wid':40, 'hei':62, 'flip':False},
                                {'x':275, 'y':231, 'wid':46, 'hei':62, 'flip':False},
                                {'x':322, 'y':231, 'wid':70, 'hei':62, 'flip':False},
                                {'x':395, 'y':231, 'wid':69, 'hei':62, 'flip':False},
                                {'x':465, 'y':231, 'wid':47, 'hei':62, 'flip':False},
                                {'x':518, 'y':231, 'wid':39, 'hei':62, 'flip':False},
                                {'x':559, 'y':231, 'wid':50, 'hei':62, 'flip':False},
                                {'x':612, 'y':231, 'wid':47, 'hei':62, 'flip':False}]

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

        #sends locations to spritesheet to grab images
        sheet = SpriteSheet('data\sprites\player1.bmp')
        self.spIdleLeft = sheet.getSet(self.spIdleLeftLoc)
        self.spIdleRight = sheet.getSet(self.spIdleRightLoc)
        self.spMoveLeft = sheet.getSet(self.spMoveLeftLoc)
        self.spMoveRight = sheet.getSet(self.spMoveRightLoc)
        self.spFallLeft = sheet.getSet(self.spFallLeftLoc)
        self.spFallRight = sheet.getSet(self.spFallRightLoc)
        self.spMeleeLeft = sheet.getSet(self.spMeleeLeftLoc)
        self.spMeleeRight = sheet.getSet(self.spMeleeRightLoc)
        self.spShootLeft = sheet.getSet(self.spShootLeftLoc)
        self.spShootRight = sheet.getSet(self.spShootRightLoc)

        #sets initial image
        self.image = self.spIdleRight[0]
        self.rect = self.image.get_rect()
        
    def update(self):
        #if moving, use moving animation
        if self.moving:
            if self.right:
                self.animation = self.spMoveRight
                #self.frame = 0
                self.dx = 5
            else:
                self.animation = self.spMoveLeft
                #self.frame = 0
                self.dx = -5

        #if idle, use idle animation
        if not self.moving:
            if self.right:
                self.animation = self.spIdleRight
            else:
                self.animation = self.spIdleLeft
            self.dx = 0

        #if falling, use falling animation
        if self.falling:
            if self.right:
                self.animation = self.spFallRight
            else:
                self.animation = self.spFallLeft

        #if melee attacking, use melee animation
        if self.melee:
            self.dx = 0
            self.dy = 0
            if not self.attacking:
                self.frame = 0
                self.attacking = True
            if self.right:
                self.animation = self.spMeleeRight
            else:
                self.animation = self.spMeleeLeft
            if self.frame >= 18 and self.frame <= 27:
                self.hitBox = True
            else:
                self.hitBox = False

        #if shooting, use shoot animation
        if self.shoot:
            self.dx = 0
            self.dy = 0
            if not self.attacking:
                self.frame = 0
                self.attacking = True
            if self.right:
                self.animation = self.spShootRight
                if self.frame == 24:
                    laser = Laser(self.rect.x + 32, self.rect.y, self.right)
                    self.laserSprites.add(laser)
            else:
                self.animation = self.spShootLeft
                if self.frame == 24:
                    laser = Laser(self.rect.x -4, self.rect.y, self.right)
                    self.laserSprites.add(laser)

        #updates frame sprite is on
        if self.frame >= len(self.animation)*3:
            self.frame = 0
            if self.attacking:
                self.melee = False
                self.attacking = False
                self.shoot = False
        self.image = self.animation[self.frame // 3]
        self.rect.width = self.image.get_rect().width
        if self.melee and self.frame == 18:
            swordBox = SwordBox(self)
            self.swordBoxSprites.add(swordBox)
        self.frame += 1


        #check for keyboard input, then move player
        self.controls()
        self.move()
        if not self.onGround():
            self.falling = True
            self.dy += 0.5
        else:
            self.falling = False
            self.dy = 0
        if self.rect.top > const.SCR_HEI:
            self.hp = 0


    def controls(self):
        keyPress = pygame.key.get_pressed() #takes all keyboard input into a dict
        #checks for movement, or idle if not moving
        if keyPress[self.cont["left"]] and not self.attacking:
            self.right = False
            self.moving = True
        if keyPress[self.cont["right"]]and not self.attacking:
            self.right = True
            self.moving = True
        if (keyPress[self.cont["right"]] and keyPress[self.cont["left"]]) or (not keyPress[self.cont["right"]] and not keyPress[self.cont["left"]]):
            self.moving = False

        #checks for jumping if player is on the ground and not attacking
        if keyPress[self.cont["jump"]] and self.onGround() and not self.attacking:
            self.falling = True
            self.dy = -10

        #checks for melee if player is on the ground and not attacking
        if keyPress[self.cont["melee"]] and self.onGround() and not self.attacking:
            self.melee = True
            Player.swordSound.play()

        #checks for shooting if player is on the ground and not attacking
        if keyPress[self.cont["shoot"]] and self.onGround() and not self.attacking and self.ammo > 0:
            self.ammo -= 1
            self.shoot = True
            Player.laserSound.play()

    def onGround(self):
        #checks if player is on a platform
        self.rect.y += 1
        abovePlat = pygame.sprite.spritecollide(self, self.level, False)
        self.rect.y -= 1
        if abovePlat:
            return True
        return False

    def move(self):
        #moves player along x axis, then checks for collision with platforms and moves player back if colliding
        temp = self.rect.x
        self.rect.x += self.dx
        plats = pygame.sprite.spritecollide(self, self.level, False)
        if plats:
            if temp < plats[0].rect.x:
                self.rect.right = plats[0].rect.left
            else:
                self.rect.left = plats[0].rect.right

        #same but for y
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
        #reduces hp and knocks back player to avoid more damage
        if not self.hitBox:
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
            

    def hud(self, screen, time):
        #displays health, ammo, score, and time at top of screen
        healthBlit = self.font.render("Health: " + str(self.hp), 1, const.RED)
        screen.blit(healthBlit, (4, 4))
        ammoBlit = self.font.render("Ammo: " + str(self.ammo), 1, const.GREEN)
        screen.blit(ammoBlit, (200, 4))
        scoreBlit = self.font.render("Score: " + str(self.killScore), 1, const.WHITE)
        screen.blit(scoreBlit, (400, 4))
        timeBlit = self.font.render("Time: " + str(time/10), 1, const.RED)
        screen.blit(timeBlit, (600, 4))

    def gameOver(self, screen, time):
        #game over screen loop, stays in loop until esc or quit, then returns to menu
        repeat = True
        while repeat:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    repeat = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        repeat = False
            font = pygame.font.Font("data\\fonts\LCD_Solid.ttf", 32)
            if self.hp <= 0:
                gameOverBlit = font.render("YOU DIED", 1, const.RED)
            else:
                gameOverBlit = font.render("GAME OVER", 1, const.GREEN)
            screen.fill(const.BLACK)
            wid, hei = font.size("GAME OVER")
            screen.blit(gameOverBlit, (const.SCR_WID/2 - wid/2, const.SCR_HEI/2 - hei/2))
            scoreBlit = self.font.render("Score: " + str(self.killScore + time), 1, const.WHITE)
            wid, hei = self.font.size("Score: " + str(self.killScore + time))
            screen.blit(scoreBlit, (const.SCR_WID/2 - wid/2, const.SCR_HEI/2 + 50))
            escBlit = self.font.render("Press Escape to return to the menu", 1, const.WHITE)
            wid, hei = self.font.size("Press Escape to return to the menu")
            screen.blit(escBlit, (const.SCR_WID/2 - wid/2, const.SCR_HEI/2 + 100))
            pygame.display.update()
