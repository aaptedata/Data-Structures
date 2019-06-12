''' A queue uses FIFO stacking (first in, first out). 
Therefore, elements are removed from the front and added to the back.'''

class Queue():
    def __init__(self):
        self.size = 0
        # what data structure should we
        # use to store queue elements? 
        self.storage = [] # List

    def enqueue(self, item):
        return self.storage.append(item)
    
    def dequeue(self):
        if self.len() == 0:
            return None
        return self.storage.pop(0) # Default is to pop the last element (aka a stack - LIFO)
        

    def len(self):
        return len(self.storage)


q = Queue()
q.enqueue(5)
q.enqueue(10)
q.enqueue(15)
q.enqueue(20)
print(q.storage)
print(q.dequeue())
print(q.storage)
print(q.len())