#!/bin/bash
"""
1. Create a binary search tree
2. I/O: insert(value) -> None | lookup(value) -> ? Boolean?
3. Goal is to efficiently create a BST
4. ok :)
5. Naive approach:
6. Why its naive?
7. See where things can go wrong (unbalanced)
8. comment steps
9. Modularize
10. Actually code
"""
from logging import NullHandler
from turtle import left


class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value
    
    def now(self, node, level=0):
        print(f"node: {node}")
        return_statement = "\t"*level+repr(node.value)+"\n"
        for child in [node.left, node.right]:
            if child is None:
                continue
            return_statement += child.now(child,level=level+1)
        return return_statement

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def __repr__(self) -> str:
        return self.root.now(self.root)

    def insert(self, value):

        # create a node for the value
        new_node = Node(value)

        # if empty
        if self.root is None:
            self.root = new_node
            return

        curr_node = self.root
        while curr_node is not None:
            # check the new node value against the current node's value
            is_smaller = new_node.value < curr_node.value

            # if the new node is smaller
            if is_smaller:
                # if the current node.left is none, set to new node
                leftmost_node = curr_node.left
                if leftmost_node is None:
                    curr_node.left = new_node
                    return
                # else, curr_node = current-node.left
                else:
                    curr_node = leftmost_node
            # elif the new node is larger
            elif not is_smaller:
                # if the current node.right is none, set to new node
                rightmost_node = curr_node.right
                if rightmost_node is None:
                    curr_node.right = new_node
                    return
                # else, curr_node = current-node.right
                else:
                    curr_node = rightmost_node
            # if equal
            else:
                return

    def lookup(self, value):
        # create a current node value
        curr_node = self.root

        # if the tree is empty
        if self.root is None:
            return None

        # if the root is the value, return the root
        if self.root.value == value:
            return self.root

        # while the current node is not none
        while curr_node is not None:
            # is_smaller boolean tests larger or smaller than current node
            is_smaller = value < curr_node.value
            # if is smaller, iterate to next left node
            if is_smaller: 
                leftmost_node = curr_node.left
                curr_node = leftmost_node
            # if it is larger, iterate to next right node
            if not is_smaller:
                rightmost_node = curr_node.right
                curr_node = rightmost_node
            # else (equal), return node
            else:
                return curr_node
        return False;

tree = BinarySearchTree()
tree.insert(9)
tree.insert(4)
tree.insert(20)

tree.insert(1)
tree.insert(6)
tree.insert(15)
tree.insert(120)
print(tree)
