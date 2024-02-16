#linked list in python 
import random

class Node:
    def __init__(self, data, next=None):
        self._data = data
        self._next = None

    def getData(self):
        return self._data

    def setData(self, data):
        self._data = data

    def setNext(self, next):
        self._next = next

    def getNext(self):
        return self._next
    
class LinkedList:
    def __init__(self):
        self.head = None

    def addHead(self, data):
        new_node = Node(data, self.head)
        self.head = new_node

    def addTail(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            current = self.head
        else:
            current = self.head
        while current.getNext() is not None:
            current = current.getNext()
        current.setNext(new_node)
    
    def binary_search(self, item):
        current = self.head
        data = []
        while current:
            data.append(current.getData())
            current = current.getNext()

        data.sort()
        low = 0
        high = len(data) - 1

        while low <= high:
            mid = (low + high) // 2
            guess = data[mid]
            if guess == item:
                return mid
            if guess > item:
                high = mid - 1
            else:
                low = mid + 1
        return None

    def display(self):
        current = self.head
        printContainer = []
        while(current != None):
            printContainer.append(current.getData())
            current = current.getNext()
        print(printContainer)

    def randomInputs(self, length):
        for i in range(length):
            self.addTail(random.randint(0,100))
        return self.head.getData()

    def size(self):
        current = self.head
        count = 0
        while current:
            count += 1
            current = current.getNext()
        return count

class IntArray:
    def __init__(self, length):
        self.array = [0] * length

    def insert(self, index, item):
        self.array[index] = item

    def display(self):
        print(self.array)

    def binary_search(self, item):
        self.array.sort()
        low = 0
        high = len(self.array) - 1

        while low <= high:
            mid = (low + high) // 2
            guess = self.array[mid]
            if guess == item:
                return mid
            if guess > item:
                high = mid - 1
            else:
                low = mid + 1
        return None
    
    def randomInputs(self):
        for i in range(len(self.array)):
            self.array[i] = random.randint(0,100)
        return self.array[random.randint(0,len(self.array)-1)]

linkedList = LinkedList()
num1 = linkedList.randomInputs(100)
print(num1)
print(linkedList.binary_search(num1))

array = IntArray(100)
num = array.randomInputs()
print(num)
print(array.binary_search(num))

#1.4: The linked list binary search has a O(nlogn). This is because the
#     searching algorithm first iterates through the nodes which is O(n) and then conducts binary_search
#     which is O(logn). All together a big of of O(nlogn)

#TODO: FIX ADD NEXT FOR LINKEDLIST TO GEENERATE A VRAIBLE SIZE
