import pygame, sys, time, math

from Classes.c_player import Player


def main():
    #intiliaze all the important stuff
    pygame.init()
    pygame.display.set_caption('Gun Blazers')
    window_surface = pygame.display.set_mode((800, 600))

    background = pygame.Surface((800, 600))
    background.fill(pygame.Color('#000000'))

    is_running = True

    #initialize player 
    player = Player()

    #main game loop btw
    while is_running:
        
        #UPADTE FUNCTION
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                is_running = False

        window_surface.blit(background, (0, 0))

        pygame.display.update()
    







#opbject orietend programming 
if __name__ == "__main__":
    main()