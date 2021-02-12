import pygame
import settings
import random

class Person():
    __radius = 10
    __v = (10,-50)
    __g = (0, -10)
    def __init__(self, surface):
        self.surface = surface
        self.color = settings.BLUE
        self.isJumping = False
        self.rect = pygame.draw.circle(self.surface, 
                        self.color,
                        (100, 100),
                        self.__radius)

    def get_rect(self):
        return self.rect

    def clicked(self, pos):
        if self.rect.collidepoint(pos):
            self.color = settings.RED

    def move(self, v):
        self.rect.move_ip(v)
        pass

    def random_move(self):
        self.rect.move_ip((random.randint(-1,1),random.randint(-1,1)))

    def draw(self):
        if self.isJumping:
            self.jumpSequence()
        pygame.draw.circle(self.surface, self.color, self.rect.center, self.__radius)
    

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
        