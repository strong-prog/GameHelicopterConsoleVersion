from random import randint as rand


# Проверка границы.
def check_bounds(coordinate_x, coordinate_y, width, height):
    if coordinate_x < 0 or coordinate_y < 0 or coordinate_x >= width or coordinate_y >= height:
        return False
    return True


# Генератор вероятности.
# cutoff - отсечка, max_random_range - максимальный диапазон рандома.
def randbool(cutoff, max_random_range):
    num = rand(0, max_random_range)
    return num <= cutoff


# Рандомный выбор координата.
def randcell(width, height):
    coordinate_x = rand(0, width - 1)
    coordinate_y = rand(0, height - 1)
    return coordinate_x, coordinate_y


# Следующий координат с рандомным направлением.
# 0 - наверх, 1 - направо, 2 - вниз, 3 - налево
def next_randcell(coordinate_x, coordinate_y):
    moves = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    direction_move = rand(0, 3)
    move_coordinate_x, move_coordinate_y = moves[direction_move][0], moves[direction_move][1]
    return coordinate_x + move_coordinate_x, coordinate_y + move_coordinate_y
