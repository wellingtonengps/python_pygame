import pygame

pygame.init() 
display = pygame.display.set_mode([840,480])  
pygame.display.set_caption("Meu Super Jogo 01") 


if __name__== "__main__":
    
    #grupo de desenho
    drawGroup = pygame.sprite.Group()    

    #player
    player = pygame.sprite.Sprite(drawGroup)
    player.image = pygame.image.load("data/player.png")
    player.image = pygame.transform.scale(player.image, [100,100])
    player.rect = pygame.Rect(0,0,200,200)

    game_loop = True 

    while game_loop:

        for event in pygame.event.get(): 
            if event.type == pygame.QUIT: 
                game_loop = False


        keys = pygame.key.get_pressed() 

        if keys[pygame.K_d]:
            player.rect.x += 1
        if keys[pygame.K_a]:
            player.rect.x -= 1
        if keys[pygame.K_w]:
            player.rect.y -= 1
        if keys[pygame.K_s]:
            player.rect.y += 1

        #drawt
        display.fill([78, 142, 237]) 

    
        drawGroup.draw(display)



        pygame.display.update() 