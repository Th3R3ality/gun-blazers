import pygame

class bullet:
    def __init__(self, x, y):
        sprite = ""
        scale = (75,75)
        if sprite == "":
            self.image_orig = pygame.Surface([25,25])
            self.image_orig.fill(pygame.Color("green"))
        else:
            self.image_orig = pygame.image.load(sprite).convert_alpha()
        
        self.image_orig = pygame.transform.scale(self.image_orig, scale)
        self.rect = self.image_orig.get_rect()
        self.radius = 10
        self.speed = 10
        
        self.x = x
        self.y = y

    def update(self):
        self.y -= self.speed

    def draw(self, surface):
        pygame.draw.circle(surface, (255, 0, 0), (self.x, self.y), self.radius)
        #surface.blit(self.image_orig, self.rect )
        #bruh ^^ green square

