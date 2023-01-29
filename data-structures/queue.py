class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if self.length() == 0:
            return print("Its empty!")
        self.queue.pop(0)
        
    def length(self):
        return len(self.queue)

    def show_queue(self):
        print(self.queue)

if __name__ == '__main__':
    x = Queue() 
    for num in range(10):
        x.enqueue(num)
    x.dequeue()

    x.show_queue()