import pygame


#inicializace PyGame
pygame.init()

#Nastavení velikosti okna
width, height = 800, 600
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("pygame01hra")




#Hlavní smyčka
running = True
x1, x2 = 50, 50
direction = 1
r = 50
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    window.fill((0, 0, 150))
    x1+=1
    if x1 > width+r:
        x1 = -50
    pygame.draw.circle(window, (55, 255, 25), (x1, 200), 50)
    x2 += .75 * direction
    if x2 < r:
        direction = 1
        
    if x2 > width-r:
        direction = -1

    pygame.draw.circle(window, (255, 55, 25), (x2, 400), 50)
    
    pygame.display.update()


pygame.quit()
