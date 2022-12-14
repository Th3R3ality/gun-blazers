import pygame, math
from realutil import *
from classes import c_bullet

bullets = []
correction_angle = 90
fire_rate = 1
#class player(pygame.sprite.Sprite):
class player():
    
    def __init__(self, pos = pygame.Vector2(0,0), sprite = "", scale = (75,75)):
        #init sprite vars
        self.image = {}
        if sprite == "":
            self.image_orig = pygame.Surface([25,25])
            self.image_orig.fill(pygame.Color("green"))
        else:
            self.image_orig = pygame.image.load(sprite).convert_alpha()
        
        self.image_orig = pygame.transform.scale(self.image_orig, scale)
        self.image = self.image_orig
        self.rect = self.image.get_rect()
        self.direction = 0
        #init game mechanic vars
        self.pos = pos
        self.health = 100
        self.movement_speed_orig = 250
        self.movement_speed = self.movement_speed_orig
        self.time_since_last_shot = 0
        self.spawnTime = 0
        
        print("player class initialized")

    def rotate(self, angle):
        self.image = pygame.transform.rotate(self.image_orig, angle)

    def shoot(self, dt):
        bullets.append(c_bullet.bullet(self.pos.x, self.pos.y, self.direction))


    def draw(self, surface):
        angle_to_cursor = atan2d(pygame.mouse.get_pos(), self.pos)
        #pygame.draw.line(surface, (200, 0, 0), self.pos, pygame.mouse.get_pos(), 10)
        self.rotate(angle_to_cursor)
        #set player direction and make sure its 360 degrees not 180 to -180
        if angle_to_cursor < 0:
            self.direction = 360 + angle_to_cursor
        elif angle_to_cursor >= 0:
            self.direction = angle_to_cursor


        self.rect = self.image.get_rect()
        self.rect = pygame.Vector2(self.pos.x - self.rect.w/2, self.pos.y - self.rect.h/2)
        surface.blit(self.image, self.rect)


        #draw bullets
        #for bullet in bullets:
            #surface.blit(surface, bullet.image.get_rect)
            
        #bullet removal and movement
        for bullet in bullets:
            if bullet.x < 800 and bullet.x > 0:
                bullet.draw(surface)
                #bullet.debug()
            else:
                bullets.pop(bullets.index(bullet))#remove bullet if its not visible

            if bullet.x > 800 or bullet.y > 600:
                bullets.remove(bullet)

    def update(self, dt):
        #debug
        #print("PlayerDirection: " + str(self.direction))
        #print("x: " + str(self.pos.x))
        #print("y: " + str(self.pos.y))

        for bullet in bullets:
            bullet.update()
            if bullet.x > 800 or bullet.y > 600:
                bullets.remove(bullet)

        self.time_since_last_shot += dt
        self.spawnTime += dt

        
    


        
        
        



     



