import pygame
import settings
import random
import math

class Person():
    __radius = 10
    __infection_r = 25
    __inf_width = 1
    __heal_time = 5000
    # __v = (10,-50)
    # __g = (0, -10)
    def __init__(self, surface, is_sick=False, x=random.randint(0,100), y=random.randint(0,100)):
        self.__is_sick = is_sick
        self.is_cured = False
        self.surface = surface
        self.color = settings.BLUE
        # self.isJumping = False
        self.x_pos = x
        self.y_pos = y
        self.sickTime = 0
        if is_sick:    
            self.person_sick()
        self.rect = pygame.draw.circle(self.surface, 
                        self.color,
                        (self.x_pos, self.y_pos),
                        self.__radius)

    def get_rect(self):
        return self.rect

    def clicked(self, pos):
        if self.rect.collidepoint(pos) and not self.is_cured:
            self.person_cure()

    def move(self, v):
        self.rect.move_ip(v)
        pass

    def random_move(self):
        self.rect.move_ip((random.randint(-5,5),random.randint(-5,5)))
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.right > self.surface.get_width():
            self.rect.right = self.surface.get_width()
        if self.rect.bottom > self.surface.get_height():
            self.rect.bottom = self.surface.get_height()

        

    def draw(self):
        # if self.isJumping:
        #     self.jumpSequence()
        self.rect = pygame.draw.circle(self.surface, self.color, self.rect.center, self.__radius)
        if self.__is_sick:
            self.rect = pygame.draw.circle(self.surface, self.color, self.rect.center, self.__infection_r, self.__inf_width)
            if self.sickTime and pygame.time.get_ticks() - self.sickTime > self.__heal_time:
                self.person_cure()

    

    # def jump(self):
    #     self.isJumping = True
    
    # def jumpSequence(self):
    #     if self.rect.y + 2*self.__radius + self.__v[1] > self.surface.get_height()-100:
    #         self.isJumping = False
    #         return
    #     self.move(self.__v)
    #     self.__v = (self.__v[0] - self.__g[0],
    #      self.__v[1] - self.__g[1])
    #     pass

    def person_sick(self):
        self.__is_sick = True
        self.is_cured = False
        self.color = settings.RED
        self.sickTime = pygame.time.get_ticks()

    def person_cure(self):
        self.__is_sick = False
        self.is_cured = True
        self.color = settings.GREEN
        print("Person is cured")
    
    def check_collisions(self, persons):
        indexies = self.rect.collidelistall(persons)
        for i in indexies:
            person = persons[i]
            x = self.rect.centerx - person.rect.centerx
            y = self.rect.centery - person.rect.centery
            distance = math.sqrt(x**2+y**2)
            if distance < self.__radius + self.__infection_r   \
                and person.__is_sick and not self.is_cured and not self.__is_sick:
                # if random.randint(0, 100) <= 80: ## Currently there's 6% change to catch COVID while outdoors
                self.person_sick()
                    
    
    def move_out_wall(self, rect):
        self.color = settings.GREEN
        if self.rect.right > rect.left:
            self.rect.right = rect.left
        if self.rect.bottom > rect.top:
            self.rect.bottom = rect.top
        if self.rect.top > rect.bottom:
            self.rect.top = rect.bottom
        if self.rect.left > rect.right:
            self.rect.left = rect.right
        