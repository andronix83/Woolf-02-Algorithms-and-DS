# Implementation of Red-Black Tree was created with the help of AI

import enum

class Color(enum.IntEnum):
    RED = 1
    BLACK = 0

class Node:
    def __init__(self, data, color: Color=Color.RED):
        self.data = data
        self.color = color
        self.left = None
        self.right = None
        self.parent = None

class RedBlackTree:
    def __init__(self):
        # NIL node is a sentinel used for all leaves
        self.TNE = Node(0, color=Color.BLACK)
        self.root = self.TNE

    def insert(self, key):
        # Standard BST insert
        node = Node(key)
        node.parent = None
        node.data = key
        node.left = self.TNE
        node.right = self.TNE
        node.color = Color.RED # New nodes are always red

        y = None
        x = self.root

        while x != self.TNE:
            y = x
            if node.data < x.data:
                x = x.left
            else:
                x = x.right

        node.parent = y
        if y is None:
            self.root = node
        elif node.data < y.data:
            y.left = node
        else:
            y.right = node

        if node.parent is None:
            node.color = Color.BLACK
            return

        if node.parent.parent is None:
            return

        # Fix the tree properties
        self._fix_insert(node)

    def _fix_insert(self, k):
        while k.parent.color == Color.RED:
            if k.parent == k.parent.parent.right:
                u = k.parent.parent.left # uncle
                if u.color == Color.RED:
                    # Case 1: Uncle is red
                    u.color = Color.BLACK
                    k.parent.color = Color.BLACK
                    k.parent.parent.color = Color.RED
                    k = k.parent.parent
                else:
                    if k == k.parent.left:
                        # Case 2: Uncle is black, k is left child
                        k = k.parent
                        self._right_rotate(k)
                    # Case 3: Uncle is black, k is right child
                    k.parent.color = Color.BLACK
                    k.parent.parent.color = Color.RED
                    self._left_rotate(k.parent.parent)
            else:
                u = k.parent.parent.right # uncle
                if u.color == Color.RED:
                    # Case 1 mirror
                    u.color = Color.BLACK
                    k.parent.color = Color.BLACK
                    k.parent.parent.color = Color.RED
                    k = k.parent.parent
                else:
                    if k == k.parent.right:
                        # Case 2 mirror
                        k = k.parent
                        self._left_rotate(k)
                    # Case 3 mirror
                    k.parent.color = Color.BLACK
                    k.parent.parent.color = Color.RED
                    self._right_rotate(k.parent.parent)
            if k == self.root:
                break
        self.root.color = Color.BLACK

    def _left_rotate(self, x):
        y = x.right
        x.right = y.left
        if y.left != self.TNE:
            y.left.parent = x

        y.parent = x.parent
        if x.parent is None:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y

    def _right_rotate(self, x):
        y = x.left
        x.left = y.right
        if y.right != self.TNE:
            y.right.parent = x

        y.parent = x.parent
        if x.parent is None:
            self.root = y
        elif x == x.parent.right:
            x.parent.right = y
        else:
            x.parent.left = y
        y.right = x
        x.parent = y

    # My implemented methods
    def sum_values(self):
        """Returns the sum of all nodes in the tree."""
        return self._recursive_sum(self.root)

    def _recursive_sum(self, node):
        if node == self.TNE:
            return 0
        return node.data + self._recursive_sum(node.left) + self._recursive_sum(node.right)


def main() -> None:
    rbt = RedBlackTree()
    values = [10, 20, 30, 15, 25]

    for v in values:
        rbt.insert(v)

    print(f"Values inserted in RBT: {values}")
    print(f"Sum of all RBT nodes: {rbt.sum_values()}")  # Output: 100


if __name__ == "__main__":
    main()