import pygame

class Player:

    def __init__(self):
        #sprites n shit

        #mechanical shit
        self.health = 100
        self.movement_Speed = 0.4
        
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

        #movement
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            self.y -= self.movement_Speed * time
        if keys[pygame.K_s]:
            self.y += self.movement_Speed * time
        if keys[pygame.K_a]:
            self.x -= self.movement_Speed * time
        if keys[pygame.K_d]:
            self.x += self.movement_Speed * time



print("Player initialized")