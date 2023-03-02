import pygame, sys, Model, View, Controller, time


pygame.init
pygame.display.set_caption("Sam's Project 1")
displayFlags = pygame.SCALED | pygame.RESIZABLE
gameWindow = pygame.display.set_mode((960,540),displayFlags)

model = Model.Model()
controller = Controller.Controller(model)
view = View.View(model)
clock = pygame.time.Clock()

def gameLoop():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        
        dt = clock.tick(60)
        gametime = 1 / float(dt)
        
        controller.userInput()
        model.updateGameState(gametime)
        view.updateView(gameWindow)
        pygame.time.wait(10)
        


gameLoop()
