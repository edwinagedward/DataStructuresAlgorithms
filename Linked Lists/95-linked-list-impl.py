#!/bin/bash

# 1. Linked list, tracking head, tail, values of each node. Node stored in head
# 2. inputs: append(value) outputs: append(value) = None
# 3. Time complexity
# 4. ok :)
# 5. Iterate through the list, until the tail points to null, and
#    set the pointer of that tail to the head of the new node
# 6. It is not good because it is slow.. O(n), unnecessary to iterate
#    through the list when a tail value exists. Slow and wastes time
# 7. I plan to use the tail value to access its pointer and set the
#    next pointer to the new object.

class LinkedList:
    def __init__(self, value):
        self.head = { 
            "value": value,
            "next": None,
            "prev": None
            }
        
        self.tail = self.head
        self.length = 1

    def __repr__(self):
        currentnode = self.head
        result = ""
        while currentnode is not None:
            result += "(head: {} -> ".format(currentnode["value"])
            currentnode = currentnode["next"]
        return result

    def append(self, value):

        # retreive the tail of the list
        tail = self.tail

        # make the current node
        curr_node = {"value": value, "next": None, "prev": tail}
        # set the tail.next to the head of the current node
        tail["next"] = curr_node

        # increment the length
        self.length += 1

        # update the tail
        self.tail = curr_node

        # return
        return self.head

    def prepend(self, value):
        # retrieve the head of the list
        head = self.head

        # create the current node
        # set the currentnode.next to the current head
        curr_node = { "value": value, "next": head, "prev": None}
        
        # update the previous for the head
        head["prev"] = curr_node

        # set the self.head to the current node
        self.head = curr_node

        # update previous value
        self.prev = None

        # increment the length
        self.length += 1

        # return
        return self.head

    def insert(self, index, value):

        # check if it is a prepend or append case
        if index == 0:
            return self.prepend(value)
        elif index >= self.length:
            return self.append(value)

        # create the new_node
        new_node = { "value": value, "next": None, "prev": None}

        # Grab the node before the goal index
        index_previous = index - 1
        parent_node = self.traverse_to_index(index_previous)
        goal_node = parent_node["next"]
        # we are now at the node before the goal index
        # point newnode[next] to the rest of the list
        new_node["next"] = goal_node

        # update the goal node's previous value
        goal_node["prev"] = new_node

        # update the new node's previous with the parent node
        new_node["prev"] = parent_node

        # point the previous value to the new node
        parent_node["next"] = new_node
        
        # increment the length
        self.length += 1
        # return
        return self.head
    
    def remove(self, index):
        # retreive to previous index
        parent_node = self.traverse_to_index(index-1)

        # retreive the goal index
        # instead of calculating TWICE, just go to next
        goal_node = parent_node["next"]

        # set previousindex[next] to goalindex[next]
        latter_node = goal_node["next"]
        latter_node["prev"] = parent_node

        parent_node["next"] = latter_node

        # decrement the length
        self.length -= 1

        return self.head
    
    def reverse(self):
        # set an index
        index = 0
        curr_node = self.head
        # iterate over all nodes
        while curr_node is not None:

            # [   None <- a -> b -> c -> d -> None ]
            #    temp = b
            #    store = c
            # store the latternode.next node in a variable
            latter_node = curr_node["next"]

            # store the value of the rest of the list so it is not lost
            list_store = latter_node["next"]
            print(f"list store {list_store}")

            # if the index is 0, set node.next to none
            if index == 0:
                curr_node["next"] = None
            else:
                # set the latternode.next to current node.
                latter_node["next"] = curr_node

            if list_store is None:
                #latter_node["next"] = latter_node
                break
            curr_node = list_store
            index += 1
        self.head = curr_node
        # return
        return self.head

    def traverse_to_index(self, index):
        curr_node = self.head
        curr_index = 0
        # iterate to the desired index
        while curr_node is not None:
            if curr_index < index:
                curr_node = curr_node["next"]
                curr_index += 1
                continue
            elif curr_index == index:
                return curr_node

linkedlist = LinkedList(10)
linkedlist.append(5)
linkedlist.append(16)
linkedlist.prepend(1)
linkedlist.insert(0, 9)
linkedlist.remove(3)
print(linkedlist)
print(linkedlist.reverse())
print(linkedlist)