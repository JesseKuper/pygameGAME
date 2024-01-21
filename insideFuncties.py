import pygame

def houseDraw(screen, screenRes):
    floor = pygame.draw.rect(screen, (161, 102, 47), pygame.Rect(screenRes[0] // 10, screenRes[1] // 10, screenRes[0] - (screenRes[0]//5), screenRes[1] - (screenRes[1]//5)))

    wN = pygame.draw.rect(screen, (200, 200, 100), pygame.Rect(screenRes[0] // 10 - 20, (screenRes[1] // 10) - 20, screenRes[0] - (screenRes[0]//5) + 40, 20))
    wS = pygame.draw.rect(screen, (200, 200, 100), pygame.Rect(screenRes[0] // 10 - 20, screenRes[1] - (screenRes[1] // 10), screenRes[0] - (screenRes[0]//5) +40, 20))
    wE = pygame.draw.rect(screen, (200, 200, 100), pygame.Rect(screenRes[0] - (screenRes[0] // 10) , screenRes[1] // 10, 20, screenRes[1] - (screenRes[1]//5)))
    wW = pygame.draw.rect(screen, (200, 200, 100), pygame.Rect(screenRes[0] // 10 - 20, screenRes[1] // 10, 20, screenRes[1] - (screenRes[1]//5)))

    door = pygame.draw.rect(screen, "black", pygame.Rect(screenRes[0] - (screenRes[0] // 4), screenRes[1] - (screenRes[1] // 10) - 20, screenRes[0]//10, 40))
    
    walls = [wN.y, wE.x, wS.y, wW.x]
    return floor, walls, door

def armoryDraw(screen, screenRes): 
    floor = pygame.draw.rect(screen, (153, 153, 153), pygame.Rect(screenRes[0] // 10- 20, (screenRes[1] // 10) - 20, screenRes[0] / 3, screenRes[1] - (screenRes[1]//5) + 20))
 
    wN = pygame.draw.rect(screen, (56, 56, 56), pygame.Rect(screenRes[0] // 10- 20, (screenRes[1] // 10) - 20, screenRes[0] // 3 + 20, 20))
    wS = pygame.draw.rect(screen, (56, 56, 56), pygame.Rect(screenRes[0] // 10 - 20, screenRes[1] - (screenRes[1] // 10), screenRes[0] // 3 + 20, 20))
    wE = pygame.draw.rect(screen, (56, 56, 56), pygame.Rect((screenRes[0] // 2) - 150 , screenRes[1] // 10, 20, screenRes[1] - (screenRes[1]//5)))
    wW = pygame.draw.rect(screen, (56, 56, 56), pygame.Rect(screenRes[0] // 10 - 20, screenRes[1] // 10, 20, screenRes[1] - (screenRes[1]//5)))

    shop = pygame.draw.rect(screen, (80, 80, 80), pygame.Rect(300, 200, 400, 100))

    door = pygame.draw.rect(screen, "black", pygame.Rect(screenRes[0] // 3 + 150, screenRes[1] - (screenRes[1]//3), 40, 150))
    
    walls = [wN.y, wE.x, wS.y, wW.x]
    return floor, walls, door, shop.y