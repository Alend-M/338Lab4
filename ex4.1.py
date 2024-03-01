# Ex 4: Complexity Analysis

def processdata(li):
  for i in range(len(li)): #a
    if li[i] > 5: #b
      for j in range(len(li)): #c
        li[i] *= 2 #d

#####
'''1. State and justify what is the best, worst and average case
complexity for the code in the previous slide[0.2 pts]'''


'''The best case complexity for this code would be when it is given a list 'li'
where all elements are <= 5. In that case, the line of code marked "#a" would just
execute n times. The best time case complexity is O(n).

The worst case is if all elements of the list 'li' are >5. Here, the code needs to go
through all lines marked #a to #d. #a and #c are O(n), #b and #d are a basic/constant time 
operations so are O(1). Overall we have O(n^2). The worst case time complexity is O(n^2)

In an avergae case, we may or may not have greater than 5 elements in the list.
Though it depends on the actual distribution of values in the list, the avg case complexity
is O(n^2)'''

#####

'''2. Are average, best, and worst case complexity the same? If not,
produce a modified version of the code above for which average,
best, and worst case complexity are equivalent. [0.2 pts]'''

'''The best avg and worse cases are not the same. If we want all the cases to have a time
complexity of (O(n^2)), (less efficient but all will be equivalent) then we can do this:'''

def processdata(li):
  for i in range(len(li)):  # Outer loop
      for j in range(len(li)):  # Inner loop
          if li[i] > 5:  # Condition
              li[i] *= 2

'''This ensures that two loops are always run n times. This also ensures that the code
will output the same values as the original code did. For example, if given the input 
[10, 2], both codes will double the element at index 0 if it is greater than 5, and
double (the same element) again based on the size of the list.'''