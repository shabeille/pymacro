from time import sleep
from os import listdir, path
from pathlib import Path
import pyautogui as macro


EXTENSION = '.txt'
DIRECTORY = 'macros'


def filter_invalid_files(files: list, target_extension: str, file_directory: str) -> list:

    # ensures we've actually got files
    if len(files) == 0:
        print('No files available to read')
        exit()

    # removes files that do not have the desired extension
    valid_files = []

    for file in files:
        if (Path(file).suffix == target_extension) and (not path.isdir(path.join(file_directory, file))):
            valid_files.append(file)

    return valid_files


def list_readable_files(files: list) -> None:
    print('\nReadable Files:\n---------------')
    
    for index, file in enumerate(files):
        print(f'{index}: "{file}"')


def get_path_from_index(files: list, index: int) -> str:
    file_index = int(index)
    
    if (file_index < 0) or (file_index > len(files) - 1):
        raise IndexError
    else:
        return path.join(DIRECTORY, files[file_index])
    

def get_path_from_string(files: list, file_name: str) -> str:
    if not file_name in files:
        raise FileNotFoundError
    else:
        return path.join(DIRECTORY, file_name)


def get_file(files: list) -> __file__:
    while True:

        print('\nSelect a file from the given list (enter either the index, or the full file name). Enter "list" to view the files again')
        file_selection = input('Selection: ')

        path_to_open = None

        if file_selection == '':
            print('\nInput cannot be empty')
            continue


        elif file_selection == 'list':
            list_readable_files(files)
            continue


        elif file_selection.isdigit():
            try:
                path_to_open = get_path_from_index(files, file_selection)
            except IndexError:
                print('\nIncorrect Index')
                continue

        else:
            try:
                path_to_open = get_path_from_string(files, file_selection)
            except FileNotFoundError:
                print('\nFile not in list')
                continue

        if not input(f'\nUsing "{path_to_open}". Is this corrrect? (y/n) ') == 'y':
            continue

        return open(path_to_open, 'r')
    

def read_key_action(list_of_keys, press_type) -> None:
    for key in list_of_keys.split('+'):

        if press_type == 'down' or press_type == 'press':
            print(f'Pressing {key}')
            macro.keyDown(key)

        elif press_type == 'up':
            print(f'Releasing {key}')
            macro.keyUp(key)


def read_file_instructions(file) -> None:
    instructions = file.readlines()
    print('Reading...\n')

    for instruction in instructions:
        if instruction.strip() == '':
            continue

        keys, action, length = instruction.split(' ')

        read_key_action(keys, action)

        sleep(int(length) / 1000) # the file is expected to give time in milliseconds. time.sleep expects seconds

        if action == 'press':
            read_key_action(keys, 'up')


def main() -> None:

    macro.PAUSE = 0 # pyautogui by default has this set to 0.1; this creates timing inaccuracies / delay with our program

    macro_files = listdir(DIRECTORY)
    macro_file = None

    macro_files = filter_invalid_files(macro_files, EXTENSION, DIRECTORY)
    list_readable_files(macro_files)

    with get_file(macro_files) as macro_file:

        if input('\nWait 5 seconds before reading? (y/n): ') == 'y':
            print('Sleeping...')
            sleep(5)

        read_file_instructions(macro_file)

    print('\n\nReading complete\n\n')



if __name__ == '__main__':
    main()
    


