# Question 1:
The time complexity of the original reverse() function is O(n^2). The function employs the use of the 'get_element_at_pos' function, which has a complexity of O(n) by itself, as it uses list traversal to access an element by a specified index. The function then creates a new node, copies the data of the old node, and repeats that process for each node in the linked list. This process creates a new list in memory which is a reversed copy of the original list. This results in a quadratic time complexity, as it calls a function with a linear time complexity 'i' number of times. As the size of the linked list would increase, the amount of time taken to complete the function would increase quadratically.

# Question 2:
## Old function:
def reverse(self):
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
## New function:
def optimized_reverse(self):
        prev_node = None
        current_node = self.head
        while (current_node != None):
            next_node = current_node.next
            current_node.next = prev_node
            prev_node = current_node
            current_node = next_node
        self.head = prev_node

The time complexity of the optimized reverse function is O(n). This is because the optimized version of the function only uses list traversal to reverse the linked list, which is known to have a time complexity of O(n). The optimized version is altered to use list traversal and an extra temporary variable in order to reverse the list in-place. In comparison, the unoptimized version created a new list with the data reversed. This is less efficient both in terms of time complexity and in terms of the memory usage of the program, as creating a new list would force more memory to be allocated when running the reverse function.