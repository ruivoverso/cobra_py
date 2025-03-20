import pygame
from pygame.locals import *

import random 

WINDOWS_WIDTH = 500
WINDOWS_HEIGHT = 500
POS_INICIAL_X = WINDOWS_WIDTH / 2 
POS_INICIAL_Y = WINDOWS_HEIGHT / 2 
BLOCK = 15

def verifica_margem(pos):
    if 0 <= pos[0] < WINDOWS_WIDTH and <= pos[1] < WINDOWS_HEIGHT
        return False
    else: 
        return True

def gera_pos_aleatoria(): 
    x = random.randint(0, WINDOWS_WIDTH)
    y = random.randint(0, WINDOWS_HEIGHT)

    return x // BLOCK + BLOCK, y 

def game_over():
    pygame.quit()
    quit()

pygame.init ()
window = pygame.display.set_mode((WINDOWS_HEIGHT, WINDOWS_WIDTH))

cobra_pos = [(POS_INICIAL_X, POS_INICIAL_Y)]
cobra_surface = pygame.Surface ((BLOCK,BLOCK))
cobra_surface.fill((68,189,50))
direcao = K_LEFT

maca_surface = pygame.Surface((BLOCK,BLOCK))
maca_surface.fill((255,0,0))
maca_pos = gera_pos_aleatoria()

clock = pygame.time.Clock()

while True: 
    clock.tick(10)
    window.fill((0,0,0))
    
    for event in pygame.event.get(): 
        if event.type == QUIT:
            pygame.quit()
            quit()

        elif event.type == KEYDOWN:
            if event.key in [K_UP, K_DOWN, K_LEFT, K_RIGHT]:
                direcao = event.key

    window.blit(maca_surface,maca_pos)


    for pos in cobra_pos: 
        window.blit(cobra_surface,pos)

    if direcao == K_RIGHT: 
        cobra_pos[0] = cobra_pos[0][0] + BLOCK, cobra_pos[0][1]
        
    elif direcao == K_LEFT: 
        cobra_pos[0] = cobra_pos[0][0] - BLOCK, cobra_pos[0][1]

    elif direcao == K_UP: 
        cobra_pos[0] = cobra_pos[0][0], cobra_pos[0][1] - BLOCK
   
    elif direcao == K_DOWN: 
        cobra_pos[0] = cobra_pos[0][0], cobra_pos[0][1] + BLOCK

# cobra_pos[0] = cobra_pos[0][0] + BLOCK, cobra_pos[0][1] isso ta muito feio eu vou me matar
#lembra cabaço que se tu soma vai pra direita se subtrai tu vai pra esquerda no pos[0][0]
#se é pra ir pra cima ou baixo é o mesmo conceito só que no pos[0][1]
    pygame.display.update()