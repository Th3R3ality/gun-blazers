import pygame, math
class base_enemy():

    def __init__(self, pos = pygame.Vector2(0,0), sprite = "", scale = (75,75)):
        #init sprite vars
        self.image_orig = {}
        if sprite == "":
            self.image_orig = pygame.Surface(scale)
            self.image_orig.fill(pygame.Color("red"))
        else:
            self.image_orig = pygame.transform.scale(pygame.image.load(sprite).convert_alpha(), scale)
        self.image = self.image_orig

        #init game mechanic vars
        self.pos = pos
        self.health = 100
        self.movement_Speed = 100
        
        print("base_enemy class initialized")

    def rotate(self, angle):
        self.image = pygame.transform.rotate(self.image_orig, angle)

    def update(self):
        pass

    def draw(self, surface):
        self.rect = self.image_orig.get_rect()
        self.rect = pygame.Vector2(self.pos.x - self.rect.w/2, self.pos.y - self.rect.h/2)
        surface.blit(self.image_orig, self.rect)