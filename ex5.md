In class, we have seen two different ways to perform multiple
measures with timeit:

• The first uses the number parameters, as in:
elapsed_time = timeit.timeit(lambda: fibonacci(1000), number=100)

• The second uses the repeat function, as in:
times = timeit.repeat(lambda: fibonacci(1000), repeat =5, number=10)


1. These approaches are designed to deal with different types of
measurement noise. Think about what happens when we try to time
a program, and which types of issues may result in an incorrect
measurement. Reflect on how the two approaches (timeit and repeat) 
attempt to address these issues. Discuss when it is appropriate to 
use one or the other.

2. Typically, the output of timeit is post-processed to compute some
sort of aggregate statistics. Let’s only consider three: average, min,
and max. Which one is the appropriate statistic to apply to the output
of timeit.timeit()? What is the appropriate statistics to apply to
the output of timeit.repeat()? Discuss why