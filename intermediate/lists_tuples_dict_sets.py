def main():
    # NOTE: Lists: ordered, mutable, allows duplicates

    players = ["giroux", "norris", "jensen", "zub", "ullmark", "chabot", "jbd"]

    # this is a neat trick to reverse a list:
    print(players[::-1])

    copy_players = players
    del copy_players[2]
    # since both lists refer to the same one in memory, changing either one will change the other:
    print(copy_players)

    # to get a proper copy:
    new_copy_players = players.copy()
    del new_copy_players[0]
    print(new_copy_players)
    print(players)

    # list comprehension can make a new list from an existing one in a simply way:
    # NOTE: it is very similar to how map() works in JS
    powerplay = ["powerplay: " + player for player in players]
    print(powerplay)

    # list comprehensions also allow for extra functionality inside. Lets filter for players who have a name less than 7 characters:
    filter_names = [player for player in players if len(player) < 7]
    print(filter_names)

    # NOTE: Tuples: ordered, immutable, allowed duplicates
    shawshank = ("Shawshank Redemption", 1994, "movie")
    print(shawshank)

    # unpacking (like spreading in JS)
    name, year, medium = shawshank
    print(year)

    # with unpacking, as long as there is at least one other unpacked reference, you can use an asterisk to be a placeholder for all other values of the tuple (or list) 
    *all, x = shawshank
    print(*all)

    # you can make tuples with the tuple() function if the argument is an iterable
    tuple_players = tuple(players)
    print(tuple_players)
    print(tuple_players[(len(tuple_players) - 1)])

    print([p for p in tuple_players])

    if "giroux" in tuple_players:
        print("yes")

    # tuple slicing:
    powerkill = tuple_players[1:3]
    print(powerkill)

    print(hash(powerkill))

    # NOTE: Dictionaries: key-value pairs (no duplicates of keys, but duplicates of values is fine), unordered (accessed by key not index) and are mutable
    planets = {"pluto": 5, 3.4: "red", "saturn": "rings"}
    print(planets[3.4])

    # if you need a copy that points to its own space in memory, use the copy() function, otherwise if you just assign a new variable to an existing dict and modify, it will modify the dict in memory
    copy_planets = planets.copy()
    print(copy_planets)



    # tuples are more efficient than lists, taking up less memory and being quicker to create data. dictionaries are also more efficient as lists as they are also hashable like tuples, but not quite as efficient as tuples.
    import timeit
    print(timeit.timeit(stmt="[0,1,2,3]", number=1000000))
    print(timeit.timeit(stmt="(0,1,2,3)", number=1000000))
    print(timeit.timeit(stmt=f"{{0:0,1:1,2:2,3:3}}", number=1000000))

    # NOTE: sets: unordered, mutable, no duplicates (any duplicate will be ignored)
    models = {"iphone 13", "galaxy 20", "iphone 13", "iphone 15x"}
    print(models) # returns unordered set
    print(len(models))

    models.remove("iphone 13")
    print("\n")
    print([model for model in models])

    samsung = {"galaxy 10+", "galaxy 20"}

    # sets union() method will "merge" sets but ignore duplicates
    print(models.union(samsung))

    # the intersection() method will see what is common between two sets
    print(models.intersection(samsung))

    # difference() sees what is in the first set that is not in the second
    print(models.difference(samsung))

    # symmetric_difference() method will "merge" the two but NOT include things that are common to each set
    print(models.symmetric_difference(samsung))

    # frozenset() will make an immutable set, so it can't be changed after initialized.
    compass = frozenset({"N", "E", "S", "W"})
    print(compass)


if __name__ == "__main__":
    main()