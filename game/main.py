import pygame, sys, time, math

from classes.c_player import Player


def main():
    #intiliaze all the important stuff
    pygame.init()
    pygame.display.set_caption('Gun Blazers')
    window = pygame.display.set_mode((800, 600))
    clock = pygame.time.Clock()
    background = pygame.Surface((800, 600))
    background.fill(pygame.Color('#ffffff'))
    pygame.mouse.set_cursor(pygame.cursors.diamond)
    is_running = True

    #initialize player 
    player = Player()

    #main game loop btw
    while is_running:
        
        #UPADTE FUNCTION
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                is_running = False
        window.blit(background, (0, 0))
        time = clock.tick(60)
        player.update(window, time)
        pygame.display.update()
    







#opbject orietend programming 
if __name__ == "__main__":
    main()