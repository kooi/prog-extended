import pygame
import math

pygame.init()

screen = pygame.display.set_mode([400,300])
pygame.display.set_caption("")
 
done = False
clock = pygame.time.Clock()

while not done:
    screen.fill( (0, 0, 0) )
    clock.tick(60)
    pygame.display.flip()
 
pygame.quit()
