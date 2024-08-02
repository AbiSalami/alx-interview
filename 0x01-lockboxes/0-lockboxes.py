#!/usr/bin/python3
"""Module that checks locked boxes."""


def canUnlockAll(boxes):
    """Method that determines if all boxes can be opened."""

    if not isinstance(boxes, list) or len(boxes) == 0:
        return False

    check = [0]
    total_boxes = len(boxes)
    list_ing = list(range(total_boxes))

    for in_check in check:
        for in_boxes in boxes[in_check]:
            if in_boxes not in check and in_boxes in list_ing:
                if in_boxes >= total_boxes:
                    return False
                check.append(in_boxes)
                if len(check) == total_boxes:
                    return True
    return len(check) == total_boxes
