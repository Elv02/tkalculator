"""
    A module containing logic for the Binary Expression Tree.
"""
from os import posix_fadvise
from typing import List
import re

class Node:
    """
        A Node in a Binary Tree.
        Has a stored value, left and right child.
    """
    def __init__(self, l_child, r_child, value: str) -> None:
        """
            Initialize the new node with it's left and right children and stored value.
        """
        self.l_child = l_child
        self.r_child = r_child
        self.value = value

    def __str__(self, depth=0) -> str:
        """
            String represents node and all children.
        """
        to_return = "\t"*depth + repr(self.value) + "\n"

        if self.l_child is not None:
            to_return += self.l_child.__str__(depth+1)
        if self.r_child is not None:
            to_return += self.r_child.__str__(depth+1)
        return to_return

    def __repr__(self) -> str:
        """
            Return the string representation of this objects data.
        """
        return "<" + self.value + ">"

def is_tree_valid(node: Node) -> bool:
    """
        Check whether a given Binary Expression Tree is in valid form.
        All operators should be inner branches, with either 2 children
        for basic ops, or 1 left child for function calls.
        Leaves should be all numerical values.
    """
    if node.l_child is None and node.r_child is None:
        num_search = re.search(r"^[+-]?\d+(\.\d+)?$", node.value)
        if num_search:
            return True
        return False
    if node.l_child is not None and node.r_child is None:
        return is_tree_valid(node.l_child)
    if node.l_child is not None and node.r_child is not None:
        return is_tree_valid(node.l_child) and is_tree_valid(node.r_child)
    return False

def build_node(stack: List[Node], val: str):
    """
        Construct an node from a given value.
        Pushes the node onto the stack before returning.
    """
    num_search = re.search(r"^[+-]?\d+(\.\d+)?$", val)
    if num_search:
        leaf = Node(None, None, val)
        stack.append(leaf)
        return

    first = None
    second = None
    if val in ("+", "-", "×", "*", "÷", "/", "^", "(", ")"):
        if len(stack)>0:
            second = stack.pop()
        if len(stack)>0:
            first = stack.pop()
        branch = Node(first, second, val)
        stack.append(branch)
        return
    if val in ("√", "%"):
        if len(stack)>0:
            first = stack.pop()
        branch = Node(first, None, val)
        stack.append(branch)
        return
    raise ValueError("Invalid operator: ", val)

def construct_tree(postfix: str) -> Node:
    """
        Constructs and returns root node for the B.E.T. created from a given postfix expression.
    """

    stack = []
    for _op in postfix.split():
        build_node(stack, _op)
    root = stack.pop()
    print(root)
    return root
