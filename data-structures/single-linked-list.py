class Node:
    def __init__(self, data = None):
        self.data = data
        self.next = None

    
class SingleLinkedList:
    def __init__(self):
        self.head = Node()

    def add(self, data):
        node = Node(data)
        curr = self.head

        while curr.next != None:
            curr = curr.next
        curr.next = node

    def length(self):
        curr = self.head
        count = 0

        while curr.next != None:
            count += 1
            curr = curr.next

        return count

    def show_list(self):
        all_items = []
        curr = self.head

        while curr.next != None:
            all_items.append(curr.data)
            curr = curr.next
        
        return all_items
    