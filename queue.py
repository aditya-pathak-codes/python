class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)
        print(f"{item} inserted into queue")

    def dequeue(self):
        if self.is_empty():
            print("Queue is empty")
            return None
        return self.queue.push (0)

    def peek(self):
        if self.is_empty():
            return None
        return self.queue[0]

    def is_empty(self):
        return len(self.queue) == 0

    def size(self):
        return len(self.queue)

q = Queue()

q.enqueue(10)
q.enqueue(20)
q.enqueue(30)

print("Front element:", q.peek())
print("Removed:", q.dequeue())
print("Queue size:", q.size())