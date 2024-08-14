#!/usr/bin/python3

import sys

def print_msg(dict_sc, total_file_size):
    """
    Method to print the statistics.
    
    Args:
        dict_sc: dict of status codes and their counts
        total_file_size: total file size computed
    Returns:
        Nothing
    """
    print("File size: {}".format(total_file_size))
    for key in sorted(dict_sc):
        if dict_sc[key] > 0:
            print("{}: {}".format(key, dict_sc[key]))

total_file_size = 0
dict_sc = {
    "200": 0,
    "301": 0,
    "400": 0,
    "401": 0,
    "403": 0,
    "404": 0,
    "405": 0,
    "500": 0
}
counter = 0

try:
    for line in sys.stdin:
        parts = line.split()
        
        if len(parts) < 7:
            continue
        
        try:
            file_size = int(parts[-1])
            status_code = parts[-2]
        except ValueError:
            continue

        if status_code in dict_sc:
            total_file_size += file_size
            dict_sc[status_code] += 1
            counter += 1
        
        if counter == 10:
            print_msg(dict_sc, total_file_size)
            counter = 0
            # Reset status code counts to start fresh for the next 10 lines
            dict_sc = {k: 0 for k in dict_sc}

finally:
    print_msg(dict_sc, total_file_size)

