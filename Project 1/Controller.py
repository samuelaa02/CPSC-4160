import pygame, sys, Objects, Model

class Controller:

    def __init__(self, model):
        self.model = model
        

    def userInput(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            self.model.player.playerJump()
        if keys[pygame.K_d]:
            self.model.player.playerMoveRight()
        if keys[pygame.K_a]:
            self.model.player.playerMoveLeft()
        if keys[pygame.K_e]:
            self.model.spawnEntity(self.model.player.position, self.model.player.direction, "projectile")
        if not (keys[pygame.K_a] or keys[pygame.K_d]):
            self.model.player.playerBreak()
        
        
