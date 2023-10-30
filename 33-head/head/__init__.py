import argparse
import signal
import sys

def signal_handler(signal, frame):
    print("")
    sys.exit(0)


def args_handler():
    parser = argparse.ArgumentParser(description='Displays the first N lines or bytes of a file.')
    parser.add_argument('filename', nargs="*", help='Files to be read.')
    parser.add_argument("-n", nargs="?", help='Number of lines to be read.', required=False, type=int, dest="total_lines", default=10)
    parser.add_argument("-c", nargs="?", help='Number of bytes to be read.', required=False, type=int, dest="total_bytes")
    try:
        namespace = parser.parse_args()
        return namespace
    except argparse.ArgumentError:
        print("Catching an argumentError")
        exit(1)


def no_file_handler(lines_to_read, bytes_to_read):
    while bytes_to_read:
        text = input()
        text_read = text[:bytes_to_read]
        print(text_read)
        bytes_to_read -= len(text_read)

        if bytes_to_read <= 0:
            break;
    else:
        for line in range(lines_to_read):
            text = input()
            print(text)


def file_handler(filename, lines_to_read, bytes_to_read):
    if bytes_to_read:
        file_ref = open(filename, "rb")
        text = file_ref.read(bytes_to_read)
        text = text.decode("utf-8")
        print(text.rstrip("\n"))
        file_ref.close()
    else:
        file_ref = open(filename, "r")
        lines_read = 0
        for line in file_ref:
            if lines_read >= lines_to_read:
                break
            print(line.rstrip("\n"))
            lines_read += 1
        file_ref.close()


def multi_files_handler(files, lines_to_read, bytes_to_read):
    if len(files) > 1:
        for filename in files:
            print(f'==> {filename} <==')
            file_handler(filename, lines_to_read, bytes_to_read)
            print("")
    else:
        file_handler(files[0], lines_to_read, bytes_to_read)


signal.signal(signal.SIGINT, signal_handler)

args = args_handler();
multi_files_handler(args.filename, args.total_lines, args.total_bytes) if args.filename else no_file_handler(args.total_lines, args.total_bytes)

sys.exit(0)
