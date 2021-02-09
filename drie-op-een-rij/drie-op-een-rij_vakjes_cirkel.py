import pygame

# constanten
#   instellingen van het programma die we makkelijk willen kunnen veranderen

# constanten_window
window_breedte = 800
window_hoogte = 600
window_achtergrondkleur = (0, 0, 25)
# constanten_vakje
vakje_breedte = 100
vakje_hoogte = 100
vakje_achtergrondkleur = (0, 50, 0)
vakje_Xkleur = (255, 255, 255)
vakje_Okleur = (0, 50, 255)
# constanten_speelveld
speelveld_marge_links = 100
speelveld_marge_boven = 100
speelveld_breedte = 300 # = vakje_breedte * 3
speelveld_hoogte = 300 # = vakje_hoogte * 3


speelveld = [ ["", "", ""],
              ["", "O", ""],
              ["", "", ""] ]



pygame.init()
screen = pygame.display.set_mode( [window_breedte,window_hoogte] ) 
clock = pygame.time.Clock()

draait = True

while draait == True:
    # ontvang invoer
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            draait = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            #print("mouseclick(", pos, ")")
            # controleer of click binnen het speelveld is
            # speelveld_marge_links < x < speelveld_marge_links + speelveld_breedte
            if pos[0] >= speelveld_marge_links and pos[0] <= speelveld_marge_links + speelveld_breedte:
                if pos[1] >= speelveld_marge_boven and pos[1] <= speelveld_marge_boven + speelveld_hoogte:
                    # uitrekenen op welk vakje we geklikt hebben
                    i = int(3*(pos[0] - speelveld_marge_links)/speelveld_breedte)
                    j = int(3*(pos[1] - speelveld_marge_boven)/speelveld_hoogte)
                    print(i,j)
                    speelveld[j][i] = "X"

    # teken het speelbord
    screen.fill( window_achtergrondkleur )
    # teken de vakjes
    for j in [0, 1, 2]:
        for i in [0, 1, 2]:
            # kijk naar wat er in onze speelveld-lijst staat
            # als "X" -> blauw-tekenen
            # als "O" -> rood-tekenen
            # als "" -> x-tekenen
            if speelveld[j][i] == "":
                pygame.draw.rect(screen, vakje_achtergrondkleur,
                    [speelveld_marge_links + i*vakje_breedte,
                     speelveld_marge_boven + j*vakje_hoogte,
                     vakje_breedte - 10,
                     vakje_hoogte - 10] )
            elif speelveld[j][i] == "X":
                pygame.draw.rect(screen, vakje_Xkleur,
                    [speelveld_marge_links + i*vakje_breedte,
                     speelveld_marge_boven + j*vakje_hoogte,
                     vakje_breedte - 10,
                     vakje_hoogte - 10] )
            elif speelveld[j][i] == "O":
#                pygame.draw.rect(screen, vakje_Okleur,
#                    [speelveld_marge_links + i*vakje_breedte,
#                     speelveld_marge_boven + j*vakje_hoogte,
#                     vakje_breedte - 10,
#                     vakje_hoogte - 10] )
                pygame.draw.circle(
                        screen,
                        vakje_Okleur,
                        [int(speelveld_marge_links + (i+.5)*vakje_breedte), # x
                         int(speelveld_marge_boven + (j+.5)*vakje_hoogte)], # y
                        int(vakje_hoogte *.5) # straal
                    )

    
    clock.tick(60)
    pygame.display.flip()
    
    
pygame.quit()




