import argparse
import signal
import sys

def signal_handler(signal, frame):
    print("")
    sys.exit(0)


def args_handler():
    parser = argparse.ArgumentParser(description='Displays the first N lines or bytes of a file.')
    parser.add_argument('filename' , nargs="?", help='file to be read.')
    try:
        namespace = parser.parse_args()
        return namespace
    except argparse.ArgumentError:
        print("Catching an argumentError")
        exit(1)


def no_file_handler():
    for line in range(10):
        text = input()
        print(text)
    sys.exit(0)


def file_handler(filename, lines_to_read = 10):
    file_ref = open(filename, "r")
    lines_read = 0
    for line in file_ref:
        if lines_read >= lines_to_read:
            break
        print(line.rstrip("\n"))
        lines_read += 1
    file_ref.close()
    sys.exit(0)


signal.signal(signal.SIGINT, signal_handler)

args = args_handler();
file_handler(args.filename) if args.filename else no_file_handler()
