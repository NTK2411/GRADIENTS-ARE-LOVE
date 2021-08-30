import time
import sys
import pygame

clock =  pygame.time.Clock()

pygame.init()
WIDTH = 1280
HEIGHT = 720

screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("I lob Gradients")

def hex_to_rgb(value):
    value = value.lstrip('#')
    lv = len(value)
    return tuple(int(value[i:i + lv // 3], 16) for i in range(0, lv, lv // 3))

def grad2color(chex1,chex2):
    c1 = hex_to_rgb(chex1)
    c2 = hex_to_rgb(chex2)
    c_mix_dif = [0,0,0]
    for i in range(3):
        c_mix_dif[i] = c2[i] - c1[i]
    for x in range(WIDTH):
        c_mix = [0,0,0]
        for i in range(3):
            c_mix[i] = c1[i] + (x * c_mix_dif[i])//WIDTH
        pygame.draw.line(screen,c_mix,(x,0),(x,720),1)

cstart = '0061ff'
cend = '60efff'

while True:
    screen.fill((255,55,255))
    grad2color(cstart,cend)
    # screen.blit(screen)

    #buttons
    # clicking = False
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()


    #showing screen
    pygame.display.update()
    clock.tick() #easy 144 fps
    print(int(clock.get_fps()))

# time.sleep(10000)

