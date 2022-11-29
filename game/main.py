import pygame, sys, time, math, json
from classes import c_base_enemy, c_player
from realutil import debug_text

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
    pygame.display.set_caption('Gun Blazers')

    debug = debug_text()
    debug.add_perma("Hello", pygame.Color("black"))
    debug.add_perma("pygame!", pygame.Color("red"))

    #set cursor icon
    pygame.mouse.set_cursor(pygame.cursors.diamond)
     
    #setup entity list and add a player
    local_player = c_player.player(
            pygame.Vector2(screen_size/2),
            "player_sprite.png")
    
    entity_list = []
    entity_list.append(c_base_enemy.base_enemy(
            pygame.Vector2(screen_size/4)))
    
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
        local_player.update(dt)
        for entity in entity_list:
            entity.update(dt, local_player)

        #############
        #  drawing  #
        #############

        #clear screen
        window.blit(background, (0, 0))
        background.fill(pygame.Color('#ffffff'))
        
        debug.add(dt, pygame.Color("black"))
        debug.add("player", pygame.Color("blue"), local_player.pos)
        

        #draw entities
        local_player.draw(window)
        for entity in entity_list:
            entity.draw(window)
        
        #display debug text
        debug.draw_flush(window)
        #pygame update functions
        pygame.display.update()
        clock.tick()
#opbject orietend programming 
if __name__ == "__main__":
    main()