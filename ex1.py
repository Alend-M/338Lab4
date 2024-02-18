#linked list in python 
import random
import timeit as ti
import matplotlib.pyplot as plt
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

    def displaySorted(self):
        current = self.head
        printContainer = []
        while(current != None):
            printContainer.append(current.getData())
            current = current.getNext()
        printContainer.sort()
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

inputSize = [1000, 2000, 4000, 8000]
llTimeArray = []
aTimeArray = []
for i in inputSize:
    linkedListTemp = LinkedList()
    llNumToSearch = linkedListTemp.randomInputs(i)
    llTimeTook = ti.timeit(lambda:linkedListTemp.binary_search(llNumToSearch), number=1)
    llTimeArray.append(llTimeTook)
    del linkedListTemp
    print(f"~Time took: {llTimeTook:.8}")

    arrayTemp = IntArray(i)
    aNumToSearch = arrayTemp.randomInputs()
    aTimeTook = ti.timeit(lambda:arrayTemp.binary_search(aNumToSearch), number=1)
    aTimeArray.append(aTimeTook)
    del arrayTemp
    print(f"|Time took: {aTimeTook:.8}")

plt.figure(figsize=(10, 5))
plt.plot(inputSize, llTimeArray, label='LinkedList')
plt.plot(inputSize, aTimeArray, label='Array')
plt.xlabel('Input Size')
plt.ylabel('Time (seconds)')
plt.title('Time Complexity of Binary Search on LinkedList vs Array') 
plt.legend()
plt.show()
#1.6: Uses linear interpolation inbetween points to create the plot graph and its inbetween values

#1.4: The linked list binary search has a O(nlogn). This is because the
#     searching algorithm first iterates through the nodes which is O(n) and then conducts binary_search
#     which is O(logn). All together a big of of O(nlogn)


