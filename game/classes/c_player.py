import pygame, math

correction_angle = 90
#class player(pygame.sprite.Sprite):
class player():

    def __init__(self, pos = pygame.Vector2(0,0), sprite = "", scale = (75,75)):
        #init sprite vars
        self.image = {}
        if sprite == "":
            self.image = pygame.Surface([25,25])
            self.image.fill(pygame.Color("red"))
        else:
            self.image = pygame.image.load(sprite).convert_alpha()
        
        self.image = pygame.transform.scale(self.image, scale)
        self.rect = self.image.get_rect()
        self.size = pygame.Vector2(self.rect.w, self.rect.h)
        #init game mechanic vars
        self.pos = pos
        self.health = 100
        self.movement_Speed = 250
        
        print("player class initialized")

    def rotate(self, surface):
        mx, my = pygame.mouse.get_pos()
        dx, dy = mx - self.pos.x, my - self.pos.y
        angle = math.degrees(math.atan2(-dy, dx)) - correction_angle
        self.image = pygame.transform.rotate(self.image, angle)
        self.rect = self.image.get_rect()

    def draw(self, surface):
        pygame.draw.line(surface, (200, 0, 0), self.pos, pygame.mouse.get_pos(), 10)
        self.rotate(surface)
        
        surface.blit(self.image, self.pos)


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
        

            
        
        
        



     



