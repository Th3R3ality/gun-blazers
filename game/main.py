import pygame, sys, time, math, json

from classes import c_player

def main():
    f = open("game/settings.json")
    settings = json.load(f)
    
    #initialize settings

    screen_size = pygame.math.Vector2(settings["screen_width"], settings["screen_height"])
    
    #initialize pygame stuff
    pygame.init()
    clock = pygame.time.Clock()
    window = pygame.display.set_mode(screen_size)
    background = pygame.Surface(screen_size); background.fill(pygame.Color('#ffffff'))
    font = pygame.font.SysFont("Arial", 18)
    
    pygame.display.set_caption('Gun Blazers')
    
    pygame.mouse.set_cursor(pygame.cursors.diamond)
     
    entity_list = []

    entity_list.append(c_player.player())


    prev_time = time.time()
    while True: ###main loop###
        dt = time.time() - prev_time #calculate deltatime
        prev_time = time.time()

        ################
        #  game logic  #
        ################

        #event loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        
        #update entities
        for entity in entity_list:
            entity.update(dt)
        


        #############
        #  drawing  #
        #############

        #clear screen
        window.blit(background, (0, 0))
        background.fill(pygame.Color('#ffffff'))
        
        #display delta time
        dt_text = font.render(str(dt), 1, pygame.Color("black"))
        window.blit(dt_text, (10, 0))
        
        #draw entities
        for entity in entity_list:
            window.blit(entity.image, entity.rect)
        
        pygame.display.update()
        clock.tick()

#opbject orietend programming 
if __name__ == "__main__":
    main()