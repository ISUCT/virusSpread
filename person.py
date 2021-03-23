import pygame
import settings
import random
conf = settings.AppSettings()
import math

class Person():
    __radius = 10
    __infection_r = 25
    __inf_width = 1
    __heal_time = 5000
    __spd = 8
    __inf_prob = 8
    # __v = (10,-50)
    # __g = (0, -10)
    def __init__(self, surface, is_sick=False, x=random.randint(0,100), y=random.randint(0,100), game_state=None):
        self.game_state = game_state
        self.__is_sick = self.handle_sickness_init(is_sick)
        # else: self.is_sick = False
        self.is_cured = False
        self.surface = surface
        self.color = settings.BLUE
        # self.isJumping = False
        self.targetReached = True
        self.x_pos = x
        self.y_pos = y
        self.sickTime = 0
        if self.__is_sick:    
            self.person_sick()
        self.rect = pygame.draw.circle(self.surface, 
                        self.color,
                        (x, y),
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
        if self.targetReached:
            self.targetPoint = (random.randint(0+2*self.__radius, self.surface.get_width()-2*self.__radius),
            random.randint(0+2*self.__radius, self.surface.get_height()-2*self.__radius))
            self.targetReached = False
        self.targetVector = (self.targetPoint[0] - self.rect.centerx, self.targetPoint[1] - self.rect.centery)
        targetVectorLen = (self.targetVector[0]**2 + self.targetVector[1]**2)**(1/2.0)
        self.targetVector = (self.targetVector[0]/targetVectorLen*self.__spd, 
            self.targetVector[1]/targetVectorLen*self.__spd)
        
        if targetVectorLen <= self.__radius:
            self.targetReached = True
        self.rect.move_ip(self.targetVector)
        
        # These checks are rudundant
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.right > self.surface.get_width():
            self.rect.right = self.surface.get_width()
        if self.rect.bottom > self.surface.get_height():
            self.rect.bottom = self.surface.get_height()

    def handle_sickness_init(self, sickness_status):
        if sickness_status:
            self.game_state.analytics.sick_people_count += 1
            self.color = settings.RED
            return sickness_status
        else:
            return sickness_status

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
        self.game_state.analytics.update_sick_people(1)
        self.color = settings.RED
        self.sickTime = pygame.time.get_ticks()

    def person_cure(self):
        self.__is_sick = False
        self.is_cured = True
        self.game_state.analytics.update_sick_people(-1)
        self.game_state.analytics.update_cured_people(1)
        self.color = settings.GREEN
    
    def check_collisions(self, persons):
        indexies = self.rect.collidelistall(persons)
        for i in indexies:
            person = persons[i]
            x = self.rect.centerx - person.rect.centerx
            y = self.rect.centery - person.rect.centery
            distance = math.sqrt(x**2+y**2)
            if distance < self.__radius + self.__infection_r   \
                and person.__is_sick and not self.is_cured and not self.__is_sick:
                if random.randint(0, 100) <= self.__inf_prob: ## Currently there's 6% change to catch COVID while outdoors
                    self.person_sick()
    
    def sign(self, num):
        return -1 if num < 0 else 1
    
    def move_out_wall(self, rect):
        self.targetVector = ((self.targetVector[0] + 10*self.sign(self.targetVector[0]))*-1,
            (self.targetVector[1] + 10*self.sign(self.targetVector[1]))*-1)
        # self.targetPoint = (self.rect.centerx+self.targetVector[0], self.rect.centery+self.targetVector[1])
        self.targetReached = True
        self.rect.move_ip(self.targetVector)