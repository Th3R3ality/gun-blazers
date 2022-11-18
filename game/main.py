import pygame, sys, time, math, json
from classes import c_player

def main():

    #initialize settings
    f = open("game/settings.json")
    settings = json.load(f)
    screen_size = pygame.math.Vector2(settings["screen_width"], settings["screen_height"])
    
    #initialize pygame, font and window
    pygame.init()
    clock = pygame.time.Clock()
    window = pygame.display.set_mode(screen_size)
    background = pygame.Surface(screen_size); background.fill(pygame.Color('#ffffff'))
    font = pygame.font.SysFont("Arial", 18)
    pygame.display.set_caption('Gun Blazers')

    #set cursor icon
    pygame.mouse.set_cursor(pygame.cursors.diamond)
     
    #setup entity list and add a player
    entity_list = []
    entity_list.append(c_player.player(
            pygame.Vector2(screen_size/2),
            "player_sprite.png"))
    
    ##
    
    ###############
    #  main loop  #
    ###############
    prev_time = time.time()
    while True:
        dt = time.time() - prev_time #calculate deltatime (precise time since last frame)
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
            entity.draw(window)
        
        #pygame update functions
        pygame.display.update()
        clock.tick()
#opbject orietend programming 
if __name__ == "__main__":
    main()