import pygame

class Player:

    def __init__(self):
        #sprites n shit
        self.surf = pygame.Surface((30, 30))
        self.surf.fill((128,255,40))



        #mechanical shit
        self.health = 100
        self.movement_Speed = 1

        #movement shit
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False