# ex7.py

import timeit
import matplotlib.pyplot as plt

class Node:
    def __init__(self, data = None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def insert_head(self, node):
        node.next = self.head
        self.head = node

    def insert_tail(self, node):
        if (self.head == None):
            self.head = node
        else:
            current = self.head
            while (current.next != None):
                current = current.next
            current.next = node

    def get_size(self):
        size = 0
        current = self.head
        while (current != None):
            size += 1
            current = current.next
        return size
    
    def get_element_at_pos(self, pos):
        current = self.head
        for i in range (pos):
            if (current == None):
                return None
            current = current.next
        return current
    
    def unoptimized_reverse(self):
        newhead = None
        prevNode = None
        for i in range(self.get_size()-1, -1, -1):
            currNode = self.get_element_at_pos(i)
            currNewNode = Node(currNode.data)
            if (newhead == None):
                newhead = currNewNode
            else:
                prevNode.next = currNewNode
            prevNode = currNewNode
        self.head = newhead
    
    def optimized_reverse(self):
        prev_node = None
        current_node = self.head
        while (current_node != None):
            next_node = current_node.next
            current_node.next = prev_node
            prev_node = current_node
            current_node = next_node
        self.head = prev_node

def linked_list(size):
    linked_list = LinkedList()
    for i in range(size):
        linked_list.insert_tail(Node(i))
    return linked_list

def timing(sizes, type):
    times = []
    if (type == "optimized"):
        for size in sizes:
            list = linked_list(size)
            time = timeit.timeit(lambda: list.optimized_reverse(), number = 100)
            times.append(time)
    elif (type == "unoptimized"):
        for size in sizes:
            list = linked_list(size)
            time = timeit.timeit(lambda: list.unoptimized_reverse(), number = 100)
            times.append(time)
    return times


list_sizes = [1000, 2000, 3000, 4000]

unoptimized_times = timing(list_sizes, "unoptimized")
optimized_times = timing(list_sizes, "optimized")

plt.plot(list_sizes, unoptimized_times, label = "Original Function")
plt.plot(list_sizes, optimized_times, label = "Optimized Function")
plt.xlabel("List Size")
plt.ylabel("Time Taken (seconds)")
plt.title("Comparing Optimized vs Unoptimized Reverse List Functions")
plt.legend()
plt.show()