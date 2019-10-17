from htmloutput import HtmlOutput
import random
from square import Square

print_delay = 5
cant_generations_per_image = 50
mutate_probability = 5


class Genetic:

    def __init__(self, sectors, image_count):
        self._sectors = sectors
        self._html_output = HtmlOutput()
        self._image_count = image_count
        
    @staticmethod
    def pick_random_parent(data_to_reproduce):
        random_index = random.randint(0, len(data_to_reproduce) - 1)
        first_parent = data_to_reproduce[random_index]
        data_to_reproduce.pop(random_index)
        return first_parent

    @staticmethod
    def reproduce_parents(color_dict, first_parent, second_parent, sector):
        for _ in range(0, 4):
            child = first_parent["square"].reproduce_with(second_parent["square"])

            if random.randint(0, 100) < mutate_probability:
                child.mutate()

            for key, color in color_dict.items():
                if color.matches_genes(child.genes):
                    color.increase_square_count()
                    break

            sector.add_to_last_generation(child)

        def run(self):
            for imageIndex in range(0, self._image_count):
                for generationIndex in range(0, cant_generations_per_image):

                    if generationIndex % print_delay == 0:
                        self._html_output.new_generation()

                    for sector in self._sectors:
                        self.calculate_next_generation(sector, imageIndex)

                    if generationIndex % print_delay == 0:
                        for sector in self._sectors:
                            self._html_output.add_in_generation(sector)

            self._html_output.write()