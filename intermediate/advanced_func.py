# ||| Forced keyword args: anything after the * must be a keyword arg otherwise an error occurs. So when invoking this function, you MUST have a keyword argument for "last"
def foo(*args, last):
    for arg in args:
        print(arg)
    print(last)

# foo(1, 2, 3, 4, 5) # error: required keyword for "last"

foo(1, 2, 3, 4, last=5) # this works!

# ||| Unpacking args: prefix a list with the * when invoking the function
def bar(*args):
    print(args)

my_list = [1, 2, 3, 4, 5]

bar(*my_list) # applies function to each item in list

# unpacking dicts must have names in arguments that match keys and is prefixed with ** when unpacking in function invocation.
# NOTE: the same amount of parameters must match the same amount of arguments for dicts -- you cannot use *args here:
def coffee(cream, sugar):
    print(cream, sugar)

my_coffee = {"sugar": False, "cream": 2}

coffee(**my_coffee) # notice how even though the dict was defined with sugar first, the function has sugar second so thats the way it will output it

# NOTE: using *args doesn't work (as that is for POSITIONAL arguments), but **kwargs works with dictionaries perfectly fine and is useful when a function is passed a dictionary with an unknown amount of keys/key names:
def unknown_coffees(**kwargs):
    for key in kwargs:
        print(kwargs[key])

unknown_coffees(**my_coffee) # This gives us False and 2

my_mac = {"battery": 46, "bluetooth": True, "wifi": True, "mirroring": False, "day": "Wednesday"}

unknown_coffees(**my_mac) # the function that unpacks dictionaries works for dictionaries that are completely different in key names as well as lengths

# ||| Local vs. Global vars
nutcrakers = 24

def nutcracker_count():
    global nutcrakers
    inside = nutcrakers 
    # using the global keyword allows us to modify the variable. If it wasn't set, then a local variable of this function would be made
    nutcrakers = 26
    print(f"variable 'inside' with function value: {inside}")

print(F"nutcrackers value before function: {nutcrakers}")
nutcracker_count()
print(F"nutcrackers value after function: {nutcrakers}")

# ||| Parameter passing: immutable objects (ex. lists) can be modified in a function. This is because objects are passed as parameters by reference, so the literal object in memory will be changed:
def change_country(list):
    list.append("Brazil")

countries = ["UK", "Spain", "Japan"]

print(countries) # prints whats expected

change_country(countries)

print(countries) # now countries is changed in memory

# NOTE: if you need to create a copy and not modify the object in literal memory, simply reassign the parameter in the function to a copied list by slicing:
def update_country_again(list):
    updated_list = list[:] # create a local variable
    updated_list.append("Canada")
    return updated_list

copy_countries = update_country_again(countries)

print(countries) # unchanged in memory
print(copy_countries) # modified copy

# ||| * operator used to do a lot in Python: 
# multiplication and exponentiation; 
# *args and **kwargs

# create lists, tuples or strings with repeated elements
zero = [0] * 10
print(zero)

holidays = ("xmas", "easter", "Canada Day") * 2
print(holidays)

# unpacking containers into elements (similar to the rest ... operator in JS) 
# NOTE: unpacking ALWAYS results in a list (even if the original container is a tuple, set, etc.)
list_of_nums = [33, 6.8, 9, 99, 5, -66, 8432]

*beginning, penultimate, last = list_of_nums

print(beginning)
print(penultimate)
print(last)

# the * can be placed anywhere when unpacking: below it will be every element thats not the first or last in the list
beg, *mid, fin = list_of_nums
print(mid)

# merge iterables (NOTE: you can merge into lists, tuples, sets, dicts, etc. You do this by demarcating the brackets)
tuple_1 = ("g", "g")
tuple_2 = ("w", "w")

new_tuple = (*tuple_1, *tuple_2) # type tuple
new_list = [*tuple_1, *tuple_2] # type list
new_set = {*tuple_1, *tuple_2} # type set

print(type(new_set))

qwerty = {"a": 1}
ytrewq = {"a": 555}
merge_dict = {**ytrewq, **qwerty}
print(merge_dict) # NOTE: if dicts have the same key when merging, the last dictionary unpacked in sequential order updates last, thus for this example the value of key "a" is 1