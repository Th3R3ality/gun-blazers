import pygame, math

class Player:

    def __init__(self):
        #sprites n shit

        #mechanical shit
        self.x = 400
        self.y = 300
        self.position = pygame.Vector2(self.x,self.y)
        self.health = 100
        self.movement_Speed = 0.4
        

    def rotate(self):
        mouse_x, mouse_y = pygame.mouse.get_pos()
        rel_x, rel_y = mouse_x - self.x, mouse_y - self.y
        angle = (180 / math.pi) * -math.atan2(rel_y, rel_x)
        #self.image = pygame.transform.rotate(self.original_image, int(angle))
        #self.rect = self.image.get_rect(center=self.position)

    def update(self, surface, dt):
        #debug
        self.position = pygame.Vector2(self.x,self.y)
        pygame.draw.line(surface, (200, 0, 0), self.position, pygame.mouse.get_pos())

        #draw the player
        pygame.draw.rect(surface, (244, 0, 0), (self.x, self.y, 64, 64))
        self.rotate()
        #movement
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            self.y -= self.movement_Speed * dt
        if keys[pygame.K_s]:
            self.y += self.movement_Speed * dt
        if keys[pygame.K_a]:
            self.x -= self.movement_Speed * dt
        if keys[pygame.K_d]:
            self.x += self.movement_Speed * dt



     



print("Player initialized")