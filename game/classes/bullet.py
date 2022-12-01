import pygame

class Bullet():
    def __init__(self, x, y, radius, color, facing, sprite = "", scale = (5, 5)):
        self.image = {}
        if sprite == "":
            self.image_orig = pygame.Surface([25,25])
            self.image_orig.fill(pygame.Color("red"))
        else:
            self.image_orig = pygame.image.load(sprite).convert_alpha()

        self.image_orig = pygame.transform.scale(self.image_orig, scale)

        self.image = self.image_orig
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.facing = facing
        self.vel = 1 * facing
        self.rect = self.image.get_rect()

    def draw(self):
        #moving the bullet(commented out bcs of debugging)
        #self.x += self.vel 
        self.rect.center = self.pos


    def debug(self):
        print("x: " + str(self.x))
        print("y: " + str(self.y))
        print("velocity:" + str(self.vel))