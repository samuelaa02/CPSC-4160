import pygame, sys, Model

BACKGROUND_COLOR = 0x006060

class View:

    def __init__(self, model):
        #build screen
        self.model = model

        

    def updateView(self, surface):
        surface.fill(BACKGROUND_COLOR)
        for platform in self.model.stage.objects:
            pygame.draw.rect(surface, platform.color, platform.rectangle)
        for entity in self.model.existingEntities:
            surface.blit(entity.sprite, entity.position)
        surface.blit(self.model.player.sprite, self.model.player.position)
        pygame.display.flip()
            
