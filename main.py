import reader, writer


def main():
    while True:
        print('\nSelect action\n-------------')
        print('1: Read macro file\n2: Write macro file\n3: Exit program')

        selection = input('Selection: ')

        if selection == '1':
            reader.main()

        elif selection == '2':
            writer.main()

        elif selection == '3':
            exit()

        else:
            print('\nInvalid selection.\nEnter the number associated with the action.')


if __name__ == '__main__':
    main()

