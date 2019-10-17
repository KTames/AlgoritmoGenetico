#!encoding=utf-8


class Sector:

    def __init__(self, logic_x, logic_y, min_x, min_y, max_x, max_y):
        self.logic_x = logic_x
        self.logic_y = logic_y
        self.min_x = min_x
        self.max_x = max_x
        self.min_y = min_y
        self.max_y = max_y
        self.probability = 10
        self.points = []
        self._colors = get_colors()
        self.generations = [[]]
        self.size = max_x - min_x
        self.square_size = self.size / 2
        self.targets_per_image = []
