import time


def log_execution(func):
    def wrapper(*args, **kwargs):
        print(f"Executing: {func.__name__}")
        print(args[0], args[1], kwargs.keys())
        result = func(*args, **kwargs)
        print(f"Completed: {func.__name__}")
        return result

    return wrapper


@log_execution
def my_function(x, y, **wello):
    print("Doing something...")
    print(x + y)
    return 42


# my_function(7, 8, one=1, two=2)
cache = {}


def memoize(func):
    def wrapper(*args, **kwargs):
        key = args[0]  # (func.__name__, args, kwargs)
        if key not in cache:
            result = func(*args, **kwargs)
            cache[key] = result
        return cache[key]

    return wrapper


@memoize
def fibonacci(n):
    if n in (0, 1):
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


# Calculate and cache Fibonacci numbers
s = time.time_ns()
print(fibonacci(20))
e = time.time_ns()
print(f"{e*0.000001 - s*0.000001:.2f}")


s = time.time_ns()
print(fibonacci(35))
e = time.time_ns()
print(f"{e*0.000001 - s*0.000001:.2f}")


s = time.time_ns()
print(fibonacci(35))
e = time.time_ns()
print(f"{e*0.000001 - s*0.000001:.2f}")


s = time.time_ns()
print(fibonacci(35))
e = time.time_ns()
print(f"{e*0.000001 - s*0.000001:.2f}")


s = time.time_ns()
print(fibonacci(35))
e = time.time_ns()
print(f"{e*0.000001 - s*0.000001:.2f}")
