import pygame, math

correction_angle = 90
#class player(pygame.sprite.Sprite):
class player(pygame.sprite.Sprite):

    def __init__(self, pos = pygame.Vector2(0,0)):

        #init sprite vars
        self.image = pygame.image.load("player_sprite.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.size = pygame.Vector2(self.rect.w, self.rect.h)

        #init game mechanic vars
        self.pos = pos
        self.health = 100
        self.movement_Speed = 250
        
        print("player class initialized")

    def rotate(self):
        mouse_x, mouse_y = pygame.mouse.get_pos()
        player_rect = self.rect 
        rel_x, rel_y = mouse_x - self.pos.x, mouse_y - self.pos.y
        angle = math.degrees(math.atan2(-rel_y, rel_x)) - correction_angle   
        self.image = pygame.transform.rotate(self.image, angle) ###DO NOT TURN ON### memory leak???
        #self.image = self.image.get_rect().center

    def update(self, dt):
        #movement
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            self.pos.y -= self.movement_Speed * dt
        if keys[pygame.K_s]:
            self.pos.y += self.movement_Speed * dt
        if keys[pygame.K_a]:
            self.pos.x -= self.movement_Speed * dt
        if keys[pygame.K_d]:
            self.pos.x += self.movement_Speed * dt
        if keys[pygame.K_LEFT]:
            self.rotate()
        if keys[pygame.K_RIGHT]:
            self.rotate()
            
        #set sprite/rect location
        self.rect = (round(self.pos.x - self.size.x/2), round(self.pos.y - self.size.y/2))
        
            
    def draw(self, surface):
        pygame.draw.line(surface, (200, 0, 0), self.pos, pygame.mouse.get_pos())
        
        



     



