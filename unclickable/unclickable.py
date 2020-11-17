import pygame

# constanten
#   instellingen van het programma die we makkelijk willen kunnen veranderen

# constanten_window
window_breedte = 800
window_hoogte = 600
window_achtergrondkleur = (0, 0, 25)
# constanten_plaatje
plaatje_links = 100
plaatje_boven = 100
plaatje_breedte = 100
plaatje_hoogte = 100
plaatje_achtergrondkleur = (255, 50, 0)

pygame.init()
screen = pygame.display.set_mode( [window_breedte,window_hoogte] ) 
clock = pygame.time.Clock()

draait = True
op_vakje = False

while draait == True:
    # ontvang invoer
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            draait = False

    # zoek de positie van de muis
    pos = pygame.mouse.get_pos()
    if pos[0] >= plaatje_links and pos[0] <= plaatje_links + plaatje_breedte and pos[1] >= plaatje_boven and pos[1] <= plaatje_boven + plaatje_hoogte:
        op_vakje = True
    else:
        op_vakje = False

    # laat het vakje de muis ontwijken  
    if op_vakje == True:
        dx = (pos[0] - plaatje_links)/plaatje_breedte - .5
        dy = (pos[1] - plaatje_boven)/plaatje_hoogte - .5
        plaatje_links -= int(dx*10)
        plaatje_boven -= int(dy*10)

    # teken het speelbord
    screen.fill( window_achtergrondkleur )
    # teken het plaatje
    pygame.draw.rect(screen, plaatje_achtergrondkleur,
        [plaatje_links,
        plaatje_boven,
        plaatje_breedte,
        plaatje_hoogte] )
    
    clock.tick(60)
    pygame.display.flip()
    
    
pygame.quit()


