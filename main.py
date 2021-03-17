import pygame
import settings
import random

from person import Person

conf = settings.AppSettings()

clock = pygame.time.Clock()
pygame.init()

screen = pygame.display.set_mode((conf.scr_width, conf.scr_height))
pygame.display.set_caption(conf.title)

surface = pygame.Surface(screen.get_size())
surface.fill(conf.bg_color)

p1 = Person(surface, True, x=200, y=200)
p2 = Person(surface, x=250, y=250)

persons = [p1, p2, Person(surface, x=110, y=110)]
for i in range(10):
    persons.append(Person(surface, x=random.randint(0, conf.scr_width) ,y=random.randint(0,conf.scr_height)))

screen.blit(surface, (0,0))

mainloop = True

dir = {pygame.K_LEFT: (-5, 0), 
        pygame.K_RIGHT: (5, 0), 
        pygame.K_UP: (0, -5),
        pygame.K_DOWN: (0, 5)}

start = (0, 0)
size = (0, 0)
drawing = False

while mainloop:
    surface.fill(conf.bg_color)
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
                # p1.jump()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            for person in persons:
                person.clicked(event.pos)
            start = event.pos
            size = 0, 0
            drawing = True
        elif event.type == pygame.MOUSEBUTTONUP:
            end = event.pos
            size = end[0] - start[0], end[1] - start[1]
            drawing = False
        elif event.type == pygame.MOUSEMOTION and drawing:
            end = event.pos
            size = end[0] - start[0], end[1] - start[1]

    
    for person in persons:
        coll = person.rect.collidelist(persons)
        print(coll)
        person.check_collisions(persons)
        person.random_move()
        person.draw()
    screen.blit(surface, (0,0))
    
    pygame.draw.rect(screen, settings.RED, (start, size))
    # pygame.display.update()

    pygame.display.flip()
    clock.tick(10)

pygame.quit()
