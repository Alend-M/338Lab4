In the lecture recordings, we discussed some of the main differences
between arrays (or lists in python) and Linked Lists.

1. Compare advantages and disadvantages of arrays vs linked list
(complexity of task completion)

- Linked lists take O(1) time complexity for insertion or deletion while arrays takee O(n).
- Searching through arrays for elements is faster as it takes O(1) complexity (because it's
indexed) vs O(n) for linked list.


2. For arrays, we are interested in implementing a replace function
that acts as a deletion followed by insertion. How can this function
be implemented to minimize the impact of each of the standalone
tasks?

3. Assuming you are tasked to implement a doubly linked list with a
sort function, given the list of sort functions below, state the
feasibility of using each one of them and elaborate why is it
possible or not to use them. 
    1. Insertion sort
        - O(n^2) time complexity because you use a loop to traverse the list n times, and in each
        loop you call the sort function, which itself is O(n).
        - No extra space allocation
        - Good for nearly sorted lists. Both sorts are good for small inputs.
    2. Merge sort
        - Better choice.
        - O(nlogn) time complexity (faster than insertion, efficient in large inputs)
        - No extra space allocation
        - Since merge sort does not depend on random access/indexes, it's better for linked list than
        insertion sort which involves swapping elements with their adjacent if they're out of order.

4. Also show the expected complexity for each and how it differs from
applying it to a regular array.
    - vhfltudekcvlguy
