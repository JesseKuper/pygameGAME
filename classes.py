

class Enemy:
    def __init__(self, health, size, name, color, pos):
        self.health = health
        self.size = size
        self.name = name
        self.color = color
        self.pos = pos
    def walk(self):
        print("walking")

enemy1 = Enemy(30,50, "en1", "red", 30)

print(enemy1.pos)

enemy1.walk()