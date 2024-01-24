from functools import lru_cache
import time
import matplotlib.pyplot as plt

execution_times = []


def timer(func):
    total_time = 0  # Initialize the total time

    def wrapper(*args, **kwargs):
        nonlocal total_time  # To modify the total_time in the enclosing scope
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        total_time += end_time - start_time
        execution_times.append(total_time)
        print(f"Finished in {total_time:.10f}s: f({args[0]}) -> {result}")
        return result

    return wrapper


@lru_cache(maxsize=None)
@timer
def fib(n: int) -> int:
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)


if __name__ == "__main__":
    for i in range(101):
        fib(i)


fib_numbers = list(range(101))
plt.figure(figsize=(10, 5))
plt.plot(fib_numbers, execution_times, marker="o")
plt.title("Execution Time for Fibonacci Numbers")
plt.xlabel("Fibonacci Number")
plt.ylabel("Time in seconds")
plt.savefig("fib_times.png")
plt.show()
