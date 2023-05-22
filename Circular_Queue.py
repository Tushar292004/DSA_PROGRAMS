class CircularQueue:
    def __init__(self, capacity):
        self.capacity = capacity
        self.queue = [None] * capacity
        self.size = 0
        self.front = 0
        self.rear = -1

    def is_empty(self):
        return self.size == 0

    def is_full(self):
        return self.size == self.capacity

    def enqueue(self, data):
        if self.is_full():
            print("Queue is full")
            return

        self.rear = (self.rear + 1) % self.capacity
        self.queue[self.rear] = data
        self.size += 1

    def dequeue(self):
        if self.is_empty():
            print("Queue is empty")
            return None

        data = self.queue[self.front]
        self.front = (self.front + 1) % self.capacity
        self.size -= 1
        return data

    def display(self):
        if self.is_empty():
            print("Queue is empty")
            return

        print("Elements in the circular queue are:", end=" ")
        for i in range(self.size):
            index = (self.front + i) % self.capacity
            print(self.queue[index], end=" ")
        print()

# Create a circular queue of capacity 5
cq = CircularQueue(5)

# Enqueue elements
cq.enqueue(14)
cq.enqueue(22)
cq.enqueue(13)
cq.enqueue(6)

# Display the queue
cq.display()  # Output: Elements in the circular queue are: 14 22 13 6

# Dequeue elements
print("Deleted value =", cq.dequeue())  # Output: Deleted value = 14
print("Deleted value =", cq.dequeue())  # Output: Deleted value = 22

# Display the queue after dequeue
cq.display()  # Output: Elements in the circular queue are: 13 6

# Enqueue more elements
cq.enqueue(9)
cq.enqueue(20)
cq.enqueue(5)

# Display the queue after enqueue
cq.display()  # Output: Elements in the circular queue are: 13 6 9 20 5
