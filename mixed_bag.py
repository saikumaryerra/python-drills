import random
import os
def unique(items):
    """
    Return a set of unique values belonging to the `items` list
    """
    return set(items)


def shuffle(items):
    """
    Shuffle all items in a list
    """
    return random.shuffle(items)


def getcwd():
    """
    Get current working directory
    """
    return os.getcwd()



def mkdir(name):
    """
    Create a directory at the current working directory
    """
    os.mkdir(name)
