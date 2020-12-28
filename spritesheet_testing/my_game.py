import pygame
from player import Player
################################# LOAD UP A BASIC WINDOW AND CLOCK #################################
pygame.init()
DISPLAY_W, DISPLAY_H = 800, 480
canvas = pygame.Surface((DISPLAY_W,DISPLAY_H))
window = pygame.display.set_mode(((DISPLAY_W,DISPLAY_H)))
running = True
clock = pygame.time.Clock()
house = pygame.image.load('backgrounds/living room.png').convert()
################################# LOAD PLAYER ###################################
poke = Player('chikorita')
################################# GAME LOOP ##########################
while running:
    clock.tick(60)
    ################################# CHECK PLAYER INPUT #################################
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                poke.LEFT_KEY, poke.FACING_LEFT = True, True
            elif event.key == pygame.K_RIGHT:
                poke.RIGHT_KEY, poke.FACING_LEFT = True, False
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                poke.LEFT_KEY = False
            elif event.key == pygame.K_RIGHT:
                poke.RIGHT_KEY = False

    ################################# UPDATE/ Animate SPRITE #################################
    poke.update()
    ################################# UPDATE WINDOW AND DISPLAY #################################
    #canvas.fill((255,255,255))
    canvas.blit(house, (0,0))
    poke.draw(canvas)
    window.blit(canvas, (0,0))
    pygame.display.update()









