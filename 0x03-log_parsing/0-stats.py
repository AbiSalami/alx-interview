#!/usr/bin/python3
import sys
import signal

total_file_size = 0
status_codes_count = {
    '200': 0,
    '301': 0,
    '400': 0,
    '401': 0,
    '403': 0,
    '404': 0,
    '405': 0,
    '500': 0
}
line_count = 0

def print_stats():
    print("File size: {}".format(total_file_size))
    for code in sorted(status_codes_count.keys()):
        if status_codes_count[code] > 0:
            print("{}: {}".format(code, status_codes_count[code]))

def signal_handler(sig, frame):
    print_stats()
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

try:
    for line in sys.stdin:
        parts = line.split()
        if len(parts) < 7:
            continue
        status_code = parts[-2]
        try:
            file_size = int(parts[-1])
            total_file_size += file_size
        except ValueError:
            continue

        if status_code in status_codes_count:
            status_codes_count[status_code] += 1

        line_count += 1
        if line_count == 10:
            print_stats()
            line_count = 0

finally:
    print_stats()

