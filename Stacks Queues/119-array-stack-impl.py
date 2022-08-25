#!bin/bash

"""
1. Create a stack using array architecture
2. Inputs/Outputs: 
    pop() -> value of popped item
    peek() -> value of top item
    push(value) -> None
3. We care about speed and readability
4. ok :)
5. N/A
7. Implement
8. write down steps
9. Modularize code
10. write
"""

class Stack:
    def __init__(self):
        self.stack = []
        self.length = 0

    def __repr__(self):
        result = ""
        for i in self.stack:
            if i is not None:
                result += "{} ->".format(i)
        return result

    def pop(self):
        if self.length == 0:
            return None

        # pop the top element
        # update the length
        self.length -= 1

        return self.stack.pop()


    def peek(self):
        return self.stack[0]

    def push(self, value):
        # Forgot to increment length
        self.stack.insert(-1, value)
        self.length += 1
        return

stack = Stack()
print(stack.push("google"))
print(stack.push("Udemy"))
print(stack.push("Discord"))

print(stack)

print(stack.pop())
print(stack.pop())

print(stack)
