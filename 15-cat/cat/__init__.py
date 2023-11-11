import argparse
import signal
import sys

import fileinput

signal.signal(signal.SIGINT, lambda signal, frame: print("") or sys.exit(0))

def args_handler():
    parser = argparse.ArgumentParser(prog='CCCAT', description='Reads files sequentially, writing them to the standard output.')
    parser.add_argument('filename', nargs="*", help='File to be read. A single dash (\'-\') or absent, reads from the standard input.')

    try:
        namespace = parser.parse_args()
        return namespace
    except argparse.ArgumentError:
        print("Catching an argumentError")
        exit(1)


args = args_handler();

for line in fileinput.input(args.filename):
    print(line.rstrip())

sys.exit(0)
