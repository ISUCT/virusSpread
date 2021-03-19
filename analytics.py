import pprint

class GameAnalytics():
    def __init__(self, p_count):
        self.people_count = p_count  ## overall people count
        self.sick_people_count = 0
        self.cured_people_count = 0
        self.current_frame = int()
        self.stats = dict()
    
    def update_stats(self):
        self.stats.update({self.current_frame: {"People count": self.people_count,
                                           "Sick": self.sick_people_count,
                                           "Cured": self.cured_people_count}})
        # [self.sick_people_count, self.cured_people_count, self.people_count]
    
    def print_stats(self):
        pp = pprint.PrettyPrinter(indent=4)
        pp.pprint(self.stats)