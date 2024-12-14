# ||| Decorators can modify or enhance another function/class behavior without directly changing its code. A function decorator can add extra functionality to a function -- a class decorator can modify how a class behaves (again, without ever needed to tinker with how the class operates). 
# Part of what makes decorators so useful is that its simply a few lines of code appended on top of a function definition. If you need to add something important to a function but are worried you might break it, then creating a decorator on the side is better, because it can handle something on its own and be used anywhere, and if it messes up with the original function/class, then instead of undoing all kinds of changes, you can comment out a few lines of code and debug.

# Decorator functions themselves are functions that take in other functions/classes as input and return new functions with the modified behavior.

# NOTE: functions that use decorators have their metadata (ex. name, docstrings, etc) replaced by the decorators' wrapper function. Importing from functools can preserve the original functions metadata, helping with debugging. Its recommended to always use this when creating your own decorators.
from functools import wraps

# func argument is another function
def my_decorator(func):
    # preserve wrapped function's metadata
    @wraps(func)
    # positional and keyword arguments can be used to handle functions with varying arguments. Its often recommended to use *args and **kwargs to allow wrapper functions in decorators to be flexible
    def wrapper(*args, **kwargs):
        print("Before running function")
        result = func(*args, **kwargs)
        print("After running function")
        return result
    return wrapper

# As soon as a function uses a decorator, its passed into the decorator as an argument. In this case, say_hello() is used in the decorator's wrapper function.
@my_decorator
def say_hello():
    print("Hello")

say_hello()
print()

@my_decorator
def greet(name, age):
    print(f"Hi, my name is {name} and I'm {age} years old.")

greet("Paul", 30)
print(greet.__name__) # since we imported functools, we can make sure to preserve the name of the function (otherwise, Python would think its being run directly from the decorator "wrapper" function)
print()

# ||| Nested decorators allow multiple decorators on a single function by stacking them
def uppercase(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result.upper()
    return wrapper

def exclaim(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return f"This is the result of exclaim: {result}"
    return wrapper

# NOTE: decorators are applied in bubbling fashion from how they are stacked on top of the function (ie. from inside out). So @uppercase is applied first, then @exclaim
@exclaim
@uppercase
def say(message):
    return message

print(say("hello"))

print()

# ||| there are a number of built-in decorators, too:
# @staticmethod: defines a method that doesn't depend on the instance or class
# @classmethod: defines a method that works with the class instead of an instance
# @property: turns a method into an attribute-style access

# ||| Parameterized decorators can take in their own arguments as well
def repeat(n):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(n):
                func(*args, **kwargs)
        return wrapper
    return decorator

@repeat(5)
def greet_repeat(name):
    print(f"Hi there {name}")

greet_repeat("Alex")
print()

# ||| More common use cases for decorators:
# 1. Logging
def log(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__} with {args} and {kwargs}")
        return func(*args, **kwargs)
    return wrapper

@log
def rectangle(w, h):
    return w * h

print(rectangle(4, 6)) # passing in *args
print(rectangle(w=4,h=6)) # passing in **kwargs
print(rectangle(4, h=6)) # passing in both *args and **kwargs. NOTE: un-named args always have to appear in argument list before keyword arguments.
print()

# 2. Performance management
import time
def timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} took {end - start:.5f} seconds")
        return result
    return wrapper

@timer
def loop_to_billion():
    for num in range(10000000 + 1):
        if num == 10000000:
            return num

print(loop_to_billion())

# NOTE: While decorators are powerful, they can introduce challenges if not used carefully:
#     Overuse: Excessive stacking of decorators can make debugging harder.
#     Performance Overhead: Each decorator adds some overhead, so they should be used judiciously in performance-critical code.
#     Complexity: A poorly written decorator can make behavior unpredictable.

