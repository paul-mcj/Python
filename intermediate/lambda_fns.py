# Lambda functions can be declared and used just as normal functions with def. HOWEVER, lambda functions should be used instead as anonymous functions to evaluate an expression to return a result in one line. If the function becomes complex enough to need at least two lines, DO NOT use a lambda function! 
# They are suitable when you need a quick, one-off function which is especially useful to include as an argument to a high order method.

# discouraged use of lambda (still works, but should be avoided):
add10 = lambda x: x + 10
print(add10(5))

# correct way of using lambda (with multiple args):
print((lambda x,y: x * y)(2, 7))




# NOTE: using lambda with high order methods

# map(fn, seq)
num_list = [1,2,3,4,5,6]
print(list(map(lambda x: x + 10, num_list)))
print([n + 10 for n in num_list]) # list comprehension

# sorted(list, key)
points2D = [(1,2), (15,1), (-6,3), (10,4)]
print(sorted(points2D, key=lambda x: x[0])) # sort by ascending x value in tuples

# filter(fn, seq)
print(list(filter(lambda x: x % 2 == 0, num_list))) # return even numbers
print([n % 2 == 0 for n in num_list]) # list comprehension to give results of filtering for each item (filter method only returns bool)
print([n for n in num_list if n % 2 == 0]) # using conditionals of list comprehension to get same results as lambda

# reduce(fn, seq) -- needs to be imported
from functools import reduce
print(reduce(lambda x, y: x + y, num_list))
