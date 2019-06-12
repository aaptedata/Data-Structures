class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        # Always wrap value in a node
        # 1. compare the element against the current node's value
        # 2. based on the result of comparison, go left or right
        # 3. If an empty spot is found, park the value there
        # 4. Otherwise go back to step 1

        # Base case: Finding an empty spot to park value.
        if value < self.value:
            # if value is less, go left
            # if there is no left child, we park node there
            if not self.left:
                self.left = BinarySearchTree(value)
            else:
                self.left.insert(value)

        elif value >= self.value:
            if not self.right:
                self.right = BinarySearchTree(value)
            else:
                self.right.insert(value)

    def contains(self, target):
        pass

    def get_max(self):
        pass

    def for_each(self, cb):
        pass

root = BinarySearchTree(55) # root
root.insert(90) # root.right
root.insert(43) # root.left
root.insert(40) # root.left.left