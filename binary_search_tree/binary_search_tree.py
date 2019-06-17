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
        test = False
        l_test = False
        r_test = False
        if self.value == None:
            return 
        elif self.value == target:
            test = True
        if self.left:
            l_test = self.left.contains(target)
        if self.right:
            r_test = self.right.contains(target)
        
        if test or l_test or r_test:
            return True
        else:
            return False

    def get_max(self):
        l_max = 0
        r_max = 0
        if self.value == None:
            return            
        max_value = self.value
        if self.left:
            l_max = self.left.get_max()
        if self.right:
            r_max = self.right.get_max()
        if l_max > max_value:
            max_value = l_max
        if r_max > max_value:
            max_value = r_max
        
        return max_value

    def for_each(self, cb):
        # Preorder traversal
        if self.value == None:
            return
        cb(self.value)
        if self.left:
            self.left.for_each(cb)
        if self.right:
            self.right.for_each(cb)

# root = BinarySearchTree(55) # root
# root.insert(90) # root.right
# root.insert(43) # root.left
# root.insert(40) # root.left.left