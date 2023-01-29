# Last in, first out

class Stack:
    def __init__(self):
        self.stack = []
    
    def is_empty(self):
        return self.stack == []

    def add_item(self, item):
        self.stack.append(item)

    def delete_item(self):
        if self.is_empty():
            print("Its empty!")
        self.stack.pop()

    def peek(self):
        if self.is_empty():
            print("Its empty!")
        return self.stack[len(self.stack) - 1]

    def show_items(self):
        print(self.stack)

s = Stack()
c = 0

while c != 5:
    print('\tSTACK OPERATIONS')
    print('1.Add')
    print('2.Delete')
    print('3.Peek')
    print('4.Show Stack')
    print('5.Exit')
    c = int(input('Enter your choice(1-5): '))
    if c == 1:
        x = input("Enter the item: ")
        s.add_item(x)
    elif c == 2:
        s.delete_item()
    elif c == 3:
        s.peek()
    elif c == 4:
        print(s.show_items())
    elif c != 5:
        print('Wrong Choice! Choose from 1 to 5 only')

print('Bye')
        