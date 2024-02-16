# Question 1:
Array size and capacity are the same; they are both equal to the number of elements that can be held by the array in question.
# Question 2:
When an array needs to grow beyound its current capacity, the method will change depending on the current state of the array.
## Case 1: Space in memory after the end of the array:
When there is space in memory after the end of the array, the program will add the elements into the memory that is currently available.
## Case 2: No space in memory after the end of the array:
When there is no space in memory, the program will copy the array with enough extra space for the new elements, then add the elements to the end of the copy of the array.

Note: In python, arrays are dynamic, which allows the program to grow the array as needed. In other languages, arrays are fixed, meaning they cannot grow/shrink after they are created.