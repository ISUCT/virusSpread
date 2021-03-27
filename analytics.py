import pprint
import pygame
import matplotlib.pyplot as plt
import matplotlib.backends.backend_agg as agg

class GameAnalytics():
    def __init__(self, p_count, tick_rate):
        self.people_count = p_count  ## overall people count
        self.sick_people_count = 0
        self.cured_people_count = 0
        self.current_frame = int()
        self.tick_rate = tick_rate
        self.stats = dict()
        self.sick_stats = []
        self.cured_stats = []
        self.seconds = []
        
        self.figure, self.axs = plt.subplots(2)
    
    def update_stats(self):
        self.stats.update({self.current_frame: {"People count": self.people_count,
                                           "Sick": self.sick_people_count,
                                           "Cured": self.cured_people_count}})
        self.seconds.append(self.current_frame * (10/ self.tick_rate))
        self.sick_stats.append(self.sick_people_count)
        self.cured_stats.append(self.cured_people_count)
    
    def print_stats(self):
        pp = pprint.PrettyPrinter(indent=4)
        pp.pprint(self.stats)
    
    def update_sick_people(self, value):
        self.sick_people_count += value
    
    def update_cured_people(self, value):
        self.cured_people_count += value

    def plot_data(self):
        
        self.figure.suptitle("Game summary")
        self.axs[0].plot(self.seconds, self.sick_stats)
        self.axs[0].set_ylabel("Sick people")
        self.axs[0].set_xlabel("Time (s)")
        self.axs[0].grid()
        self.axs[1].plot(self.seconds, self.cured_stats)
        self.axs[1].set_ylabel("Cured people")
        self.axs[1].set_xlabel("Time (s)")
        self.axs[1].grid()

        canvas = agg.FigureCanvasAgg(self.figure)
        canvas.draw()
        renderer = canvas.get_renderer()
        raw_data = renderer.tostring_rgb()
        size = canvas.get_width_height()
        
        return pygame.image.fromstring(raw_data, size, "RGB")
        ##plt.show()