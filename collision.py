import pygame
import const

def checkDamage(playerSprite, enemySprites, laserSprites, arrowSprites, swordBoxSprites):
    #check arrows hitting the player
    playerDict = pygame.sprite.groupcollide(playerSprite, arrowSprites, False, True)
    for playerKey in playerDict:
        for arrow in playerDict[playerKey]:
            #damage player for every arrow hitting it
            if arrow.right:
                playerKey.damage(10, True)
            else:
                playerKey.damage(10, False)
    #check lasers hitting enemies
    enemyDict = pygame.sprite.groupcollide(enemySprites, laserSprites, False, True)
    for enemyKey in enemyDict:
        for laser in enemyDict[enemyKey]:
            #damage each enemy for every laser hitting it
            if laser.right:
                enemyKey.damage(25, True)
            else:
                enemyKey.damage(25, False)
        playerSprite.sprites()[0].killScore += 40
    #check sword hitbox hitting enemies
    swordDict = pygame.sprite.groupcollide(swordBoxSprites, enemySprites, False, False)
    for swordKey in swordDict:
        for enemy in swordDict[swordKey]:
            #damage enemy hit by sword swing
            if swordKey.rect.x < enemy.rect.x:
                enemy.damage(50, True)
            else:
                enemy.damage(50, False)
        playerSprite.sprites()[0].killScore += 100
    #check players and enemies colliding
    playerDict = pygame.sprite.groupcollide(playerSprite, enemySprites, False, False)
    for playerKey in playerDict:
        for enemy in playerDict[playerKey]:
            #Damages the player for every enemy touching it
            if not playerKey.hitBox:
                if playerKey.rect.x < enemy.rect.x:
                    playerKey.damage(10, False)
                else:
                    playerKey.damage(10, True)


#kills projectiles that hit walls
def projectileWallCol(laserSprites, arrowSprites, platformSprites):
    pygame.sprite.groupcollide(laserSprites, platformSprites, True, False)
    pygame.sprite.groupcollide(arrowSprites, platformSprites, True, False)
