#!/usr/bin/python3
"""UTF-8 Validation Module."""

def validUTF8(data):
    """
    Determines if a given data set represents a valid UTF-8 encoding.

    Args:
        data (list): A list of integers representing bytes in the data.

    Returns:
        bool: True if data is valid UTF-8, False otherwise.
    """
    remaining_bytes = 0

    leading_one_mask = 1 << 7
    second_bit_mask = 1 << 6

    for byte in data:
        mask_byte = 1 << 7

        if remaining_bytes == 0:
            while mask_byte & byte:
                remaining_bytes += 1
                mask_byte >>= 1

            if remaining_bytes == 0:
                continue

            if remaining_bytes == 1 or remaining_bytes > 4:
                return False

        else:
            if not (byte & leading_one_mask and not (byte & second_bit_mask)):
                return False

        remaining_bytes -= 1

    return remaining_bytes == 0

