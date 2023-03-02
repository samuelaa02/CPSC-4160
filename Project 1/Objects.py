import pygame, sys

#   Constants
GRAVITY = .1
P_MAX_SPEED = 1
P_SPRINT_MULTI = 1.5
P_ACCEL = .1
P_JUMP_HEIGHT = -4




# Entity Class -- things that move
class Entity:
    #   Parameters:
    #   sprite - String - path to sprite location
    #   x - int - x location on screen
    #   y - int - y location on screen
    #   gravity - bool - whether or not gravity affects this entity
    def __init__(self, sprite, x, y, gravity):
        self.sprite = pygame.image.load(sprite)
        self.rect = self.sprite.get_rect()
        self.position = pygame.math.Vector2(x,y)
        self.velocity = pygame.math.Vector2(x=0,y=0)
        self.gravity = gravity
        self.grounded = False
        self.direction = "left"

    #apply physics calculations
    def physicsUpdate(self, gametime, stage):
        self.gravityUpdate()
        self.collisionUpdate(stage)
        self.velocityUpdate(gametime) #may need to swap to last check

    #check for collisions and apply collision physics
    def collisionUpdate(self, stage):
        testGrounded = False
        for obj in stage.objects:
           
            #check if colliding, if they are, check which form of collision
            #if(pygame.Rect.colliderect(obj.rectangle, self.rect)):
            if(self.gravity):
                testGrounded = testGrounded or self.collisionGround(obj.rectangle)
            self.collisionWall(obj.rectangle)
            self.collisionCeiling(obj.rectangle)
        self.grounded = testGrounded

    #check if the entity collides with a wall
    def collisionWall(self, other):
        leftLine = ((self.position.x, self.position.y + 1), (self.position.x, self.position.y + 15))
        rightLine = ((self.position.x + 16, self.position.y + 1), (self.position.x + 16, self.position.y + 15))
        if(other.clipline(leftLine) ):
            self.velocity.x = 0
            self.position.x = other.right + 1
        elif(other.clipline(rightLine)):
            self.velocity.x = 0
            self.position.x = other.left -17
    
    #check if the entity collided with the ground
    def collisionGround(self, other):
        bottomLine = ((self.position.x+1, self.position.y + 16), (self.position.x + 15, self.position.y + 16))
        if(other.clipline(bottomLine)):
            self.velocity.y = 0
            self.position.y = other.top - 16
            return True
        else:
            return False

    #check if the entitiy collided with a ceiling
    def collisionCeiling(self, other):
        topLine = ((self.position.x+1, self.position.y), (self.position.x + 15, self.position.y))
        if(other.clipline(topLine)):
            self.velocity.y = 0
            self.position.y = other.bottom + 1

    #update position based on current velocity
    def velocityUpdate(self, gametime):
        self.position.x += self.velocity.x
        self.position.y += self.velocity.y

    #update current velocity based on gravity
    def gravityUpdate(self):
        if(self.gravity and not self.grounded and self.velocity.y < -P_JUMP_HEIGHT):
            self.velocity.y += GRAVITY

    

#Player Class-- inherits from entity
class Player(Entity):

    def __init__(self, sprite, x, y):
        super().__init__(sprite, x, y, True)

    
    #add vertical acceleration to player
    def playerJump(self):
        if(self.grounded):
            self.position.y -= 1
            self.velocity.y += P_JUMP_HEIGHT
            self.grounded = False
    
    #add left acceleration to player
    def playerMoveLeft(self):
        if(self.velocity.x > -P_MAX_SPEED):
            self.velocity.x -= P_ACCEL
            self.direction = "left"
    
    #add right acceleration to player
    def playerMoveRight(self):
        if(self.velocity.x < P_MAX_SPEED):
            self.velocity.x += P_ACCEL
            self.direction = "right"
    
    #deccelerate player
    def playerBreak(self):
        if(self.velocity.x < 0.11 and self.velocity.x > -0.11):
            self.velocity.x = 0
        elif(self.velocity.x > 0):
            self.velocity.x -= P_ACCEL
        elif(self.velocity.x < 0):
            self.velocity.x += P_ACCEL
        
    



