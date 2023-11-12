import argparse
import signal
import sys

import fileinput

signal.signal(signal.SIGINT, lambda signal, frame: print("") or sys.exit(0))

def args_handler():
    parser = argparse.ArgumentParser(prog='CCCAT', description='Reads files sequentially, writing them to the standard output.')
    parser.add_argument('-n', action='store_true', help='Show number line')
    parser.add_argument('filename', nargs="*", help='File to be read. A single dash (\'-\') or absent, reads from the standard input.')

    try:
        namespace = parser.parse_args()
        return namespace
    except argparse.ArgumentError:
        print("Catching an argumentError")
        exit(1)


args = args_handler();
files = args.filename
op_number = args.n

line_index = 0
for line in fileinput.input(files):
    line_index += 1
    line_num = (str(line_index) + " ") if op_number else ""
    text = line.rstrip()
    print(f'{line_num}{text}')

sys.exit(0)
