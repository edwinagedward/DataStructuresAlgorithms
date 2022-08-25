#!bin/bash
"""
1. Creating a queue using a linked list Node architecture
2. Inputs/Outputs:
      enqueue(value) -> None
      dequeue() -> value removed
      peek() -> first value in queue
3. The goal is for speed and memory efficiency
4. ok :)
5/6. N/A
7. I will create a node class, then a queue class, and implement each function
   based on the linked list structure.
8. walk through code and write down steps
9. modularize code
10. start writing
"""

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Queue:
    def __init__(self):
        self.first = None
        self.last = None
        self.length = 0

    def __repr__(self):
        curr_node = self.first
        result = ""

        while curr_node is not None:
            result += "{} -> ".format(curr_node.value)
            next_node = curr_node.next
            curr_node = next_node
        
        return result

    def enqueue(self, value):
        """
        This function will add a node to the queue (FIFO)
        """
        # create a new node
        new_node = Node(value)

        # if the list is empty
        if self.length == 0:
            self.first = new_node
            self.last = new_node
            self.length = 1
            return

        # set the self.last.next = new-node
        self.last.next = new_node

        # update the new self.last
        self.last = new_node

        # increment the list length
        self.length += 1

        return

    def dequeue(self):
        """
        This function will remove a node from the list (FIFO)

        MISTAKES:
             
             * Forgot to check for variable correctness
             * Forgot to return the node
             * Forgot to return the VALUE of said node
        """

        # Retreive the first node
        first_node = self.first

        # set the self.first to be the first-node.next
        self.first = first_node.next

        # decrement the length
        self.length -= 1

        return first_node.value

    def peek(self):
        """
        This function will return the first item in line, with no changes (FIFO)

        MISTAKES:

            * Forgot to return the VALUE of node
        """

        # if the length is 0, return None
        if self.length == 0:
            return None

        # retreive the first item in the list
        return self.first.value


queue = Queue()
queue.enqueue("Joy")
queue.enqueue("Matt")
queue.enqueue("Pavel")
queue.enqueue("Samir")
print(queue)

print(queue.dequeue())
print(queue.dequeue())
print(queue.dequeue())
print(queue.dequeue())
print(queue)


