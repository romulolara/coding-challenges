import argparse
import signal
import sys

import fileinput

signal.signal(signal.SIGINT, lambda signal, frame: print("") or sys.exit(0))

def args_handler():
    parser = argparse.ArgumentParser(prog='CCCAT', description='Reads files sequentially, writing them to the standard output.')
    parser.add_argument('-n', action='store_true', help='Show number line')
    parser.add_argument('-b', action='store_true', help='Show number only for not blank line')
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
op_number_not_blank = args.b

line_index = 0
for line in fileinput.input(files):
    line_num = ""
    text = line.rstrip()
    if op_number or (op_number_not_blank and len(text) > 0):
        line_index += 1
        line_num = (str(line_index) + " ")

    print(f'{line_num}{text}')

sys.exit(0)
