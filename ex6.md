In the lecture recordings, we discussed some of the main differences
between arrays (or lists in python) and Linked Lists.

1. Compare advantages and disadvantages of arrays vs linked list
(complexity of task completion)

Arrays:
    Advantages
        - O(1) time complexity for searching. Random access (indexed).
    Disadvantages
        - O(n) time complexity for insertion and deletetion at anywhere other than the tail because the array must be shifted to make space/fill space of the added/removed elements
        - Fixed size upon declaration (in languages other than python or others that have memory management built in). Resizing could be 'costly' in terms of time complexity because of possible memory reallocation and data copying if trying to add to the array beyond its allocated space. 

Linked Lists:
    Advantages
        - O(1) time complexity for insertion/deletion, better than arrays because you do not need to shift elements
        - Can dynamically grow/shrink
    Disadvantages
        - O(n) time complexity for searching because you must start traversing from the head pointer
        - Memory overhead as they also need to store the pointers to the next (and prev for double LL) nodes.


2. For arrays, we are interested in implementing a replace function
that acts as a deletion followed by insertion. How can this function
be implemented to minimize the impact of each of the standalone
tasks?

If we want to minimize the impact of deletion followed by insertion via a replace function for an array, then we can do this by directly replacing the element at the target index. For example, making the element at the target index null (thereby deleting the previous value) and then inserting the new element at that same index. This method is more efficient than the alternatives of individual insertion and deletion functions which involve shifting the array to fill/make room for elements and could also lead to memory allocation issues.


3. Assuming you are tasked to implement a doubly linked list with a
sort function, given the list of sort functions below, state the
feasibility of using each one of them and elaborate why is it
possible or not to use them. 
    1. Insertion sort
        - O(n^2) time complexity because you use a loop to traverse the list n times, and in each loop you call the sort function, which itself is O(n).
        - No extra space allocation
        - Good for nearly sorted lists. Both sorts are good for small inputs.
        - Possible to use with a doubly linked list if nodes are ordered, and the prev and next pointers are updated with each swap.
    2. Merge sort
        - Better choice.
        - O(nlogn) time complexity (faster than insertion, efficient in large inputs)
        - No extra space allocation
        - Since merge sort does not depend on random access/indexes, it's better for linked list than
        insertion sort which involves swapping elements with their adjacent if they're out of order.

4. Also show the expected complexity for each and how it differs from
applying it to a regular array.
  
    1. Insertion sort
        - O(n^2) for avg and worst cases for linked list and arrays. Implementation with a linked list is slightly more efficient than with arrays because they are dynamic and we will not need to shift elements by index.
    2. Merge Sort
        - O(nlogn) for linked lists and arrays. Arrays may cost more memory during the merge process (memory reallocation) whilst linked lists can be divided and merged without memory reallocation

