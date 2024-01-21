import pygame


def outsideCalcMap(screen, map, mapCalculated):
    telX = 0
    telY = 0
    waterX = []
    waterY = []
    treeX = []
    treeY = []
    for i in map:
        telX = 0
        string = i.split()
        for x in string:
            if int(x) == 1:
                waterX.append(telX)
                waterY.append(telY)
            if int(x) == 2:
                treeX.append(telX)
                treeY.append(telY)
            telX += 60
        telY += 60
    mapCalculated = True
    return waterX, waterY, treeX, treeY, mapCalculated


def outsideDrawMap(screen, waterX, waterY, treeX, treeY):
    tel = 0
    while tel <= len(waterX):
        try:
            mapBuild = pygame.draw.rect(screen, (0, 101, 168), pygame.Rect(waterX[tel], waterY[tel], 60, 60))
        except:
            pass # try except methode hier niet beste manier misschien later verbeteren?
        tel += 1

    tel2 = 0
    while tel2 <= len(treeX):
        try:
            mapBuild = pygame.draw.rect(screen, (1, 46, 13), pygame.Rect(treeX[tel2], treeY[tel2], 60, 60))
        except:
            pass
        tel2 += 1

def outsideDraw(screen, screenRes):
    width = 0
    house = pygame.draw.rect(screen, "red", pygame.Rect(200, 100, 300, 200))
    houseEntrance = pygame.draw.rect(screen, "black", pygame.Rect(310, 290, 80, 20))

    armory = pygame.draw.rect(screen, (46, 46, 46), pygame.Rect(400, screenRes[1] - 250, 120, 220))
    armoryEntrance = pygame.draw.rect(screen, "black", pygame.Rect(515, screenRes[1] - 90, 15, 40))

    wildEntrance = pygame.draw.rect(screen, "black", pygame.Rect(screenRes[0] - 20, screenRes[1]/2, 20, 200))

    return houseEntrance, armoryEntrance, wildEntrance