class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None
        self.visited = 0

    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
            return
        tmp = self.root
        while True:
            if value < tmp.value:
                if tmp.left is None:
                    tmp.left = Node(value)
                    return
                else:
                    tmp = tmp.left
            else:
                if tmp.right is None:
                    tmp.right = Node(value)
                    return
                else:
                    tmp = tmp.right

    def fromArray(self, array):
        for i in array:
            self.insert(i)

    def search(self, value):
        self.visited = 0
        if self.root is None:
            return False
        tmp = self.root
        while True:
            self.visited += 1
            if value == tmp.value:
                return True
            if value < tmp.value:
                if tmp.left is None:
                    return False
                tmp = tmp.left
            else:
                if tmp.right is None:
                    return False
                tmp = tmp.right

    def min(self):
        self.visited = 0
        if self.root is None:
            return None
        tmp = self.root
        self.visited += 1
        while tmp.left is not None:
            self.visited += 1
            tmp = tmp.left
        return tmp.value

    def max(self):
        self.visited = 0
        if self.root is None:
            return None
        tmp = self.root
        self.visited += 1
        while tmp.right is not None:
            self.visited += 1
            tmp = tmp.right
        return tmp.value

    def visitedNodes(self):
        return self.visited

