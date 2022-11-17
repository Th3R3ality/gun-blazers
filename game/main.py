import pygame, sys, time, math

from classes.c_player import Player


pygame.init()
clock = pygame.time.Clock()
font = pygame.font.SysFont("Arial", 18)

def deltaTime(time):
    

def main():
    
    #intiliaze all the important stuff
    pygame.display.set_caption('Gun Blazers')
    window = pygame.display.set_mode((1600, 900))
    clock = pygame.time.Clock()
    background = pygame.Surface((1600, 900))
    background.fill(pygame.Color('#ffffff'))
    pygame.mouse.set_cursor(pygame.cursors.diamond)
    is_running = True

    #initialize player 
    player = Player()

    #main game loop btw
    while is_running:
        #UPADTE FUNCTION
        fps = str(int(clock.get_fps()))
        fps_text = font.render(fps, 1, pygame.Color("black"))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                is_running = False
        window.blit(background, (0, 0))
        window.blit(fps_text, (10, 0))
        #time = Tick()
        time = clock.tick()
        player.update(window, time)
        pygame.display.update()
    







#opbject orietend programming 
if __name__ == "__main__":
    main()