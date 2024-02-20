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

    - Issues that may result in an incorrect time when trying to time a program include:
        -- Other programss or processees running in the background which may affect the execution time of the program you're timing.
        -- Garbage collection. Languages like python which include auto garbage collection may add
        extra time to execution as they deallocate the unused memory.
        -- System/Computer contraints. The software or hardware constraints of the computer itself could lead to slower execution time.

    - Timeit.timeit and timeit.repeat both address these issues. 
    Timeit.timeit measures the avg time for execution of a specified bit of code, over a specified number of executions (number = loops). This avoids any extra time added by background programs or the computer itself being slow, it ignored garbage collection. This is best used for quick measurements of avg execution time.

    - Timeit.repeat does time measurements on a specified bit of code, and repeats them multiple times (numer = loops, repeat = repeating of timing the loops). It returns an array of execution times. This is best used for when you want a more statistical analysis of timings, because there will be slight variations in time with each execution.

2. Typically, the output of timeit is post-processed to compute some
sort of aggregate statistics. Let’s only consider three: average, min,
and max. Which one is the appropriate statistic to apply to the output
of timeit.timeit()? What is the appropriate statistics to apply to
the output of timeit.repeat()? Discuss why

    - The appropriate statistic for timeit.timeit is average as the function itself only returns an average time.
    - For timeit.repeat, all three statistics are worth considering. Minimum and Maximum would be the best and worst case times, respectively. Average would give you the (average) general time to expect when executing the bit of code. That being said, python documentation states here: https://docs.python.org/3/library/timeit.html#timeit.Timer.repeat that the minimum time is likely the only/ most important statistic for timeit.repeat