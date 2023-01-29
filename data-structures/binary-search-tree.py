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
        
    def show_tree(self, ver = 'in'):
        if self.root != None:
            if ver == 'in':
                self.print_in(self.root)
            elif ver == 'prev':
                self.print_pre(self.root)
            elif ver == 'post':
                self.print_post(self.root)

    def print_in(self, node):
        if node == Node:
            return
        self.print_in(node.left)
        print(node.val)
        self.print_in(node.right)

    def print_pre(self, node):
        if node == None:
            return
        print(node.val)
        self.print_pre(node.left)
        self.print_pre(node.right)

    def print_post(self, node):
        if node == None:
            return
        self.print_post(node.left)
        self.print_post(node.right)
        print(node.val)