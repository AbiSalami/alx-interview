#!/usr/bin/python3
""" Module that checks locked boxes """

def canUnlockAll(boxes):
    """ Method that determines if all boxes can be opened """
    if not isinstance(boxes, list):
        return False

    if len(boxes) == 0:
        return False

    opened = [0]
    total_boxes = len(boxes)
    list_ing = list(range(total_boxes))

    for in_check in opened:
        for key in boxes[in_check]:
            if key not in opened and key in list_ing:
                if key >= total_boxes:
                    return False
                opened.append(key)
                if len(opened) == total_boxes:
                    return True
    return len(opened) == total_boxes

