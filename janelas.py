#crlt+f5 compila o codigo sem debugar (vscode)
import pygame

pygame.init()  #inicialização do modulo pygame
display = pygame.display.set_mode([840,480])  #definição de resolução
pygame.display.set_caption("Meu Super Jogo 01") #altera nome da janela

def draw(): #funçao para a parti grafica (proximas aulas)
    display.fill([78, 142, 237]) #altera cor background


if __name__== "__main__":
    
    gameLoop = True 

    while gameLoop:
        draw()
        pygame.display.update()  #loop que permite que a tela fica estatica