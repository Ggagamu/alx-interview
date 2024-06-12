#!/usr/bin/python3
"""Method that determines if all the boxes can be opened."""


def canUnlockAll(boxes):
    """This function takes a list of lists and the content
       of a list will unlock other lists
    """

    keys = [0]
    for key in keys:
        for boXKey in boxes[key]:
            if boXKey not in keys and boXKey < len(boxes):
                keys.append(boXKey)
    if len(keys) == len(boxes):
        return True
    return False
