import pygame


clock = pygame.time.Clock()
pygame.init()
screen = pygame.display.set_mode((640,480))
background = pygame.Surface(screen.get_size())
background.fill((255, 200, 200)) # R G B
pygame.display.set_caption("VirusTracking")



mainloop = True

radius = 30
WIDTH, HEIGHT = screen.get_size()
RED = (255, 0, 0)

x = 0 - radius
y = HEIGHT // 4

field_height = HEIGHT // 2

field = pygame.Surface((WIDTH, field_height))
field.fill((0, 255, 0))

y_field = 0 - field_height

while mainloop:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print("QUIT")
            mainloop = False

    screen.blit(background,(0,0))

    field.fill((0, 255, 0))

    pygame.draw.circle(field, RED, (x, y), radius)
    screen.blit(field,(0, y_field))

    if y_field >= HEIGHT + field_height:
        y_field = 0 - field_height
    else:
        y_field += 1

    if x >= WIDTH + radius:
        # перемещаем его за левую
        x = 0 - radius
    else:  # Если еще нет,
        # на следующей итерации цикла
        # круг отобразится немного правее
        x += 2

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
