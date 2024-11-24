# iterators can take in an iterable object (ex. list, dictionary, set) and specifically look at each individual element to do something to it and continue the iteration when called upon with "next()" function.

from itertools import product, permutations, combinations, accumulate, groupby

def main():
    # NOTE: product: generates all possible combinations of elements from each iterable. its very memory efficient.
    wing_type = ["flats", "drums"]
    sauces = ["hot", "honey", "dill"]
    print(product(wing_type, sauces)) # see the iterable object type
    print(list(product(wing_type, sauces))) # convert to list iterable
    print(set(product(wing_type, sauces))) # convert to set iterable

    # can use repeats as well
    print(list(product(sauces, repeat=2)))

    # NOTE: permutations: returns all possible orderings
    screwdrivers = ["phillips", "flathead", "robertson"]
    print(list(permutations(screwdrivers)))

    # you can specify shorter length permutations
    print(list(permutations(screwdrivers, 2)))


    # NOTE: combinations: with no repetitions, it lists all combinations of items. it must take in a length argument.
    mtg_colours = ["white", "blue", "black", "red", "green"]
    print("mono color:")
    print(list(combinations(mtg_colours, 1)))
    print("\nguilds:")
    print(list(combinations(mtg_colours, 2)))
    print("\nshards/wedges:")
    print(list(combinations(mtg_colours, 3)))
    print("\n4-color:")
    print(list(combinations(mtg_colours, 4)))
    print("\nwubrg:")
    print(list(combinations(mtg_colours, 5)))


    # NOTE: accumulate: iterator returns sums of all previous items. strings will essentially concatenate, numbers will add.
    fabrics = ["silk", "cotton", "leather", "polyester"]
    print(list(accumulate(fabrics)))
    acc_nums = [10,2,5,50,10,13]
    print(list(accumulate(acc_nums)))

    # NOTE: groupby: by taking in a key function, it can group elements in the iterator
    def smaller_than_11(x):
        return x < 11
    group_obj = groupby(acc_nums, key=smaller_than_11)
    for key, value in group_obj:
        print(key, list(value))





if __name__ == "__main__":
    main()