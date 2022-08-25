#!/bin/bash

# 1. Hash function, create get/set
# 2. Inputs/Outputs: 
#        (SET: input: (key, value)    output: None) 
#        (GET: input: (key)           output: [key,value])
# 3. Functionality. Time complexity
# 4. ok :) | do I specifically return for each?
# 5. N/A
# 6. N/A
# 8. walk through code from beginning
# 9. create functions needed for code
# 10. Start writing code

# A decorator is used with __call__, and the output of the function it is
# called with is used as input for the __call__ function.
class HashTable:
    def __init__(self, size):
        self.data = [None for i in range(size)]

    def set(self, in_key, in_value):
        # O(1)
        # Needed code for collisions
        # [None, None, [["hello", 3"], ["love", 143]], None]
        # self.data[bucket_index][entry_index][0]
        address = self._hash(in_key)
        if not self.data[address]:
            self.data[address] = []
        self.data[address].append([in_key, in_value])
        print(self.data)
        return None

    def get(self, in_key):
        # O(1)
        # Don't look at each index as its own item
        # Look at each index as a BUCKET.
        # Check if key does not exist
        currBucket = self.data[self._hash(in_key)]
        print(currBucket)
        key = 0
        value = 1
        if currBucket is not None:
            entry =  [i for i in currBucket if i[key] == in_key]
            return None if not entry else entry[key][value]
        return None

    def keys(self):
        keys_list = []
        for bucket in self.data:
            if bucket is not None:
                keys_list += [i[0] for i in bucket]
        return keys_list

    def _hash(self, key):
        # ord() gets char code
        # O(1), as we are iterating only over the KEY.
        hash = 0
        for i in range(len(key)):
            hash = (hash + ord(key[i]) * i) % len(self.data)
        return hash

hashtable = HashTable(2)

hashtable.set("helli", "45")
hashtable.set("hell0", "450")
print(hashtable.keys())
