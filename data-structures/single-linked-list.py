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

        if curr == None:
            curr = node
        else: 
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
            curr = curr.next
            all_items.append(curr.data)
        
        print(all_items)

    def get_item(self, index):
        if index >= self.length():
            return "Index out of range!"
        indx = 0
        curr = self.head

        while curr.next != None:
            if indx == index:
                return curr.data

            indx += 1

    def delete(self, index):
        if index >= self.length():
            return "Index out of range!"
        indx = 0
        curr = self.head

        while curr.next != None:
            last = curr
            curr = curr.next
            if indx == index:
                last.next = curr.next
                return "Deleted!"
                indx += 1

    def insert(self, index, data):
        if index >= self.length():
            return "Index out of range!"

        elif index == self.length():
            self.add(data)

        node = Node(data)
        indx = 0
        curr = self.head
    
        while curr.next != None:
            last = curr
            curr = curr.next

            if indx == index:
                last.next = node
                node.next = curr
            indx += 1

if __name__ == '__main__':
    l = SingleLinkedList()  

    for num in range(10):
        l.add(num)

    l.get_item(3)

    l.insert(4, 11)

    l.delete(2)

    l.show_list()