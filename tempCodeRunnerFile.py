plt.figure(figsize=(10, 5))  # Set the figure size
plt.plot(inputSize, llTimeArray, label='LinkedList')  # Plot the LinkedList times
plt.plot(inputSize, aTimeArray, label='Array')  # Plot the Array times
plt.xlabel('Input Size')  # Label the x-axis
plt.ylabel('Time (seconds)')  # Label the y-axis
plt.title('Time Complexity of Binary Search on LinkedList vs Array')  # Set the title
plt.legend()  # Show the legend
plt.grid(True)  # Show the grid
plt.show()