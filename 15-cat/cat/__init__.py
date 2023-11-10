import argparse
import signal
import sys

import fileinput

signal.signal(signal.SIGINT, lambda signal, frame: print("") or sys.exit(0))

def args_handler():
    parser = argparse.ArgumentParser(description='Reads files sequentially, writing them to the standard output.')
    parser.add_argument('filename', nargs="?", help='Files to be read.')

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


args = args_handler();

if args.filename:
    file_handler(args.filename)


sys.exit(0)
