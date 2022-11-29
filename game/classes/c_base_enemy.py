import pygame, math
from realutil import *
class base_enemy():

    def __init__(self, init_pos = pygame.Vector2(0,0), init_sprite = "", init_scale = (50,50)) -> None:
        #init sprite vars
        self.image = {}
        if init_sprite == "":
            self.image = pygame.Surface([25,25])
            self.image.fill(pygame.Color("red"))
        else:
            self.image = pygame.image.load(init_sprite).convert_alpha()
        
        self.image = pygame.transform.scale(self.image, init_scale)
        self.rect = self.image.get_rect()
        self.size = pygame.Vector2(self.rect.w, self.rect.h)

        #init game mechanic vars
        self.pos = init_pos
        self.health = 100
        self.movement_speed = 150
        
        print("base_enemy class initialized")

    def update(self, dt, target):
        dir = atan2d(self.pos, target.pos)
        self.pos.x += self.movement_speed * math.sin(math.radians(dir)) * dt
        self.pos.y += self.movement_speed * math.cos(math.radians(dir)) * dt

    def draw(self, surface):
        self.rect = self.image.get_rect()
        self.rect = pygame.Vector2(self.pos.x - self.rect.w/2, self.pos.y - self.rect.h/2)
        surface.blit(self.image, self.rect)
        