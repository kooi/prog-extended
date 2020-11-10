import pygame

pygame.init()
screen = pygame.display.set_mode( [640,360] ) 
clock = pygame.time.Clock()

draait = True

while draait == True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            draait = False

    screen.fill( (0, 0, 0) )
    clock.tick(60)
    pygame.display.flip()
    
    
pygame.quit()
