#crlt+f5 compila o codigo sem debugar (vscode)
import pygame

pygame.init()  #inicialização do modulo pygame
display = pygame.display.set_mode([840,480])  #definição de resolução
pygame.display.set_caption("Meu Super Jogo 01") #altera nome da janela

def draw(): #funçao para a parti grafica (proximas aulas)
    display.fill([78, 142, 237]) #altera cor background


if __name__== "__main__":
    
    game_loop = True 

    while game_loop:

        for event in pygame.event.get(): #fila de inputs
            if event.type == pygame.QUIT: #input para fechar o game
                game_loop = False
            
            elif event.type == pygame.KEYDOWN: #verifica se alguma tecla foi precionada
                if event.key == pygame.K_w:
                    print("w precionado")
            elif event.type == pygame.KEYUP: #verifica se alguma tecla foi solta
                if event.key == pygame.K_w:
                    print("W solto")

        keys = pygame.key.get_pressed() 

        if keys[pygame.K_w]: #verifica se esta segurando w
            print("Segura w")

        draw()
        pygame.display.update()  #loop que permite que a tela fica estatica