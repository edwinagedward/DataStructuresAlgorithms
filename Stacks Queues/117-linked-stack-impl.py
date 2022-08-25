#!bin/bash
"""
1. Create a Stack using a linked list archetecture.
   Use Node class -> self.value && self.next
   Add peek, push(x), and pop

2. Inputs/Outputs:
   peek() -> value to be popped
   push(value) -> None
   pop() -> value that has been popped

3. Main goal is speed
4. ok :)
5/6. Naive approach would be to use an array.  It is a faster approach which may be
   less readable for the next engineer who comes in to read, but being that this is
   a stack and not a queue, it shouldn't be a problem.
"""

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Stack:
    def __init__(self):
        self.top = None
        self.bottom = None
        self.length = 0

    def __repr__(self):

        curr_node = self.top
        result = ""
        while curr_node is not None:
            result += "{} -> ".format(curr_node.value)
            curr_node = curr_node.next

        result += "/n Top: {}/n Bottom: {}".format(self.top, self.bottom)
        return result

    def peek(self):
        # Looking at the top element
        return self.top.value

    def push(self, value):
        # Replace the top element

        # create the node for the current element
        new_top = Node(value)

        # get the current top element
        old_top = self.top

        # set the .next to the old top element
        new_top.next = old_top

        # update self.top
        self.top = new_top

        # Update bottom element if it is None
        if self.bottom is None:
            self.bottom = new_top
        
        self.length += 1

        return

    def pop(self):
        # Return the top element and remove from list

        # Check if the list is empty
        if self.top is None:
            return None

        # retreive the top element
        popped_element = self.top
        
        # update self.top
        self.top = popped_element.next

        # If we remove the last element
        if self.top is None:
            self.bottom = None

        self.length -= 1

        return popped_element.value

stack = Stack()
print(stack.push("google"))
print(stack.push("Udemy"))
print(stack.push("Discord"))

print(stack)

print(stack.pop())
print(stack.pop())
print(stack.pop())

print(stack)