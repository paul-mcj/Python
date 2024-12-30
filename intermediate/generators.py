# ||| Generators are functions that return iterable objects -- the items inside are created only when individually invoked and only keep the current state of the generator in memory, meaning they are VERY memory efficient. Compare this to a list where all items are stored in memory.
# Generators do not know any values besides the current one, and only know how to find the next value because of the logic defined inside. 
# Since generators are stateful (meaning they can pause/resume and change what they yield based on external conditions) its possible to adjust their behavior/output dynamically during execution. For this reason, generators are considered an advanced concept. 

def my_generator():
    # "yield" pauses the function to RETURN a value. Always remember that its basically a special "return" equivalent keyword.
    yield 1
    yield 2
    yield 3

# instantiate object
g = my_generator()

# NOTE: very powerful part of generators is they can simply call "next" to resume the generator from its paused state.
get_first_value = next(g)
print(get_first_value) # value 1, the "pause" holding up before value 2 and after
print()

# notice how if we now call "next" in the generator it will now give us the second value returned by the second yield
get_second_value = next(g)
print(get_second_value) # value 2, the "pause" holding up before value 3
print()

# can also simply iterate over all values just like normal as this will essentially just call "next" method for all yield statements
for i in g:
    print(i) # 1, 2, 3

print()

# NOTE: generators are exhausted when there are no more values to yield. This means all yield statements have been executed and thus the generator has reached the end of its function script. Since generators retain their execution state between calls to "next", once a generator is done executing its doesn't reset itself. To "reuse" a generator, a new instance is necessary.
# This makes sense since generators don't store all values in memory -- they only create values on demand. Reusing a generator would require saving past values (not just ones in current state).

# ||| For this example, lets compare where we might be better off with a generator over a function.
# we can start with a normal function that takes in a number "n", and gives the sum of all numbers up to "n" (count starting 1, 2, 3, ... "n").
def sum_func(n):
    nums = []
    count = 0
    while count < n:
        nums.append(count)
        count += 1
    return nums

sum_list_a = sum_func(1000)
print(sum(sum_list_a)) # 45

# OK, cool. But lets make a generator to do the same thing:
def sum_gen(n):
    count = 0
    while count < n:
        yield count
        count += 1
        
sum_list_b = sum_gen(1000)
print(sum(sum_list_b)) # 45

# now lets compare the memory size of the function and the generator versions:
from sys import getsizeof

print(getsizeof(sum_list_a)) # 8856 bytes
print(getsizeof(sum_list_b)) # 192 bytes

print()

# There is a pretty negligible difference when "n" is less than 100, but then exponentially scales where the function that uses a list takes up WAY MORE MEMORY than the generator! Since the whole concept is really to just get a value, then having a list is unnecessary. 

# ||| Generator expressions are like list comprehensions, except they use parenthesis not square brackets:
my_generator_expression = (i for i in range(10) if i % 2 == 0)

print(type(my_generator_expression)) # generator

