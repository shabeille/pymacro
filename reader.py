from time import sleep
from pathlib import Path
import pyautogui as macro


macro.PAUSE = 0 # pyautogui by default has this set to 0.1; this creates timing inaccuracies / delay with our program


def read_key_action(list_of_keys, press_type) -> None:
    for key in list_of_keys.split('+'):
        if press_type == 'down' or press_type == 'press':
            print(f'Pressing {key}')
            macro.keyDown(key)

        elif press_type == 'up':
            print(f'Releasing {key}')
            macro.keyUp(key)


class Reader:
    def __init__(self, file_path: str|Path):
        with open(file_path) as f:
            self.instructions = f.readlines()

    def read_file_instructions(self, pause: float = None) -> None:
        if not (pause is None or pause <= 0):
            print(f'Pausing for {pause} seconds')
            sleep(pause)

        print('Reading...\n')

        for instruction in self.instructions:
            if instruction.strip() == '' or instruction.strip()[0] == '#':
                continue

            keys, action, duration = instruction.split(' ')

            read_key_action(keys, action)

            sleep(float(duration) / 1000) # the file is expected to give time in milliseconds. time.sleep expects seconds

            if action == 'press':
                read_key_action(keys, 'up')



    


