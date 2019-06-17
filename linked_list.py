class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node 

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next

    def set_value(self, value):
        self.value = value

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_to_tail(self, value):
        # wrap the value in a node 
        new_node = Node(value)
        # check if we're in an empty list state
        if not self.head and not self.tail:
            # set the list's head reference to point to new_node
            self.head = new_node
            # set the list's tail reference to point to new_node 
            self.tail = new_node
        else:
            # update the old tail's next reference to refer to the new node 
            self.tail.set_next(new_node)
            # update the LinkeList's `tail` reference 
            self.tail = new_node

    def remove_head(self):
        # what if our list is empty?
        if not self.head and not self.tail:
            return None
        # what if our list only contained a single node?
        # if not self.head.get_next():
        if self.head is self.tail:
            old_head = self.head
            self.head = None
            self.tail = None
            return old_head.get_value()
        # store a reference to the node we're removing 
        old_head = self.head
        # update the head reference to refer to the old head's next node 
        self.head = old_head.get_next()
        # return the old head's value 
        return old_head.get_value()

        # if self.head is self.tail:
        #     self.tail = None
        # old_head = self.head
        # self.head = old_head.get_next()
        # return old_head.get_value()

    def contains(self, target):
        # what if our list is empty?
        if not self.head and not self.tail:
            return False
        # get another reference that initially starts at the head of the list 
        current = self.head
        # loop so long as `current` is a valid Node 
        while current:
            if currrent.get_value() == target:
                return True
            # update the current to refer to current's next node 
            current = current.get_next()
        # we've looped through the whole list and haven't found what we're looking for 
        return False
        
