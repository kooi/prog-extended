import pygame

pygame.init()

screen = pygame.display.set_mode([400,300])
pygame.display.set_caption("")
 
done = False
clock = pygame.time.Clock()

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            print("mouseclick(", pos, ")")

    screen.fill( (0, 0, 0) )
    clock.tick(60)
    pygame.display.flip()
 
pygame.quit()
