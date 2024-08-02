#!/usr/bin/python3
"""
0-lockboxes module
"""

def canUnlockAll(boxes):
    """
    Determines if all boxes can be unlocked
    Args:
        boxes (list of list of int): list of boxes with keys
    Returns:
        bool: True if all boxes can be unlocked, else False
    """
    n = len(boxes)
    opened = set([0])
    stack = [0]

    while stack:
        current_box = stack.pop()
        for key in boxes[current_box]:
            if key not in opened and key < n:
                opened.add(key)
                stack.append(key)
    
    return len(opened) == n

