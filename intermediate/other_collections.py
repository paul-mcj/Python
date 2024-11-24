# Collections: are more types beyond the built in ones (like list, tuple, set, etc.)
from collections import Counter, namedtuple, defaultdict, deque

def main():
    # NOTE: counter: will return a dictionary counting the amount of times each item occurs in a dataset
    nums = [23,23,23,67,81]
    nums_counter = Counter(nums)
    print(nums_counter)

    letters = Counter("ashofenwfonwjvfbwerygewrinbgfoedwncvioewdfioew");
    print(letters)
    print(nums_counter.values())

    # two most common counts
    print(letters.most_common(2))

    # convert each unit of the original data type as a new element -- should convert to list otherwise it will ive object memory address
    print(list(letters.elements()))

    # NOTE: namedTuple: lightweight way to create a simple class without defining an actual class
    # remember tuples are immutable and cannot change. si if you need method support for your class, a regular class is more appropriate. namedTuples help when you need something class-like that is also quick, simple and definite.
    Car = namedtuple("Car", ["make", "model", "year"])
    car1 = Car("Honda", "Accord", 2005)
    print(car1)

    # NOTE: defaultdict: can set default values for keys depending on type passed into method. Normal dictionaries give errors if trying to access a key that doesn't exist, default dictionaries give you the default value of the default type.
    default_dict = defaultdict(int)
    default_dict["a"] = 1
    print(default_dict["b"]) # "b" doesn't exist, so "0" is returned

    empty_name = defaultdict(str)
    empty_name["first"] = "Paul"
    print(empty_name["second"]) # returns whitespace

    # The default type must be callable (ex. list, set, str, function, class, etc.) so it cannot accept Bool, True, False or None for example. If you need to return a boolean for some reason, use a simple lambda function instead:
    false_by_default = defaultdict(lambda: False)
    false_by_default["one"] = True
    print(false_by_default["two"]) # False

    # NOTE: deque: a double-ended queue that can add or remove from both ends. its very efficient.
    deq = deque()
    deq.append("chocolate")
    deq.append("graham cracker")
    deq.append("marshmallow")
    print(deq)

    # add element to beginning
    deq.appendleft("first: start fire")
    print(deq)

    # remove last element
    deq.pop()
    print(deq)

    

if __name__ == "__main__":
    main()