import pygame

pygame.init()
screen = pygame.display.set_mode((640,480))
background = pygame.Surface(screen.get_size())
background.fill((255, 200, 200)) # R G B
pygame.display.set_caption("VirusTracking")
screen.blit(background,(0,0))

mainloop = True

while mainloop:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print("QUIT")
            mainloop = False
    pygame.display.flip()

pygame.quit()
