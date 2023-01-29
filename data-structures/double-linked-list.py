class Node:
    def __init__(self, data = None):
        self.data = data
        self.next = None
        self.prev = None

class DoubleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def length(self):
        count = 0
        curr = self.head

        while curr:
            count += 1
            curr = curr.next

        return count

    def get_item(self, index):
        if index >= self.length():
            print("Out of range!")

        idx = 0
        curr = self.head

        while curr:
            if idx == index:
                return curr
            idx += 1
            curr = curr.next

        
    def insert_start(self, data):
        node = Node(data)
        
        if self.head:
            node.next = self.head
            self.head.prev = self.tail
            self.head = node
        else:
            self.head = self.tail = node

    def insert_end(self, data):
        node = Node(data)

        if self.tail:
            self.tail.next = node
            node.prev = self.tail
            self.tail = node
        else:
            self.head = self.tail = node

    def instert_next(self, ref, data):
        if not ref:
            return
        node = Node(data)
        node.prev = ref

        if ref.next is None:
            self.tail = node
        else:
            node.next = ref.next
            node.next.prev = node
        ref.next = node

    def instert_prev(self, ref, data):
        if not ref:
            return
        node = Node(data)
        node.next = ref

        if ref.prev is None:
            self.head = node
        else:
            node.prev = ref.prev
            ref.prev.next = node
        ref.prev = node
    
    def remove(self, node):
        if not node:
            return
        if not node.prev:
            self.head = node.next
        else:
            node.prev.next = node.next
        if not node.next:
            self.tail = node.prev
        else:
            node.next.prev = node.prev

    def show_list(self):
        all_items = []
        curr = self.head

        while curr:
            all_items.append(curr.data)
            curr = curr.next
        return all_items


if __name__ == '__main__':
    x = DoubleLinkedList() # creating object of doublyLinkedList
    x.insert_start(1) # Inserting 1 at the begining
    x.insert_end(2) # Inserting 2 at the end
    x.insert_end(6) # Inserting 6 at the end
    x.instert_next(x.get_item(1),5) # Inserting 5 after 1st(according to index) node
    x.instert_prev(x.get_item(3),10)# Inserting 10 before 3rd(according to index) node
    x.remove(x.get_item(1)) # Removing 1st(according to index) node
    print(x.length()) # Print the length of the Linked List
    print(x.show_list()) # Print the Linked List i.e. [1,5,10,6]