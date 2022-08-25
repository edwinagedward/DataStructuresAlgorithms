#!/bin/bash

# Google question :)
# 1. Key points: given an unordered array
# 2. Input: nums - a list of integers | Output: the first repeating character
# 3. Main goal: Time complexity
# 4. ok!
# 5. nested for loops to compare each item with its pair at i+1, return the
#    first input that returns at i and j.
# 6. It is an O(n2) approach, it is slow and does a lot of calculations twice
# 7. Use a hash table. for each new char, add the char as a key, and a boolean
#    as the value. If the boolean is True, return the key, else continue

def firstRecurringCharacter(nums): 
    # Check if the list is empty or with one element
    if len(nums) < 2:
        return None 

    char_hash_table = {}

    for char in nums:
        if char in char_hash_table and char_hash_table[char] == True:
            return char
        char_hash_table[char] = True
    return None

print(firstRecurringCharacter([2]))