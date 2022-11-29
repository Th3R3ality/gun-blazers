import pygame, math
from realutil import *

correction_angle = 90
#class player(pygame.sprite.Sprite):
class player():

    def __init__(self, pos = pygame.Vector2(0,0), sprite = "", scale = (75,75)):
        #init sprite vars
        self.image = {}
        if sprite == "":
            self.image_orig = pygame.Surface([25,25])
            self.image_orig.fill(pygame.Color("red"))
        else:
            self.image_orig = pygame.image.load(sprite).convert_alpha()
        
        self.image_orig = pygame.transform.scale(self.image_orig, scale)
        self.image = self.image_orig
        self.rect = self.image.get_rect()
        
        #init game mechanic vars
        self.pos = pos
        self.health = 100
        self.movement_speed = 250
        
        print("player class initialized")

    def rotate(self, angle):
        self.image = pygame.transform.rotate(self.image_orig, angle)
        

    def draw(self, surface):
        angle_to_cursor = atan2d(pygame.mouse.get_pos(), self.pos)
        pygame.draw.line(surface, (200, 0, 0), self.pos, pygame.mouse.get_pos(), 10)
        self.rotate(angle_to_cursor)
        
        self.rect = self.image.get_rect()
        self.rect = pygame.Vector2(self.pos.x - self.rect.w/2, self.pos.y - self.rect.h/2)
        surface.blit(self.image, self.rect)


    def update(self, dt):
        #movement
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            self.pos.y -= self.movement_speed * dt
        if keys[pygame.K_s]:
            self.pos.y += self.movement_speed * dt
        if keys[pygame.K_a]:
            self.pos.x -= self.movement_speed * dt
        if keys[pygame.K_d]:
            self.pos.x += self.movement_speed * dt
        

            
        
        
        



     



