import pygame
import settings
from person import Person

conf = settings.AppSettings()

clock = pygame.time.Clock()
pygame.init()

screen = pygame.display.set_mode((conf.scr_width, conf.scr_height))
pygame.display.set_caption(conf.title)
surface = pygame.Surface(screen.get_size())
surface.fill(conf.bg_color)
p1 = Person(screen, surface)
screen.blit(surface, (0,0))

mainloop = True

dir = {pygame.K_LEFT: (-5, 0), 
        pygame.K_RIGHT: (5, 0), 
        pygame.K_UP: (0, -5),
        pygame.K_DOWN: (0, 5)}

while mainloop:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print("QUIT")
            mainloop = False
        if event.type == pygame.KEYDOWN:
            if event.key in dir:
                v = dir[event.key]
                p1.move(v)
            if event.key ==pygame.K_SPACE:
                print("Space")
                p1.jump()
    p1.draw()
    pygame.display.flip()
    # pygame.display.update()
    clock.tick(60)

pygame.quit()
