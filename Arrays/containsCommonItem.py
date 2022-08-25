#!bin/bash

"""
 Given 2 arrays, create a fn that lets a user know (T/F) whether
 these two arrays contain any common items
 EX:
 array1 = [a, b, c , d]
 array2 = [z, y, i]
 ^^^ FALSE.

 array3 = [a, b, c, x]
 array4 = [z, y, x]
 ^^^ TRUE.
 """

def containsCommonItem(array1, array2):
    """
    Returns if common item between arrays
    """
    array1_set = set(array1)
    array2_set = set(array2)

    if (array1_set & array2_set):
        return True
    return False

print(containsCommonItem(["a", "b", "c"], ["x", "y", "a"]))