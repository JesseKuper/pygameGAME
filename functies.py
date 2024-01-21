import pygame

## niet op de goede plek maar met import komt een error dus voor nu hier
def shopMenu(screen, screenRes, shopSel, window1, window2, window3, mb1):
    mX, mY =pygame.mouse.get_pos()
    
    cursor = pygame.draw.rect(screen, "black", pygame.Rect(mX, mY , 1, 1))
    if window1 and window2 and window3:
        if cursor.colliderect(window1):
            shopSel = 0
        if cursor.colliderect(window2):
            shopSel = 1
        if cursor.colliderect(window3):
            shopSel = 2
    if mb1:
        if shopSel == 0:
            print("BUY 1")
        if shopSel == 1:
            print("BUY 2")
        if shopSel == 2:
            print("BUY 3")
    cost = 0
    backgroundBorder = pygame.draw.rect(screen, (219, 172, 52), pygame.Rect(screenRes[0] - (screenRes[0] // 2), (screenRes[1] // 10) - 20, screenRes[0] / 3 + 150, screenRes[1] - (screenRes[1]//5) + 20))
    background = pygame.draw.rect(screen, (153, 153, 153), pygame.Rect(screenRes[0] - (screenRes[0] // 2)+ 20, (screenRes[1] // 10), screenRes[0] / 3 + 110, screenRes[1] - (screenRes[1]//5) -20))
    c1=c2=c3= (100, 100, 100)
    if shopSel == 0:
        cost = 50
        c1 = (150, 150, 150)
        wbY = (screenRes[1] // 10) + 10
    elif shopSel == 1:
        cost = 100
        c2 = (150, 150, 150)
        wbY = (screenRes[1] // 10) + 245
    elif shopSel == 2:  
        cost = 200
        c3 = (150, 150, 150)
        wbY = (screenRes[1] // 10) + 480
    windowBackground = pygame.draw.rect(screen, (219, 172, 52), pygame.Rect(screenRes[0] - (screenRes[0] // 2)+ 30, wbY, screenRes[0] / 3 + 90, (screenRes[1]//5) + 20 ))

    window1 = pygame.draw.rect(screen, c1, pygame.Rect(screenRes[0] - (screenRes[0] // 2)+ 40, (screenRes[1] // 10)+ 20, screenRes[0] / 3 + 70, screenRes[1]//5))
    image1Load = pygame.image.load("images/example.png") ### maak images 285 bij 170
    image1 = pygame.draw.rect(screen, "white", pygame.Rect(1400, 150, 285, 170))
    screen.blit(image1Load, image1)
    font = pygame.font.SysFont(None, 30)
    pName = font.render("PRODDUCT NAME", True, "white")
    screen.blit(pName, (screenRes[0] - (screenRes[0] // 2)+ 50, (screenRes[1] // 10)+ 40))

    font = pygame.font.SysFont(None, 25)
    pStat1 = font.render("- STAT NUMBER 1", True, "white")
    screen.blit(pStat1, (screenRes[0] - (screenRes[0] // 2)+ 70, (screenRes[1] // 10)+ 90))
    font = pygame.font.SysFont(None, 25)
    pStat2 = font.render("- STAT NUMBER 2", True, "white")
    screen.blit(pStat2, (screenRes[0] - (screenRes[0] // 2)+ 70, (screenRes[1] // 10)+ 120))
    font = pygame.font.SysFont(None, 25)
    pStat3 = font.render("- STAT NUMBER 3", True, "white")
    screen.blit(pStat3, (screenRes[0] - (screenRes[0] // 2)+ 70, (screenRes[1] // 10)+ 150))
    font = pygame.font.SysFont(None, 25)
    pStat4 = font.render("- STAT NUMBER 4", True, "white")
    screen.blit(pStat4, (screenRes[0] - (screenRes[0] // 2)+ 70, (screenRes[1] // 10)+ 180))


    window2 = pygame.draw.rect(screen, c2, pygame.Rect(screenRes[0] - (screenRes[0] // 2)+ 40, (screenRes[1] // 10)+(screenRes[1]//5 ) + 40, screenRes[0] / 3 + 70, (screenRes[1]//5)))
    image2Load = pygame.image.load("images/example.png") ### maak images 285 bij 170
    image2 = pygame.draw.rect(screen, "white", pygame.Rect(1400, 170+(screenRes[1]//5 ), 285, (screenRes[1]//5 ) - 40))
    screen.blit(image2Load, image2)
    font = pygame.font.SysFont(None, 30)
    p2Name = font.render("PRODDUCT NAME", True, "white")
    screen.blit(p2Name, (screenRes[0] - (screenRes[0] // 2)+ 50, (screenRes[1] // 10)+ 60+(screenRes[1]//5 )))

    font = pygame.font.SysFont(None, 25)
    p2Stat1 = font.render("- STAT NUMBER 1", True, "white")
    screen.blit(p2Stat1, (screenRes[0] - (screenRes[0] // 2)+ 70, (screenRes[1] // 10)+ 110+(screenRes[1]//5 )))
    font = pygame.font.SysFont(None, 25)
    p2Stat2 = font.render("- STAT NUMBER 2", True, "white")
    screen.blit(p2Stat2, (screenRes[0] - (screenRes[0] // 2)+ 70, (screenRes[1] // 10)+ 140+(screenRes[1]//5 )))
    font = pygame.font.SysFont(None, 25)
    p2Stat3 = font.render("- STAT NUMBER 3", True, "white")
    screen.blit(p2Stat3, (screenRes[0] - (screenRes[0] // 2)+ 70, (screenRes[1] // 10)+ 170+(screenRes[1]//5 )))
    font = pygame.font.SysFont(None, 25)
    p2Stat4 = font.render("- STAT NUMBER 4", True, "white")
    screen.blit(p2Stat4, (screenRes[0] - (screenRes[0] // 2)+ 70, (screenRes[1] // 10)+ 200+(screenRes[1]//5 )))



    window3 = pygame.draw.rect(screen, c3, pygame.Rect(screenRes[0] - (screenRes[0] // 2)+ 40, (screenRes[1] // 10)+(screenRes[1]//5) + 275, screenRes[0] / 3 + 70, (screenRes[1]//5)))
    image3Load = pygame.image.load("images/example.png") ### maak images 285 bij 170
    image3 = pygame.draw.rect(screen, "white", pygame.Rect(1400, 405+(screenRes[1]//5 ), 285, (screenRes[1]//5 ) - 40))
    screen.blit(image3Load, image3)
    font = pygame.font.SysFont(None, 30)
    p3Name = font.render("PRODDUCT NAME", True, "white")
    screen.blit(p3Name, (screenRes[0] - (screenRes[0] // 2)+ 50, (screenRes[1] // 10)+ 295+(screenRes[1]//5 )))

    font = pygame.font.SysFont(None, 25)
    p3Stat1 = font.render("- STAT NUMBER 1", True, "white")
    screen.blit(p3Stat1, (screenRes[0] - (screenRes[0] // 2)+ 70, (screenRes[1] // 10)+ 345+(screenRes[1]//5 )))
    font = pygame.font.SysFont(None, 25)
    p3Stat2 = font.render("- STAT NUMBER 2", True, "white")
    screen.blit(p3Stat2, (screenRes[0] - (screenRes[0] // 2)+ 70, (screenRes[1] // 10)+ 375+(screenRes[1]//5 )))
    font = pygame.font.SysFont(None, 25)
    p3Stat3 = font.render("- STAT NUMBER 3", True, "white")
    screen.blit(p3Stat3, (screenRes[0] - (screenRes[0] // 2)+ 70, (screenRes[1] // 10)+ 405+(screenRes[1]//5 )))
    font = pygame.font.SysFont(None, 25)
    p3Stat4 = font.render("- STAT NUMBER 4", True, "white")
    screen.blit(p3Stat4, (screenRes[0] - (screenRes[0] // 2)+ 70, (screenRes[1] // 10)+ 435+(screenRes[1]//5 )))

    font = pygame.font.SysFont(None, 40)
    nav1 = font.render("arrow Up / down", True, "white")
    screen.blit(nav1, (screenRes[0] - (screenRes[0] // 2)+ 50, (screenRes[1] // 10)+ 500+(screenRes[1]//5 )))

    font = pygame.font.SysFont(None, 40)
    nav1 = font.render("Enter to selects", True, "white")
    screen.blit(nav1, (screenRes[0] - (screenRes[0] // 2)+ 50, (screenRes[1] // 10)+ 550+(screenRes[1]//5 )))
    
    font = pygame.font.SysFont(None, 80)
    nav1 = font.render(f"cost: {cost}", True, "white")
    screen.blit(nav1, (screenRes[0] - (screenRes[0] // 2)+ 520, (screenRes[1] // 10)+ 525+(screenRes[1]//5 )))

    return window1, window2, window3

#HUD FUNCTIONS



def eventUpdate(w_key, d_key, s_key, a_key, space_key, e_key, down_key, up_key, tab_key, escape_key, mb1):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            playing = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                w_key = True
            if event.key == pygame.K_d:
                d_key = True
            if event.key == pygame.K_s:
                s_key = True
            if event.key == pygame.K_a:
                a_key = True
            if event.key == pygame.K_SPACE:
                space_key = True
            if event.key == pygame.K_e:
                e_key = True
            if event.key == pygame.K_DOWN:
                down_key = True
            if event.key == pygame.K_UP:
                up_key = True
            if event.key == pygame.K_TAB:
                tab_key = True
            if event.key == pygame.K_ESCAPE:
                escape_key = True

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                w_key = False
            if event.key == pygame.K_d:
                d_key = False
            if event.key == pygame.K_s:
                s_key = False
            if event.key == pygame.K_a:
                a_key = False
            if event.key == pygame.K_SPACE:
                space_key = False
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            mb1 = True
        
        if event.type == pygame.MOUSEBUTTONUP:
            mb1 = False
    return w_key, d_key, s_key, a_key, space_key, e_key, down_key, up_key, tab_key, escape_key, mb1


def gameBorders(playerPos, walls, outside, speed, w_key, d_key, s_key, a_key):
    if not outside:
        if (playerPos[1] - walls[0]) < 25:
            w_key = False
        if (playerPos[0] - walls[1]) > - 75:
            d_key = False
        if (playerPos[1] - walls[2]) > - 75:
            s_key = False
        if (playerPos[0] - walls[3]) < 25:
            a_key = False

    if outside: 
        if playerPos[0] < 0: 
            playerPos[0] += speed*1.2
        if playerPos[1] < 0:
            playerPos[1] += speed*1.2
        if playerPos[1] > 1055:
            playerPos[1] -= speed*1.2
        if playerPos[0] > 1895:
            playerPos[0] -= speed*1.2

    return w_key, d_key, s_key, a_key



def playerMovement(listX, listY, playerPos, w_key, d_key, s_key, a_key, inwater, dt, speed, paused, outside):
    if outside:
        postel = 0
        fpstel = 0     
        if len(listX) > 0:
            while postel <= len(listX): 
                try: 
                    if playerPos[0] >= listX[postel] and playerPos[0] <= listX[postel] + 60 and playerPos[1] >= listY[postel] and playerPos[1] <= listY[postel] + 60:
                        inwater = True
                except:
                    pass #fix dit
                postel += 1
            if not inwater:
                speed = 250*dt
            if inwater:
                speed = 70*dt
                inwater = False

    
    #elifs if no diagonal !!
    if not paused:
        if w_key:
            playerPos[1] -= speed
        if s_key:
            playerPos[1] += speed
        if d_key:
            playerPos[0] += speed
        if a_key:
            playerPos[0] -= speed
    
    return inwater, speed, playerPos


def playerLookDirection(playerPos, directionX, directionY):
    mX, mY =pygame.mouse.get_pos()
    cursorPos = [mX, mY]
    if mY - playerPos[1] > 0:
        directionY = "south"
    else:
        directionY = "north"

    if mX - playerPos[0] > 0:
        directionX = "east"
    else:
        directionX = "west"
    return directionX, directionY, cursorPos


def playerDraw(screen, playerPos, playerSize, outside, attack, health, mana, screenRes, paused, balance): 
    shield = ""
    if outside and attack and not paused and mana > 0: 
        shield = pygame.draw.rect(screen, (161, 5, 33), pygame.Rect(playerPos[0] -50, playerPos[1] -  50, 125, 125 ))
        borderN = pygame.draw.rect(screen, (112, 0, 20), pygame.Rect(playerPos[0] -50, playerPos[1] -  50, 125, 5 ))
        borderS = pygame.draw.rect(screen, (112, 0, 20), pygame.Rect(playerPos[0] -50, playerPos[1] +  70, 125, 5 ))
        borderW = pygame.draw.rect(screen, (112, 0, 20), pygame.Rect(playerPos[0] - 50, playerPos[1] - 50, 5, 125 ))
        borderE = pygame.draw.rect(screen, (112, 0, 20), pygame.Rect(playerPos[0] + 70, playerPos[1] - 50, 5, 125 )) 
        mana -= 0.3
    else:
        if mana < 50 and not paused:
            mana += 0.01
    
    player = pygame.draw.rect(screen, "white", pygame.Rect(playerPos[0], playerPos[1], playerSize[0], playerSize[1]))
    playerColor = pygame.draw.rect(screen, (47, 60, 77), pygame.Rect(playerPos[0]+ 5, playerPos[1]+ 5, playerSize[0]-10, playerSize[1]-10))

    healthEmpty = pygame.draw.rect(screen, "white", pygame.Rect(screenRes[0]//2 - 255, screenRes[1] - 85, 510, 30))
    healthMeter = pygame.draw.rect(screen, "red", pygame.Rect(screenRes[0]//2 - 250, screenRes[1] - 80, health*5, 20))

    manaEmpty = pygame.draw.rect(screen, "white", pygame.Rect(screenRes[0]//2 - 255, screenRes[1] - 45, 510, 30))
    manaMeter = pygame.draw.rect(screen, "blue", pygame.Rect(screenRes[0]//2 - 250, screenRes[1] - 40, mana*5, 20))

    font = pygame.font.SysFont(None, 20)
    nav1 = font.render(f"Balance: {balance}", True, "Red")
    screen.blit(nav1, (20, 20))
    return player, mana, shield, balance



def entranceCollissions(outside, house, armory, wild, playerPos, playerSize, player, screenRes, wildEntrance, houseEntrance, armoryEntrance, dt, speed, mapCalculated):
    if outside:
        if player.colliderect(wildEntrance):
            if wild:
                house = armory = mapCalculated = wild = False
                outside = True
                playerPos[0] = 100
                playerPos[1] = screenRes[1]/2
            elif not wild:
                house = armory = mapCalculated = False
                outside = wild = True
                playerPos[0] = 100
                playerPos[1] = screenRes[1]/2
        if player.colliderect(houseEntrance) and not wild:
            house = True
            armory = outside = wild = False
            speed = 400*dt
            playerSize[0] = 75
            playerSize[1] = 75
            playerPos[0] = 1520
            playerPos[1] = 840
        elif player.colliderect(armoryEntrance) and not wild:
            house = outside = wild = False
            armory = True
            speed = 400*dt
            playerSize[0] = 75
            playerSize[1] = 75
            playerPos[0] = 680
            playerPos[1] = 770
    
    return house, armory, outside, wild, speed, mapCalculated, playerPos, playerSize




def insideCollissions(player, door, playerPos, playerSize, speed, dt, armory, outside, house, wild):
    if not outside:
        if player.colliderect(door):
            if armory:
                playerPos[0] = 560
                playerPos[1] = 990
            elif house:
                playerPos[0] = 350
                playerPos[1] = 330
            armory = house = wild = False
            outside = True
            speed = 250*dt
            playerSize[0] = 25
            playerSize[1] = 25
    return speed, playerSize, playerPos, armory, house, outside, wild
    


    
def armoryCollissions(playerPos, shop, screen, e_key, shopSel, screenRes, armory, window1, window2, window3, mb1):
    if armory:
        if playerPos[1] - shop < 200:
            if not e_key:
                font = pygame.font.SysFont(None, 30)
                img = font.render("SHOP (E)", True, "white")
                screen.blit(img, (playerPos[0] + 80, playerPos[1] - 20))
            if e_key:
                window1, window2, window3 = shopMenu(screen, screenRes, shopSel, window1, window2, window3, mb1)
        else:
            e_key = False

    return e_key, window1, window2, window3
    


def inventory(screen, screenRes, invItems): 
    invBorder = pygame.draw.rect(screen, "black", pygame.Rect(400 - 10,100 - 10, screenRes[0] - 800 + 20, screenRes[1] - 200 + 20 ))
    invBackground = pygame.draw.rect(screen, "grey", pygame.Rect(400,100, screenRes[0] - 800, screenRes[1] - 200 ))
    textX = 400
    textY = 100
    for i in invItems:
        font = pygame.font.SysFont(None, 50)
        img = font.render(f"{i}", True, "white")
        screen.blit(img, (textX, textY))
        textX += 224
        textY += 176
    
    invgrid = pygame.draw.rect(screen, "black", pygame.Rect(400,286, screenRes[0] - 800, 10 ))
    invgrid = pygame.draw.rect(screen, "black", pygame.Rect(400,463, screenRes[0] - 800, 10 ))
    invgrid = pygame.draw.rect(screen, "black", pygame.Rect(400,639, screenRes[0] - 800, 10 ))
    invgrid = pygame.draw.rect(screen, "black", pygame.Rect(400,815, screenRes[0] - 800, 10 ))
    invgrid = pygame.draw.rect(screen, "black", pygame.Rect(400,991, screenRes[0] - 800, 10 ))
    

    invgrid = pygame.draw.rect(screen, "black", pygame.Rect(624,100, 10, screenRes[1] - 200 ))
    invgrid = pygame.draw.rect(screen, "black", pygame.Rect(848,100, 10, screenRes[1] - 200 ))
    invgrid = pygame.draw.rect(screen, "black", pygame.Rect(1072,100, 10, screenRes[1] - 200 ))
    invgrid = pygame.draw.rect(screen, "black", pygame.Rect(1296,100, 10, screenRes[1] - 200 ))
    invgrid = pygame.draw.rect(screen, "black", pygame.Rect(1520,100, 10, screenRes[1] - 200 ))


def pauseMenu(screen, screenRes, mb1, escape_key, playing, menu):
    mX, mY =pygame.mouse.get_pos()
    

    font = pygame.font.SysFont(None, 70)
    img = font.render("Resume", True, "white")
    screen.blit(img, (screenRes[0]/2, screenRes[1]/2 - 200))

    font = pygame.font.SysFont(None, 70)
    img = font.render("back to Menu", True, "white")
    screen.blit(img, (screenRes[0]/2, screenRes[1]/2))
    tXResume, tYResume = font.size("Resume")
    tXMenu, tYMenu = font.size("back to menu")

    if mX > (screenRes[0]/2) and mX < ((screenRes[0]/2) + tXResume) and mY > (screenRes[1]/2 - 200) and mY < ((screenRes[1]/2 - 200) + tYResume) and mb1:
        escape_key = False
    if mX > (screenRes[0]/2) and mX < ((screenRes[0]/2) + tXMenu) and mY > (screenRes[1]/2) and mY < ((screenRes[1]/2) + tYMenu) and mb1:
        escape_key = False
        playing = False
        startMenu = True
    return  escape_key, playing, menu