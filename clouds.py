from utils import randbool


class Clouds:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.cells = [[0 for _ in range(width)] for _ in range(height)]

    def update(self, cutoff_clouds=2, max_random_range_clouds=10, cutoff_lightning=1, max_random_range_lightning=10):
        for row_index in range(self.height):
            for cell_index in range(self.width):
                if randbool(cutoff_clouds, max_random_range_clouds):
                    self.cells[row_index][cell_index] = 1
                    if randbool(cutoff_lightning, max_random_range_lightning):
                        self.cells[row_index][cell_index] = 2
                else:
                    self.cells[row_index][cell_index] = 0

    def export_data(self):
        return {
            'cells': self.cells,
        }

    def import_date(self, data):
        self.cells = data['cells'] or [[0 for _ in range(self.width)] for _ in range(self.height)]
