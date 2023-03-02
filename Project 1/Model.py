import pygame, sys, Objects

# Constants
PLAYER_SPRITE = "./player.png"
PROJECTILE_SPRITE = "./projectile.png"

#custom level file
LEVEL = "./level.txt"


class Model:
    
    #game state stuff
    def __init__(self):
        self.existingEntities = []
        self.player = Objects.Player(PLAYER_SPRITE, 60, 0)
        self.stage = Level(LEVEL)


    def updateGameState(self, gametime):
        for e in self.existingEntities:
            e.physicsUpdate(gametime, self.stage)
        self.player.physicsUpdate(gametime, self.stage)
    
    def spawnEntity(self, spawnPos, direction ,type):
        if(type == "projectile"):
            projectile = Objects.Entity(PROJECTILE_SPRITE, spawnPos.x, spawnPos.y, True)
            if(direction == "right"):
                projectile.velocity.x = 4.0
            else:
                projectile.velocity.x = -4.0
            self.existingEntities.append(projectile)

        


#reads level data from file and converts to platform objects to be draw in scene
class Level:
    def __init__(self, levelFile):
        self.objects = []
        with open(levelFile) as file:
            for line in file:
                rectInfo = line.split()
                self.objects.append(Platform(rectInfo[0], int(rectInfo[1]), int(rectInfo[2]), int(rectInfo[3]), int(rectInfo[4])))

# objects that entities can collide with and stand on
class Platform:

    def __init__(self, color, x, y, width, height):
        self.rectangle = pygame.Rect(x, y, width, height)
        self.color = pygame.Color(color)

    
