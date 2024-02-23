#3.1: The strategy used to grow arrays when full is over-allocation. This is used in list_resize to allocate more memory in the
#     stack and move the list there. This is calculated in the function mentioned before with the function as the current size,
#     plus one-eighth of the current size plus a small constant (6), rounded up to the nearest multiple of 4.

import sys
import timeit
import matplotlib.pyplot as plt

my_list = []

prev_capacity = None
for i in range(64):
    my_list.append(i)
    list_size = sys.getsizeof(my_list)
    current_capacity = (list_size - sys.getsizeof([])) // 8
    if current_capacity != prev_capacity:
        print(f"Capacity changed! Current capacity: {current_capacity}")
        prev_capacity = current_capacity


def grow_array(S):
    my_list = [0] * S  

    for _ in range(1000):
        my_list.append(42)  

elapsed_time_grow_to_S_plus_1_array = []
elapsed_time_grow_to_S_array = []

S = 64

for _ in range(1000):
    elapsed_time_grow_to_S_plus_1 = timeit.timeit(lambda: grow_array(S), number=1)
    elapsed_time_grow_to_S = timeit.timeit(lambda: grow_array(S - 1), number=1)
    elapsed_time_grow_to_S_plus_1_array.append(elapsed_time_grow_to_S_plus_1)
    elapsed_time_grow_to_S_array.append(elapsed_time_grow_to_S)

print(f"Time to grow from size {S} to {S+1}: {elapsed_time_grow_to_S_plus_1:.6f} seconds")
print(f"Time to grow from size {S-1} to {S}: {elapsed_time_grow_to_S:.6f} seconds")

plt.figure(figsize=(10, 6))
attempts = list(range(1, 1001))
plt.plot(attempts, elapsed_time_grow_to_S_plus_1_array, label='S to S+1', alpha=0.5)
plt.plot(attempts, elapsed_time_grow_to_S_array, label='S-1 to S', alpha=0.5)
plt.ylabel('Time (seconds)')
plt.xlabel('Attempt')
plt.title('Time Measurements of Array Growth')
plt.legend()
plt.show()
#3.5: There is a noticable difference. On multiple instances s to s+1 has extremely longer times compared to 
#     s to s-1. This is likely cause of the over-allocation taking alot of the time for s+1. 
