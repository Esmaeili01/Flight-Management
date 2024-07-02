# Data Structure : Circular Queue
class Queue:
    def __init__(self):
        self.Size = 6
        self.array = [None] * self.Size 
        self.front = 0
        self.rear = 0
    def empty(self): 
        if self.front == self.rear:
            return 1  
        else:
            return 0  
    def full(self):
        if self.front == (self.rear+1) % self.Size:
            return 1 
        else:
            return 0  
    def insert(self , item):
        if self.full() == 0:
            self.array[self.rear] = item
            self.rear = (self.rear + 1) % self.Size
            return 1 
        else:
            return 0
    def remove(self):
        if self.empty() == 0:
            self.array[self.front] = None
            self.front = (self.front + 1) % self.Size
            return 1 
        else:
            return 0
    def display(self):
        return self.array[self.front]