import pygame, math

class player(pygame.sprite.Sprite):

    def __init__(self):
        
        #init sprite
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("player_sprite.png").convert_alpha()
        
        #init rect and rect size vars
        self.rect = self.image.get_rect()
        self.size = pygame.math.Vector2(self.rect.w/2, self.rect.h/2)

        #init game mechanic vars
        self.pos = pygame.math.Vector2(self.rect.x,self.rect.y)
        self.health = 100
        self.movement_Speed = 250
        
        print("player class initialized")

    def rotate(self):
        mouse_x, mouse_y = pygame.mouse.get_pos()
        rel_x, rel_y = mouse_x - self.pos.x, mouse_y - self.pos.y
        angle = (180 / math.pi) * -math.atan2(rel_y, rel_x)
        #self.image = pygame.transform.rotate(self.image, int(angle)) ###DO NOT TURN ON### memory leak???
        

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
            
        #set sprite/rect location
        self.rect = (round(self.pos.x - self.size.x), round(self.pos.y - self.size.y))
        #self.rotate()
            
    def draw(self, surface):
        #debug
        pygame.draw.line(surface, (200, 0, 0), self.pos, pygame.mouse.get_pos())



        #draw the player
        #pygame.draw.rect(surface, (244, 0, 0), (self.pos.x, self.pos.y, 64, 64))
        



     



