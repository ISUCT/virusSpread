import pygame

WIN_HEIGHT = 480
WIN_WIDTH = 640
BLACK = (0, 0, 0)

clock = pygame.time.Clock()
pygame.init()

class Rocket:
    __width = 20
    __height = 50
    
    def __init__(self, surface, color):
        self.surface = surface
        self.color = color
        self.x = surface.get_width()//2 - self.__width //2
        self.y = surface.get_height()

        pass

    def fly(self):
        self.rect = pygame.draw.circle(self.surface, 
                        self.color,
                        (self.x, self.y),
                        self.__height)

        pygame.draw.rect(self.surface, 
                        (255,0,0,50),
                        (self.rect.x, self.rect.y,
                        self.rect.width,
                        self.rect.height
                        ),2)
        self.rect.move_ip(0,-3)
        self.y -= 3
        if self.y < -self.__height:
            self.y = WIN_HEIGHT
        # pass

mainloop = True

screen = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))

# background = pygame.Surface(screen.get_size())
# background.fill((255, 200, 200)) # R G B
pygame.display.set_caption("VirusTracking")

rect_left = pygame.Rect(
    (0, 0), (WIN_WIDTH // 2, WIN_HEIGHT))
surf_left = pygame.Surface(
    (rect_left.width, rect_left.height))
surf_left.fill((255,255,255))


screen.blit(surf_left, rect_left)

rocket_left = Rocket(surf_left, BLACK)
pygame.display.update()

while mainloop:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print("QUIT")
            mainloop = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if rocket_left.rect.collidepoint(event.pos):
                print("click in Rocet")

    surf_left.fill((255,255,255))
    rocket_left.fly()
    screen.blit(surf_left, rect_left)
    pygame.display.update(rect_left)

    clock.tick(60)

pygame.quit()
