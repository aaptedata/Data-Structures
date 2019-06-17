class Heap:
    def __init__(self, comparator):
        self.storage = []
        self.comparator = comparator # function to determine priority

    def insert(self, value):
        pass

    def delete(self):
        pass

    def get_priority(self):
        pass

    def get_size(self):
        pass

    def _bubble_up(self, index):
        # bubble until you've reached the top of the heap
        # or until the parent is higher priority
        while index > 0:
        # single bubble up iteration:
          # get parent index
              parent = (index - 1) // 2
              # compare the child against value of the parent
              # if child value has higher ppriority than parent's value
              if self.storage[index] > self.storage[parent]:
                  # swap them
                  self.storage[index], self.storage[parent] = self.storage[parent], self.storage[index]
                  # update child's index to be new index
                  index = parent

              else:
              # stop bubbling
                  break

    def _sift_down(self, index):
        pass
