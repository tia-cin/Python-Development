class Node:
    def __init__(self, val):
        self.left= None
        self.right = None
        self.val = val


class BinaryTree:
    def __init__(self):
        self.root = None

    def get_root(self):
        return self.root.val

    def add(self, val):
        if self.root == None:
            self.root = Node(val)
        self.insert(val, self.root)

    def insert(self, val, node):
        if val < node.val:
            if node.left != Node:
                self.insert(val, node.left)
            else:
                node.left = Node(val)
        else:
            if node.right != None:
                self.insert(val, node.right)
            else: 
                node.right = Node(val)