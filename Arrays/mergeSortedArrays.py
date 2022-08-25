#!/bin/bash

"""
 1. Sorted array, merge with sort
 2. Input: two sorted arrays with integers. Output: One merged sorted array
 3. Main Goal: Return a sorted array with low time complexity
 4. ok :)
 5. Naive: Iterate through each array (nested) and compare each value,
           then add to result list
"""
#Naive
def mergeSortedArrays(arr1, arr2):
    result = []

    while len(arr1) > 0 or len(arr2) > 0:
        arr1_item = arr1[i]
        arr2_item = arr2[j]
        print(arr1_item, arr2_item)
        if arr1_item < arr2_item:
            result.append(arr1.pop(i))
            break
        elif arr2_item < arr1_item:
            result.append(arr2.pop(j))
            break
        elif arr1_item == arr2_item:
            # If they are equal
            result.append(arr1.pop(i))
            result.append(arr2.pop(j))
            break
    print(arr1, arr2)
    return result
#O(n2)


# Better
def mergeSortedArrays2(arr1, arr2):
    result = []
    
    arr1_pointer = 0
    arr2_pointer = 0

    max_length = max(len(arr1), len(arr2))

    # Iterate through each array, making comparisons
    while arr1_pointer < max_length-1 or arr2_pointer < max_length-1:
        arr1_current = arr1[arr1_pointer]
        arr2_current = arr2[arr2_pointer]

        if arr1_current == arr2_current:
            result.append(arr1_current)
            result.append(arr2_current)
            arr1_pointer += 1
            arr2_pointer +=1
            continue

        elif arr1_current < arr2_current:
            result.append(arr1_current)
            arr1_pointer+=1
            continue

        elif  arr2_current < arr1_current:
            result.append(arr2_current)
            arr2_pointer+=1
            continue
        
        else:
            break
        
    return result

# O(n)
print(mergeSortedArrays([0,3,4,31], [4,6,30]))
