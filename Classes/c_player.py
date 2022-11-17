import pygame

class Player:

    def __init__(self):
        #sprites n shit
        #self.surf = pygame.Surface((64, 64))
        #self.surf.fill(("#000000"))
        #self.rect = self.surf.get_rect(center = (400, 300))

        #mechanical shit
        self.health = 100
        self.movement_Speed = 1
        
        #movement shit
        self.x = 400
        self.y = 300
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False
    def update(self, surface, time):
        #draw the player
        pygame.draw.rect(surface, (244, 0, 0), (self.x, self.y, 64, 64))
        #check for movement
        if self.moving_up == True:
            self.y -= self.movement_Speed * time
        if self.moving_down == True:
            self.y += self.movement_Speed * time
        if self.moving_left == True:
            self.x -= self.movement_Speed * time
        if self.moving_right == True:
            self.x += self.movement_Speed * time

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    self.moving_up = True
                if event.key == pygame.K_s:
                    self.moving_down = True
                if event.key == pygame.K_a:
                    self.moving_left = True
                if event.key == pygame.K_d:
                    self.moving_right = True
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_w:
                    self.moving_up = False
                if event.key == pygame.K_s:
                    self.moving_down = False
                if event.key == pygame.K_a:
                    self.moving_left = False
                if event.key == pygame.K_d:
                    self.moving_right = False
                    

print("Player initialized")