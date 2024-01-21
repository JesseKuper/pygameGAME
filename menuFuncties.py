import pygame
def startMenu(screen, screenRes, selected, playTextWidth, menu, playing):
    
    mx, my=pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if selected == 0:
                playing = True
                menu = False
            elif selected == 1:
                exit()
    
    playColor = exitColor = "black"

    startPlayX = startExitX = 50
    startPlayXcol = startExitXcol = 50
    startPlayY = screenRes[0]/4 - 250
    startExitY = startPlayY + 200
    textSize = 250
    
    font = pygame.font.SysFont(None, textSize)
    playTextWidth, playTextHeight = font.size("PLAY")
    
    if selected == 0:
        playColor = "grey"
        startPlayX += 100

    elif selected == 1:
        exitColor = "grey"
        startExitX += 100


    font = pygame.font.SysFont(None, textSize)
    img = font.render("PLAY", True, playColor)
    screen.blit(img, (startPlayX, startPlayY))

    font = pygame.font.SysFont(None, textSize)
    img = font.render("EXIT", True, exitColor)
    screen.blit(img, (startExitX, startExitY))

    if mx > startPlayXcol and mx < startPlayXcol + playTextWidth and my > startPlayY and my < startPlayY + playTextHeight:
        selected = 0
    elif mx > startExitXcol and mx < startExitXcol + playTextWidth and my > startExitY and my < startExitY + playTextHeight:
        selected = 1
    else: selected = 3


    
    

    return selected, playTextWidth, menu, playing




exec(open("main.py").read())#### WEGHALEN IS VOOR TESTEN ZODAT F5 KAN DOEN IN DIT BESTAND