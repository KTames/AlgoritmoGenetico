#!encoding=utf-8
from sector import Sector


class Probabilistic:

    def __init__(self, images, rows, columns):
        self._images = images
        self._rows = rows
        self._columns = columns

    def _create_sectors(self):

        width_per_sector = self._images[0].width / self._columns
        height_per_sector = self._images[0].height / self._rows

        # Calcula los X y Y de cada sector
        sectors = [
            Sector(
                column,
                row,
                int(width_per_sector * column),
                int(height_per_sector * row),
                int(width_per_sector * (column + 1)),
                int(height_per_sector * (row + 1))
            ) for row in range(0, self._rows)
            for column in range(0, self._columns)
        ]

        return sectors

    @staticmethod
    def _choose_sector(sectors, probabilistic_index):
        index_sector = -1
        length = len(sectors)
        while probabilistic_index >= 0 and index_sector + 1 < length:
            index_sector += 1
            probabilistic_index -= sectors[index_sector].probability
        return index_sector
