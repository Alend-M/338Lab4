import time
import random
import matplotlib.pyplot as plt

# inefficient implementation: linear search; worst case complexity: O(n)
def linear_search(arr, key):
    for i in range(len(arr)):
        if arr[i] == key:
            return i
    return -1

# efficient implementation: binary search; worst case complexity: O(log(n))
def binary_search(arr, key):
    lo = 0
    hi = len(arr) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if arr[mid] == key:
            return mid
        elif arr[mid] < key:
            lo = mid + 1
        else:
            hi = mid - 1
    return -1

def timing(type, arr, key):
    times = []
    for i in range(100):
        start_time = time.time()
        type(arr, key)
        end_time = time.time()
        times.append(end_time - start_time)
    return times

array = sorted(random.sample(range(10000), 1500))
key = random.choice(array)

linear = timing(linear_search, array, key)
binary = timing(binary_search, array, key)

plt.hist(linear, bins = 20, label = "Linear Search")
plt.hist(binary, bins = 20, label = "Binary Search")
plt.xlabel("Time in Seconds")
plt.ylabel("Frequency")
plt.title("Time Distribution of Linear vs Binary Search")
plt.legend()
plt.show()