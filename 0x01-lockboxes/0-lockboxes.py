def canUnlockAll(boxes):
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

