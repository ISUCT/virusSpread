import pygame
import settings
import random
from analytics import GameAnalytics

from person import Person

class GameState():
    def __init__(self, settings, analytics):
        self.settings = settings
        self.analytics = analytics


conf = settings.AppSettings()
analytics = GameAnalytics(conf.number_of_people, conf.tick_rate)

clock = pygame.time.Clock()
pygame.init()

game_state = GameState(conf, analytics)
game_state.analytics.current_frame = 0

screen = pygame.display.set_mode((game_state.settings.scr_width, game_state.settings.scr_height))
pygame.display.set_caption(game_state.settings.title)

surface = pygame.Surface(screen.get_size())
surface.fill(game_state.settings.bg_color)

p1 = Person(surface, True, x=200, y=200, game_state=game_state)
p2 = Person(surface, x=250, y=250, game_state=game_state)

persons = [p1, p2, Person(surface, x=110, y=110, game_state=game_state)]
for i in range(game_state.settings.number_of_people):
    persons.append(Person(surface, x=random.randint(0, game_state.settings.scr_width) ,y=random.randint(0,game_state.settings.scr_height), game_state=game_state))

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
    game_state.analytics.current_frame += 1
    surface.fill(game_state.settings.bg_color)
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
            if button.collidepoint(event.pos):
                print ("You press button")
                analytics.print_stats()
                analytics.plot_data()
        elif event.type == pygame.MOUSEBUTTONUP:
            end = event.pos
            size = end[0] - start[0], end[1] - start[1]
            drawing = False
        elif event.type == pygame.MOUSEMOTION and drawing:
            end = event.pos
            size = end[0] - start[0], end[1] - start[1]

    button = pygame.draw.rect(surface, settings.RED, (20, 10, 50, 26))
    font = pygame.font.SysFont(None, 19)
    img = font.render('График', True, settings.BLUE)


    wall = pygame.draw.rect(surface, settings.BLACK, (start, size))
    indexies = wall.collidelistall(persons)
    for i in indexies:
        persons[i].move_out_wall(wall)
    

    for person in persons:
        person.check_collisions(persons)
        person.random_move()
        person.draw()
    screen.blit(surface, (0,0))
    screen.blit(img, (20, 20))


    
    # pygame.display.update()

    pygame.display.flip()
    clock.tick(game_state.settings.tick_rate)
    game_state.analytics.update_stats()


pygame.quit()


