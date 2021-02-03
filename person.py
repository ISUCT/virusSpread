import pygame
import settings

class Person():
    __radius = 10
    __v = (10,-50)
    __g = (0, -10)
    def __init__(self, screen, surface):
        self.surface = surface
        self.screen = screen 
        self.color = settings.BLUE
        self.isJumping = False
        self.rect = pygame.draw.circle(self.surface, 
                        self.color,
                        (100, 100),
                        self.__radius)
    
    def move(self, v):
        self.rect.move_ip(v)
        print(self.rect)
        pass

    def draw(self):
        self.screen.blit(self.surface, self.rect)
        if self.isJumping:
            self.jumpSequence()
    
    def jump(self):
        self.isJumping = True
    
    def jumpSequence(self):
        if self.rect.y + 2*self.__radius + self.__v[1] > self.surface.get_height()-100:
            self.isJumping = False
            return
        self.move(self.__v)
        self.__v = (self.__v[0] - self.__g[0],
         self.__v[1] - self.__g[1])
        pass
        