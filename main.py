import pygame
from functies import *
from wildFuncties import *
from menuFuncties import *
from outsideFuncties import *
from insideFuncties import *



pygame.init()
FPS = 60
screenRes = [1920, 1080]
screen = pygame.display.set_mode((screenRes[0], screenRes[1]))
clock = pygame.time.Clock()
dt = clock.tick(FPS)/1000


menu = house = True
paused = playing  = outside = wild = False
mapCalculated = armory = inwater = False
w_key = d_key = s_key = a_key = space_key = e_key = down_key = up_key = tab_key = escape_key = mb1 = False
playerPos = [250, 150]
playerSize = [75, 75]
cursorPos = []

speed = 400*dt
walls = [0,0,0,0]

waterX = waterY = treeX = treeY = lastLoc = invItems = []

coins = shop = playTextWidth = shopSel = wildEntrance = armoryEntrance = houseEntrance = 0
health = 100
mana = 50
balance = 99999

selected = 3
directionX = "north"
directionY = "west"

window1 = window2 = window3 = ""
e1posX = 1700
e1posY = 800
e1Health = 30




map = [
    "1 1 1 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 1 1 1 1 1 1",
    "1 1 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 1 1 1 1",
    "1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 1 1",
    "0 0 0 0 0 0 0 0 0 0 2 2 0 0 0 0 0 0 2 0 0 0 0 0 0 0 0 0 0 1 1 1",
    "0 0 0 0 0 0 0 0 0 0 2 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 1",
    "0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1",
    "1 0 0 0 0 0 0 0 0 0 0 0 0 1 1 1 1 1 1 1 0 0 0 0 0 0 0 0 0 0 0 0",
    "1 1 0 0 0 0 0 0 0 0 0 0 0 1 1 1 1 1 1 1 1 0 0 0 0 0 0 0 0 0 0 0",
    "1 1 1 0 0 0 0 0 0 0 0 0 0 0 0 1 1 1 1 1 1 1 0 0 0 0 0 0 0 0 0 0",
    "1 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 1 1 0 0 0 0 0 0 0 0 0 0",
    "1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 1 1 0 0 0 0 0 0 0 0 0 0",
    "0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 1 1 0 0 0 0 0 0 0 0 0 0",
    "0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0",
    "1 1 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0",
    "1 1 1 1 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0",
    "1 1 1 1 1 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0",
    "1 1 1 1 1 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0",
    "1 1 1 1 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0",
]


while menu:
    screen.fill("white")
    selected, playTextWidth, menu, playing = startMenu(screen, screenRes, selected, playTextWidth, menu, playing)
    pygame.display.flip()
    clock.tick(FPS) 







while playing:
    w_key, d_key, s_key, a_key, space_key, e_key, down_key, up_key, tab_key, escape_key, mb1 = eventUpdate(w_key, d_key, s_key, a_key, space_key, e_key, down_key, up_key, tab_key, escape_key, mb1)
    
    w_key, d_key, s_key, a_key = gameBorders(playerPos, walls, outside, speed, w_key, d_key, s_key, a_key)

    inwater, speed, playerPos = playerMovement(waterX, waterY, playerPos, w_key, d_key, s_key, a_key, inwater, dt, speed, paused, outside)

    directionX, directionY, cursorPos = playerLookDirection(playerPos, directionX, directionY)#DirectionX/Y doet niks nu. CursorPos kan je wel gebruiken
    
    
    
    
    
    
    
    if wild:
        screen.fill((2, 87, 24))#(0, 101, 168) Voor water kleur

        if not mapCalculated:
            map = newMap()
            waterX, waterY, treeX, treeY, mapCalculated = wildCalcMap(screen, map, mapCalculated)

        grass = wildDrawMap(screen, waterX, waterY, treeX, treeY)
        wildEntrance = wildDraw(screen, screenRes)
        #enemy1, e1posX, e1posY, e1Health, invItems = enemy(screen, posX, posY, outside, e1posX, e1posY, e1Health, paused, invItems, player, enemy1) ####enemy systeem wss opniew


    if outside and not wild:
        screen.fill((2, 87, 24))#(0, 101, 168) Voor water kleur

        if not mapCalculated:
            waterX, waterY, treeX, treeY, mapCalculated = outsideCalcMap(screen, map, mapCalculated)

        outsideDrawMap(screen, waterX, waterY, treeX, treeY)
        houseEntrance, armoryEntrance, wildEntrance = outsideDraw(screen, screenRes)
        

    elif not outside:
        if house:
            screen.fill("black")
            floor, walls, door = houseDraw(screen, screenRes)
        if armory:
            screen.fill("black")
            floor, walls, door, shop = armoryDraw(screen, screenRes)

    player, mana, shield, balance = playerDraw(screen, playerPos, playerSize, outside, space_key, health, mana, screenRes, paused, balance)


    house, armory, outside, wild, speed, mapCalculated, playerPos, playerSize = entranceCollissions(outside, house, armory, wild, playerPos, playerSize, player, screenRes, wildEntrance, houseEntrance, armoryEntrance, dt, speed, mapCalculated)
    speed, playerSize, playerPos, armory, house, outside, wild = insideCollissions(player, door, playerPos, playerSize, speed, dt, armory, outside, house, wild)
    e_key, window1, window2, window3 = armoryCollissions(playerPos, shop, screen, e_key, shopSel, screenRes, armory, window1, window2, window3, mb1)


    if tab_key:
        paused = True
        inventory(screen, screenRes, invItems)
    else:
        paused = False

    if escape_key:
        paused = True
        escape_key, playing, menu = pauseMenu(screen, screenRes, mb1, escape_key, playing, menu)
    else:
        paused = False

    
    
    pygame.display.flip()

    clock.tick(FPS) 

pygame.quit()