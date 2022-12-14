import pygame, sys, time, math, json, os, random
from classes import c_base_enemy, c_player, c_bullet
from realutil import debug_text, point_in_circle

def main():

    killAmmount = 0
    print("Working dir:", os.getcwd())
    #initialize settings
    f = open("game/settings.json")
    settings = json.load(f)
    screen_size = pygame.math.Vector2(settings["screen_width"], settings["screen_height"])

    #music
    pygame.mixer.init()
    pygame.mixer.music.load('game/hot_garbage.wav')
    pygame.mixer.music.play()
    
    #initialize pygame, font and window
    pygame.init()
    clock = pygame.time.Clock()
    window = pygame.display.set_mode(screen_size)
    background = pygame.Surface(screen_size); background.fill(pygame.Color('#ffffff'))
    pygame.display.set_caption('Gun Blazers')

    debug = debug_text()
    debug.add_perma("Gun Blazers", pygame.Color("black"))

    #set cursor icon
    pygame.mouse.set_cursor(pygame.cursors.diamond)
     
    #setup entity list and add a player
    bullet_list = []
    local_player = c_player.player(
            pygame.Vector2(screen_size/2),
            "player_sprite.png")
    
    entity_list = []

    
    
    
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
        #spawn enemies
        #print(local_player.spawnTime)

        #fuck it spawn infinite
        if(local_player.spawnTime > 0.4):
            local_player.spawnTime = 0
            dir = random.randrange(0, 360)
            dist = 1000
            entity_list.append(c_base_enemy.base_enemy(
            pygame.Vector2(math.cos(math.radians(dir)) * dist, math.sin(math.radians(dir)) * dist),
            "enemy.png"))



        #event loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        #controls/input
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            local_player.pos.y -= local_player.movement_speed_orig * dt
        if keys[pygame.K_s]:
            local_player.pos.y += local_player.movement_speed_orig * dt
        if keys[pygame.K_a]:
            local_player.pos.x -= local_player.movement_speed_orig * dt
        if keys[pygame.K_d]:
            local_player.pos.x += local_player.movement_speed_orig * dt
        if keys[pygame.K_SPACE]:
            if local_player.time_since_last_shot > 0.17:
                local_player.time_since_last_shot = 0
                bullet_list.append(c_bullet.bullet(local_player.pos.x, local_player.pos.y, local_player.direction))

        
        #update entities
        local_player.update(dt)
        for eidx, entity in enumerate(entity_list):
            entity.update(dt, local_player)
        
        for bidx, bullet in enumerate(bullet_list):
            hit = False
            bullet.update(dt)
            #debug.add("bullet pos", pygame.Color("black"), (bullet.x, bullet.y))
            for eidx, entity in enumerate(entity_list):
                if point_in_circle((bullet.x, bullet.y), entity.pos, entity.radius):
                    hit = True
                    killAmmount += 1
                    print("rip")
                    
                    entity_list.pop(eidx)
                    #debug.add("bullet colliding", pygame.Color("red"))
                    continue
            if hit:
                bullet_list.pop(bidx)
                


        #############
        #  drawing  # 
        #############

        #clear screen
        window.blit(background, (0, 0))
        background.fill(pygame.Color('#ffffff'))
        #debug.add(f"frametime: {dt}", pygame.Color("black"))
        #debug.add("player", pygame.Color("blue"), local_player.pos)
        debug.add("",pygame.Color("white"))
        debug.add("",pygame.Color("white"))
        debug.add(f'KILLS: {killAmmount} ', pygame.Color("red"))
        

        #draw entities
        local_player.draw(window)
        for entity in entity_list:
            entity.draw(window)
        for bullet in bullet_list:
            bullet.draw(window)


        #display debug text
        debug.draw_flush(window)
        #pygame update functions
        pygame.display.update()
        clock.tick()



#opbject orietend programming 
if __name__ == "__main__":
    main()