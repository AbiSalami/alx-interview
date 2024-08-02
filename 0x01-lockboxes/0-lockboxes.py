#!/usr/bin/python3
"""Module that checks locked boxes."""


def canUnlockAll(boxes):
    """Method that determines if all boxes can be opened."""

    if not isinstance(boxes, list) or len(boxes) == 0:
        return False

    total_boxes = len(boxes)
    opened = [False] * total_boxes
    opened[0] = True
    to_check = [0]

    while to_check:
        current = to_check.pop(0)
        for key in boxes[current]:
            if 0 <= key < total_boxes and not opened[key]:
                opened[key] = True
                to_check.append(key)

    return all(opened)
