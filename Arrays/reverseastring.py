#!/bin/bash

from sre_compile import isstring


def reverse(str):
    """
    Create a function that should reverse a string
    Hello -> olleH
    """
    # Check input
    if not str or not isstring(str) or len(str) < 2:
        print("Invalid input")
        return

    # Brute force O(n)
    # result = ""
    # for letter in range(len(str)-1, -1, -1):
    #     result += str[letter]
    # print(result)

    # concise way. O(n)
    # Start at end of string and end at position 0, step with -1.
    print(str[::-1])

reverse("")