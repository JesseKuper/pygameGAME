import pygame
def newMap():
    map = [
    "1 1 1 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 1 1 1 1 1 1",
    "1 1 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 1 1 1 1",
    "1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 1 1",
    "0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 1 1",
    "0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 1",
    "0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1",
    "1 0 0 0 0 0 0 0 0 0 0 0 0 1 1 1 1 1 1 1 0 0 0 0 0 0 0 0 0 0 0 0",
    "1 1 0 0 0 0 0 0 0 0 0 0 0 1 1 1 1 1 1 1 1 0 0 0 0 0 0 0 0 0 0 0",
    "1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 1 1 1 1 1 1 0 0 0 0 0 0 0 0 0 0",
    "0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 1 0 0 0 0 0 0 0 0 0 0 0 0",
    "0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0",
    "0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0",
    "0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0",
    "1 1 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0",
    "1 1 1 1 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0",
    "1 1 1 1 1 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0",
    "1 1 1 1 1 1 0 0 0 0 0 0 0 0 0 2 2 2 2 2 2 0 0 0 0 0 0 0 0 0 0 0",
    "1 1 1 1 1 0 0 0 0 0 0 0 0 0 2 2 2 2 2 2 2 2 2 0 0 0 0 0 0 0 0 0",
]
    return map

def wildCalcMap(screen, map, mapCalculated):
    telX = 0
    telY = 0
    waterX = waterY = treeX = treeY = []
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

def wildDrawMap(screen, waterX, waterY, treeX, treeY):
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


def wildDraw(screen, screenRes):
    wildEntrance = pygame.draw.rect(screen, "black", pygame.Rect(0, screenRes[1]/2, 20, 200))
    return wildEntrance

exec(open("main.py").read())#### WEGHALEN IS VOOR TESTEN ZODAT F5 KAN DOEN IN DIT BESTAND