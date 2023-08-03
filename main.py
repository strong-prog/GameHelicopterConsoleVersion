from map import Map
from helicopter import Helicopter
from clouds import Clouds
from pynput import keyboard
import time
import os
import json


# Обработка нажатия клавиш.
def process_key(key):
    global helico, tick, clouds, field
    button = key.char.lower()

    # Движение вертолета.
    if button in MOVES.keys():
        move_x, move_y = MOVES[button][0], MOVES[button][1]
        helico.move(move_x, move_y)
    # Сохранение игры.
    elif button == 'f':
        data = {
            'helicopter': helico.export_data(),
            'clouds': clouds.export_data(),
            'field': field.export_data(),
            'tick': tick,
        }
        with open('level.json', 'w') as lvl:
            json.dump(data, lvl)
    # Загрузка игры.
    elif button == 'g':
        with open('level.json', 'r') as lvl:
            data = json.load(lvl)
            tick = data['tick'] or 1
            helico.import_date(data['helicopter'])
            field.import_date(data['field'])
            clouds.import_date(data['clouds'])


listener = keyboard.Listener(
    on_press=None,
    on_release=process_key)
listener.start()


MOVES = {'w': (-1, 0), 'd': (0, 1), 's': (1, 0), 'a': (0, -1)}
MAP_WIDTH, MAP_HEIGHT = 15, 15
TICK_SLEEP = 0.05
TREE_UPDATE = 500
CLOUDS_UPDATE = 250
FIRE_UPDATE = 100

field = Map(MAP_WIDTH, MAP_HEIGHT)
clouds = Clouds(MAP_WIDTH, MAP_HEIGHT)
helico = Helicopter(MAP_WIDTH, MAP_HEIGHT)
tick = 1

while True:
    os.system('clear')
    field.print_stats(helico)
    field.print_map(helico, clouds)
    helico.process_helicopter(field, clouds)

    if tick % TREE_UPDATE == 0:
        field.generate_tree()
    if tick % FIRE_UPDATE == 0:
        field.update_fires()
    if tick % CLOUDS_UPDATE == 0:
        clouds.update()

    print('F - сохранить. G - загрузить.')
    tick += 1
    time.sleep(TICK_SLEEP)

