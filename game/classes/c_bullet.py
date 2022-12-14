import pygame, math
from realutil import *

class bullet:
    def __init__(self, x, y, facing):
        sprite = ""
        scale = (75,75)
        if sprite == "":
            self.image_orig = pygame.Surface([25,25])
            self.image_orig.fill(pygame.Color("green"))
        else:
            self.image_orig = pygame.image.load(sprite).convert_alpha()
        
        self.image_orig = pygame.transform.scale(self.image_orig, scale)
        self.image = self.image_orig
        self.rect = self.image_orig.get_rect()
        self.direction = facing
        self.enemy_pos = pygame.Vector2(0, 0)
        self.dist_bullet_enemy = 0
        self.radius = 3
        self.speed = 250
        self.x = x
        self.y = y
        self.pos = pygame.Vector2(self.x, self.y)

    def get_dist(self, enemy_pos):
        dist_bullet_enemy = self.pos - enemy_pos
        return dist_bullet_enemy

    def update(self, dt):
        #debug
        print("BulletDirection: " + str(self.direction))
        #move bullet
        #pygame.transform.rotate(self.image_orig, self.direction)
        self.x += self.speed * math.cos(math.radians(self.direction + 90)) * dt 
        self.y -= self.speed * math.sin(math.radians(self.direction + 90)) * dt
        #check collision
        #find dinstance and check if its lower than radius
        self.get_dist(self.enemy_pos)

    def draw(self, surface):
        pygame.draw.circle(surface, (0, 0, 0), (self.x, self.y), self.radius)

