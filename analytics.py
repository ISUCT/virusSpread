import pprint
import matplotlib.pyplot as plt

class GameAnalytics():
    def __init__(self, p_count, tick_rate):
        self.people_count = p_count  ## overall people count
        self.sick_people_count = 0
        self.cured_people_count = 0
        self.current_frame = int()
        self.tick_rate = tick_rate
        self.stats = dict()
    
    def update_stats(self):
        self.stats.update({self.current_frame: {"People count": self.people_count,
                                           "Sick": self.sick_people_count,
                                           "Cured": self.cured_people_count}})
    
    def print_stats(self):
        pp = pprint.PrettyPrinter(indent=4)
        pp.pprint(self.stats)
    
    def update_sick_people(self, value):
        self.sick_people_count += value
    
    def update_cured_people(self, value):
        self.cured_people_count += value
    
    def plot_data(self):
        self.sick_stats = []
        self.cured_stats = []
        self.seconds = [key * (1 / self.tick_rate) for key in self.stats.keys()]
        for item in self.stats:
            self.sick_stats.append(self.stats[item]["Sick"])
            self.cured_stats.append(self.stats[item]["Cured"])

        fig, axs = plt.subplots(2)
        fig.suptitle("Game summary")
        axs[0].plot(self.seconds, self.sick_stats)
        axs[0].set_ylabel("Sick people")
        axs[0].set_xlabel("Time (s)")
        axs[0].grid()
        axs[1].plot(self.seconds, self.cured_stats)
        axs[1].set_ylabel("Cured people")
        axs[1].set_xlabel("Time (s)")
        axs[1].grid()
        plt.show()