import argparse
import reader


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('path', help='The path to the file that should be read')
    parser.add_argument('-p', '--pause', type=float, default=0, help='Duration to pause before beginning file execution')

    args = parser.parse_args()

    file_reader = reader.Reader(args.path)
    file_reader.read_file_instructions(pause=args.pause)

if __name__ == '__main__':
    main()

