import time
import random


# Task 1
def measure_time(func):
    def inner_function(*args, **kwargs):
        start = time.time()
        func(*args, **kwargs)
        end = time.time()
        runtime = end - start
        return runtime

    return inner_function


# Task 2
def function_logging(func):
    def inner_function(*args, **kwargs):
        func_result = func(*args, **kwargs)
        if len(args) == 0 and len(kwargs) == 0:
            print(f'Function {func.__name__} is called with no arguments')
        elif len(args) == 0:
            print(f'Function {func.__name__} is called with keyword arguments: {kwargs}')
        elif len(kwargs) == 0:
            print(f'Function {func.__name__} is called with positional arguments: {args}')
        else:
            print(f'Function {func.__name__} is called with positional arguments: {args} '
                  f'and with keyword arguments: {kwargs}')
        print(f'Function {func.__name__} returns output of type {type(func_result).__name__}')
        return func_result

    return inner_function


# Task 3
def russian_roulette_decorator(probability, return_value):
    def decorator(func):
        def inner_function(*args, **kwargs):
            func_result = func(*args, **kwargs)
            prob = random.random()
            if prob >= probability:
                return func_result
            else:
                return return_value
        return inner_function
    return decorator
