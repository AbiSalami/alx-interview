#!/usr/bin/python3
import sys
import signal

total_size = 0
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
    print("File size: {}".format(total_size))
    for code in sorted(status_codes_count.keys()):
        if status_codes_count[code] > 0:
            print("{}: {}".format(code, status_codes_count[code]))

def signal_handler(sig, frame):
    print_stats()
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

for line in sys.stdin:
    try:
        parts = line.split()
        if len(parts) != 10:
            continue
        ip, _, _, date, _, method, path, protocol, status_code, file_size = parts
        if method != '"GET' or path != '/projects/260' or protocol != 'HTTP/1.1"':
            continue
        total_size += int(file_size)
        if status_code in status_codes_count:
            status_codes_count[status_code] += 1
        line_count += 1
        if line_count % 10 == 0:
            print_stats()
    except Exception:
        continue

print_stats()
