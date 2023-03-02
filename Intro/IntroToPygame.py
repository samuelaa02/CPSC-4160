import pygame, sys, time

#Globals
SCREEN_SIZE = SCREEN_WIDTH, SCREEN_HEIGHT = 600, 600
SCREEN_COLOR = 0x006060


rectColor = 0xffffff
rectSize = rectWidth, rectHeight = 50, 50
rectPos = rectX, rectY = 150, 150
rectSpeed = 5
gravSpeed = 4

gameRect = pygame.Rect(rectX, rectY, rectWidth, rectHeight)

def move_rect(gameRect):
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        gameRect.move_ip(-rectSpeed,0)
    if keys[pygame.K_RIGHT]:
        gameRect.move_ip(rectSpeed,0)
    if keys[pygame.K_UP]:
        gameRect.move_ip(0,-rectSpeed)
    if keys[pygame.K_DOWN]:
        gameRect.move_ip(0,rectSpeed)
    gravity(gameRect)
    
def gravity(gameRect):
    keys = pygame.key.get_pressed()
    if not keys[pygame.K_UP]:
        gameRect.move_ip(0,gravSpeed)
        



#Initalization and Setup
pygame.init
pygame.display.set_caption("I am a game!")
surface = pygame.display.set_mode(SCREEN_SIZE)


#Game Loop
while True:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    gameRect.clamp_ip(surface.get_rect())
    move_rect(gameRect)
    surface.fill(SCREEN_COLOR)
    pygame.draw.rect(surface, rectColor, gameRect)
    pygame.display.update()
    pygame.time.wait(17)
    
