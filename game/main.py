import pygame, sys, time, math

from classes.c_player import Player


pygame.init()
clock = pygame.time.Clock()
font = pygame.font.SysFont("Arial", 18)

def deltaTime(time):
    return

def main():
    
    #intiliaze all the important stuff
    pygame.display.set_caption('Gun Blazers')
    
    window = pygame.display.set_mode((400, 300))
    clock = pygame.time.Clock()
    background = pygame.Surface((400, 300))
    background.fill(pygame.Color('#ffffff'))
    
    pygame.mouse.set_cursor(pygame.cursors.diamond)
    
    #instantiate local_player 
    local_player = Player()



    #main game loop btw
    while True:
    
        #print(pygame.time.Clock.get_time())
        deltaTime = clock.tick(10)/1000
        
        #UPADTE FUNCTION
        fps_text = font.render(str(deltaTime), 1, pygame.Color("black"))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        
        
        #render/draw stuff
        window.blit(background, (0, 0))
        window.blit(fps_text, (10, 0))
        local_player.update(window, time)
        
        pygame.display.update()
    







#opbject orietend programming 
if __name__ == "__main__":
    main()