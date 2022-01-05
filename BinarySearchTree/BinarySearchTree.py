class BinarySearchTree:
    def __init__(self):
        self.array = [0, 'X']

    def insert(self, key):
        if len(self.array) - 1 == 1 and self.array[1] == 'X':
            self.array[1] = key
        else:
            n = 1
            while n < len(self.array):
                if self.array[n] != 'X':
                    if key < self.array[n]:
                        if 2 * n > len(self.array) - 1:
                            self.add(len(self.array), 2 * n + 1)
                        n *= 2
                    elif key > self.array[n]:
                        if 2 * n + 1 > len(self.array) - 1:
                            self.add(len(self.array), 2 * n + 2)
                        n = 2 * n + 1
                    else:
                        break
                else:
                    self.array[n] = key
    
    def delete(self, key):
        n = 1
        while n < len(self.array):
            if self.array[n] != 'X':
                if key < self.array[n]:
                    if 2 * n > len(self.array) - 1:
                        break
                    n *= 2
                elif key > self.array[n]:
                    if 2 * n + 1 > len(self.array) - 1:
                        break
                    n = 2 * n + 1
                else:
                    m = 2 * n + 1
                    if m > len(self.array) or self.array[m] == 'X':
                        self.array[n] = 'X'
                        break
                    while m < len(self.array):
                        if 2 * m < len(self.array) - 1 and self.array[2 * m] != 'X':
                            m = 2 * m
                        else:
                            break
                    temp = self.array[m]
                    self.array[m] = self.array[n]
                    self.array[n] = temp
                    self.array[m] = 'X'
                    break
            else:
                break

    def searchKey(self, key):
        try:
            n = 1
            Output = []
            while n < len(self.array):
                Output.append(self.array[n])
                if key < self.array[n]:
                    n *= 2
                elif n > len(self.array):
                    n = 2 * n + 1
                else:
                    print(Output)
                    print(f"{self.array[n]} is found.")
                    return
            print("NOT found.")
        except:
            print("NOT found.")

    def printProperty(self):
        n = 1
        height = 0
        size = 0
        if self.array[n] == 'X':
            print(f"The height of T is {height} and the size of T is {size}.")
            return
        height = self.getHeight(n, 0)
        for i in range(1, len(self.array)):
            if self.array[i] != 'X':
                size += 1
        print(f"The height of T is {height} and the size of T is {size}.")

    def preorderTraversal(self):
        if len(self.array) == 2 and self.array[1] == 'X':
            print("Preorder of T: Tree T is empty")
            return
        Output = []
        self.preorder(1, Output)
        print(f"Preorder of T: {Output}")

    def postorderTraversal(self):
        if len(self.array) == 2 and self.array[1] == 'X':
            print("Postorder of T: Tree T is empty")
            return
        Output = []
        self.postorder(1, Output)
        print(f"Postorder of T: {Output}")

    def inorderTraversal(self):
        if len(self.array) == 2 and self.array[1] == 'X':
            print("Inorder of T: Tree T is empty")
            return
        Output = []
        self.inorder(1, Output)
        print(f"Inorder of T: {Output}")

    def preorder(self, n, Output):
        if self.array[n] == 'X':
            return
        Output.append(self.array[n])
        if 2 * n < len(self.array):
            self.preorder(2 * n, Output)
        if 2 * n + 1 < len(self.array):
            self.preorder(2 * n + 1, Output)

    def postorder(self, n, Output):
        if self.array[n] == 'X':
            return
        if 2 * n < len(self.array):
            self.postorder(2 * n, Output)
        if 2 * n + 1 < len(self.array):
            self.postorder(2 * n + 1, Output)
        Output.append(self.array[n])

    def inorder(self, n, Output):
        if self.array[n] == 'X':
            return
        if 2 * n < len(self.array):
            self.inorder(2 * n, Output)
        Output.append(self.array[n])
        if 2 * n + 1 < len(self.array):
            self.inorder(2 * n + 1, Output)

    def getHeight(self, n, Limit):
        if 2 * n > len(self.array) - 1 and 2 * n + 1 > len(self.array) - 1 or self.array[n] == 'X':
            return Limit
        a = 0
        b = 0
        if 2 * n < len(self.array) - 1:
            a = self.getHeight(2 * n, Limit + 1)
        if 2 * n + 1 < len(self.array) - 1:
            b = self.getHeight(2 * n + 1, Limit + 1)
        if a > b:
            return a
        else: 
            return b

    def add(self, start, end):
        for Run in range(start, end):
            self.array.append('X')



T=BinarySearchTree()
print(T.array)
T.printProperty()
T.preorderTraversal()
T.postorderTraversal()
T.inorderTraversal()

# Simple test
print(T.searchKey(9))
T.insert(35)
print(T.array)
T.printProperty()
T.preorderTraversal()
T.postorderTraversal()
T.inorderTraversal()

# Simple test on insertions
T.insert(45)
T.insert(40)
T.insert(43)
T.insert(41)
T.insert(42)
print(T.array)
T.printProperty()
T.preorderTraversal()
T.postorderTraversal()
T.inorderTraversal()

# Simple test on deletions
T.delete(30)
T.delete(38)
T.delete(40)
print(T.array)
T.printProperty()
T.preorderTraversal()
T.postorderTraversal()
T.inorderTraversal()