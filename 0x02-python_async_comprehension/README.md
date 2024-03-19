Python async comprehension

This project focuses on implementing asynchronous generators, async comprehensions, and type-annotated generators in Python. These concepts are fundamental in asynchronous programming, allowing developers to write efficient and non-blocking code. The tasks in this project require implementing coroutines to demonstrate the use of async generators and async comprehensions while ensuring adherence to coding standards and proper documentation.
Tasks
0. Async Generator

Implement a coroutine named async_generator that loops 10 times. In each iteration, asynchronously wait for 1 second and then yield a random number between 0 and 10 using the random module.
1. Async Comprehensions

Import the async_generator coroutine from the previous task. Write another coroutine called async_comprehension that utilizes an async comprehension over async_generator to collect 10 random numbers. The coroutine should return the list of 10 random numbers.
2. Run time for four parallel comprehensions

Import the async_comprehension coroutine from the previous task. Implement a measure_runtime coroutine that executes async_comprehension four times in parallel using asyncio.gather. The measure_runtime coroutine should measure the total runtime for executing the four async comprehensions and return the total runtime.



