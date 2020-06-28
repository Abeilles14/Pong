import pygame

pygame.init()

width = 640
height = 480

screen = pygame.display.set_mode((width, height))
texture = pygame.image.load("chibi_willem.png")

posX = 0
posY = 0

velX = 0.05
velY = 0.05

gameover = False

while not gameover:
    # list of all events
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            gameover = True;
    posX += velX
    posY += velY

    if posX < 0 or posX > width - texture.get_rect().width:
        velX = -velX
    if posY < 0 or posY > height - texture.get_rect().height:
        velY = -velY

    screen.fill((255, 255, 255))
    screen.blit(texture, (round(posX), round(posY)))
    # flip buffers, bring buffer to the front
    pygame.display.flip()

pygame.quit()
