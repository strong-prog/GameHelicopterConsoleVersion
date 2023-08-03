from utils import randcell


class Helicopter:

    def __init__(self, width, height):
        random_cell = randcell(width, height)
        rand_coordinate_x, rand_coordinate_y = random_cell[0], random_cell[1]
        self.height = height
        self.width = width
        self.coordinate_x = rand_coordinate_x
        self.coordinate_y = rand_coordinate_y
        self.tank = 0
        self.mxtank = 1
        self.score = 0
        self.lives = 20
        self.TREE_BONUS = 100
        self.UPGRADE_COST = 500
        self.LIVE_COST = 1000

    def process_helicopter(self, field, clouds):
        cell_field = field.cells[self.coordinate_x][self.coordinate_y]
        cell_clouds = clouds.cells[self.coordinate_x][self.coordinate_y]
        if cell_field == 2:
            self.tank = self.mxtank
        if cell_field == 5 and self.tank > 0:
            self.tank -= 1
            self.score += self.TREE_BONUS
            field.cells[self.coordinate_x][self.coordinate_y] = 1
        if cell_field == 4 and self.score >= self.UPGRADE_COST:
            self.mxtank += 1
            self.score -= self.UPGRADE_COST
        if cell_field == 3 and self.score >= self.LIVE_COST:
            self.lives += 10
            self.score -= self.LIVE_COST
        if cell_clouds == 2:
            self.lives -= 1
            if self.lives == 0:
                field.game_over(self.score)

    def move(self, move_x, move_y):
        new_coordinate_x, new_coordinate_y = move_x + self.coordinate_x, move_y + self.coordinate_y
        if 0 <= new_coordinate_x < self.height and 0 <= new_coordinate_y < self.width:
            self.coordinate_x, self.coordinate_y = new_coordinate_x, new_coordinate_y

    def export_data(self):
        return {
            'score': self.score,
            'lives': self.lives,
            'x': self.coordinate_x, 'y': self.coordinate_y,
            'tank': self.tank,
            'mxtank': self.mxtank,
        }

    def import_date(self, data):
        self.coordinate_y = data['x'] or 0
        self.coordinate_y = data['y'] or 0
        self.tank = data['tank'] or 0
        self.mxtank = data['mxtank'] or 1
        self.lives = data['lives'] or 20
        self.score = data['score'] or 0
