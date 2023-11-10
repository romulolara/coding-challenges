import argparse
import signal
import sys

import fileinput

signal.signal(signal.SIGINT, lambda signal, frame: print("") or sys.exit(0))

def args_handler():
    parser = argparse.ArgumentParser(description='Reads files sequentially, writing them to the standard output.')
    parser.add_argument('filename', nargs="?", help='File to be read. A single dash (\'-\') or absent, reads from the standard input.')

    try:
        namespace = parser.parse_args()
        return namespace
    except argparse.ArgumentError:
        print("Catching an argumentError")
        exit(1)


def file_handler(filename):
    try:
        with open(filename) as file_ref:
            print(file_ref.read())
            file_ref.close()
    except FileNotFoundError:
        print(f'cccat: {filename}: No such file or directory.')
    except IsADirectoryError:
        print(f'cccat: {filename}: Is a directory.')


def no_file_handler():
    try:
        for text in fileinput.input():
            print(text.rstrip())
    except FileNotFoundError:
        while True:
            text = input()
            print(text.rstrip())


args = args_handler();
if args.filename and '-' != args.filename:
    file_handler(args.filename)
else:
    no_file_handler()


sys.exit(0)
