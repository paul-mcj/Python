original = 5

# creates a new variable with the same reference! This is not a problem, as integers are immutable
copy = original
print(f"copy: {copy}")

# copy can easily change its pointer to reference something else (ie. its independent of original)
copy = 6
print(f"copy: {copy}")
print(f"original: {original}")

# this works differently than with mutables like lists:
animals = ["dog", "cat", "bird"]
copy_animals = animals
copy_animals[0] = "bear"

# Uh oh! the animals has also changed, even though the change was made via copy_animals! this is because the assignment doesn't make a true copy, it literally assigns the same object in reference!
print()
print(f"animals: {animals}")
print(f"copy_animals: {copy_animals}")

# ||| There are lots of ways to perform shallow copying: one level deep, only references direct nested child objs

# one way is to use the copy module
from copy import copy as copy_func
true_animal_copy = copy_func(animals)
true_animal_copy[0] = "tiger"

# the true_animal_copy is independent from animals and can now be mutated and not affect the original!
print()
print(f"animals: {animals}")
print(f"true_animal_copy: {true_animal_copy}")

# can also use list () method:
print()
animals_list = list(animals)
animals_list[0] = "giraffe"
print(f"animals: {animals}")
print(f"animals_list: {animals_list}")


# can also use list slicing (which is close to the spread operator in JS to copy):
print()
animals_slice = animals[:]
animals_slice[0] = "monkey"
print(f"animals: {animals}")
print(f"animals_slice: {animals_slice}")

# ||| If you need to copy a nested collection, then the above methods of shallow copying simply will not work. This is where you need to perform deep copying (ie. making a full independent copy)
# NOTE: deep copying is much more complex than shallow copying. you can use JSON or pickling serialization, or create custom methods to create copies of objects. But, the most common and easiest way is to simply use the deepcopy method from the copy module
from copy import deepcopy

# make a nested list and make a deepcopy, then modify the deep copy and see that the original is unchanged:
print()
nested_animals = [animals, animals_slice]
copy_nested_animals = deepcopy(nested_animals)
copy_nested_animals[0][2] = "rabbit"

print(f"nested_animals: {nested_animals}")
print(f"copy_nested_animals: {copy_nested_animals}")

# NOTE: if you want to create copies of class instances, it follows the same rules as above: shallow copying is okay if the object instance is only "one-layer deep", but if it is used in another class for example, then a deep copy MUST be made to keep the copies independent!