import pygame
import const
from player import Player
from level import *
import tutorial, level1, level2, bossLevel
import camera

#Setup
pygame.init()
screen = pygame.display.set_mode((const.SCR_WID, const.SCR_HEI))
pygame.display.set_caption("Bones of the Earth")
clock = pygame.time.Clock()
FPS = 60
pygame.mixer.music.load("data\\sounds\music.ogg")
pygame.mixer.music.play(-1, 0.0)
musicPlaying = True
current = 0
menuItems = [["Tutorial",const.RED], ["Level 1",const.WHITE], ["Level 2",const.WHITE], ["Boss",const.WHITE], ["Exit",const.WHITE]]
menuFont = pygame.font.Font("data\\fonts\LCD_Solid.ttf", 20)
titleFont = pygame.font.Font("data\\fonts\LCD_Solid.ttf", 50)
titleBlit = titleFont.render("BONES OF THE EARTH", 1, const.BROWN)
titWid, titHei = titleFont.size("BONES OF THE EARTH")
nameBlit = menuFont.render("Stephen Ogden 2017", 1, const.BROWN)
menuBack = camera.Background()
cursor = 0
totalRep = True
menuRep = True

#Menu Loop
while totalRep:
    while menuRep:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                menuRep = False
                repeat = False
                totalRep = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_m:
                    if musicPlaying:
                        pygame.mixer.music.stop()
                    else:
                        pygame.mixer.music.play(-1, 0.0)
                    musicPlaying = not musicPlaying
                if event.key == pygame.K_DOWN:
                    cursor += 1
                    if cursor >= len(menuItems):
                        cursor = 0
                if event.key == pygame.K_UP:
                    cursor -= 1
                    if cursor < 0:
                        cursor = len(menuItems)-1
                if event.key == pygame.K_RETURN:
                    if cursor == len(menuItems)-1:
                        repeat = False
                        totalRep = False
                        current = 0
                    else:
                        repeat = True
                        current = cursor
                    menuRep = False

        menuBack.shift(-1)
        menuBack.update(screen)
        screen.blit(titleBlit, (const.SCR_WID/2 - titWid/2, 100))
        screen.blit(nameBlit, (4, const.SCR_HEI-25))
        for item in menuItems:
            item[1] = const.WHITE
        menuItems[cursor][1] = const.RED
        placement = 200
        for item in menuItems:
            itemBlit = menuFont.render(item[0], 1, item[1])
            wid, hei = menuFont.size(item[0])
            screen.blit(itemBlit, (const.SCR_WID/2 - wid/2, placement))
            placement += 75
        pygame.display.update()

    #Game setup
    timer = 5400
    menuRep = True
    player = Player()
    player.rect.x = 0
    player.rect.y = 504

    levels = [Tutorial(tutorial.platLoc, tutorial.skelLoc, tutorial.zombLoc, player, tutorial.endLoc),
              Level(level1.platLoc, level1.skelLoc, level1.zombLoc, player, level1.endLoc),
              Level(level2.platLoc, level2.skelLoc, level2.zombLoc, player, level2.endLoc),
              BossLevel(bossLevel.platLoc, bossLevel.skelLoc, bossLevel.zombLoc, player, bossLevel.endLoc, bossLevel.bossLoc)]
    player.level = levels[current].platformSprites

    #Game Loop
    while repeat:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                repeat = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    repeat = False
                if event.key == pygame.K_m:
                    if musicPlaying:
                        pygame.mixer.music.stop()
                    else:
                        pygame.mixer.music.play(-1, 0.0)
                    musicPlaying = not musicPlaying

        #update the screen
        levels[current].update()
        levels[current].draw(screen)
        player.hud(screen, int(timer/6))

        #check if the player has reached the end of the stage
        if player.rect.right + levels[current].camera.displacement > levels[current].endLoc:
            current += 1
            if current < len(levels):
                player.level = levels[current].platformSprites
            player.rect.x = 0
            player.rect.y = 504
            #reset after the tutorial
            if current == 1:
                player.ammo = 10
                player.hp = 100
                player.killScore -= int(timer/6)
            player.killScore += int(timer/6)
            timer = 5400
        #check for game over
        if player.hp <= 0 or current >= len(levels) or timer <= 0:
            player.gameOver(screen, int(timer/6))
            repeat = False
        timer -= 1
        pygame.display.update()
        clock.tick(FPS)

pygame.quit()
