import pygame, math
class base_enemy():

    def __init__(self, pos = pygame.Vector2(0,0), sprite = "", scale = (75,75)) -> None:
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
        self.movement_speed = 100
        
        print("base_enemy class initialized")

    def update(self):
        pass

    def draw(self, surface):
        self.rect = self.image.get_rect()
        self.rect = pygame.Vector2(self.pos.x - self.rect.w/2, self.pos.y - self.rect.h/2)
        surface.blit(self.image, self.rect)
        