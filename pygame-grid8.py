import pygame

rood = (255, 0, 0)
zwart = (0, 0, 0)

hoogte = 300
breedte = 400

pygame.init()
screen = pygame.display.set_mode([breedte, hoogte])
clock = pygame.time.Clock()

running = True
drawing = False
vorige_muis = None


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
#            print("mouseclick(", pos, ")")
            drawing = True
            vorige_muis = pos
        elif event.type == pygame.MOUSEMOTION:
            if drawing == True:
                pos = pygame.mouse.get_pos()
#                pygame.draw.circle(screen, rood, pos, 2)
#                pygame.draw.line(screen, rood, vorige_muis, pos, 2)
                pygame.draw.aaline(screen, rood, vorige_muis, pos, 5)
                vorige_muis = pos
        elif event.type == pygame.MOUSEBUTTONUP:
            drawing = False
 
    clock.tick(60)
    pygame.display.flip()
 
pygame.quit()
