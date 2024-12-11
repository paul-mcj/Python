# generate pseudo random numbers.
import random

# print random float from 0 - 1
a = random.random()
print(a)

# give a range with .uniform
b = random.uniform(1, 10)
print(b)

# there are all kinds of random numbers to generate with different upper ranges, standard deviations, sequences, etc.

# get a single random element from a list
c = list("ABCDEFGHIJ")
print(random.choice(c))

# get a specified number of elements from a list (will never pick the same value twice)
print(random.sample(c, 3)) # 3 random elements
print(random.sample(c, len(c))) # pass in the length of the list, so it will essentially spit out the list in a random order 
random.shuffle(c) # the above is equivalent to using the shuffle method, except the method alters the list in place (meaning it is totally changed in memory -- the sample will select elements from without changing its actual structure) 
print(c)

# get a specified number of elements from a list (*CAN* pick the same value twice)
print(random.choices(c, k=len(c))) # notice how there may be multiples

# ||| Random numbers are reproducible, hence pseudo random. Passing in a value to the seed (can be an int, float, string of None) initializes the RNG and calling the seed value will always give you the same result. This is useful when you need to have consistent outputs for debugging or reproduce a simulation/predictable results but also have some "randomness" to the values.

# As soon as you set a seed, anything that uses the random module will have the same value when run -- so random.random will always be the same, random.randint(1, 10) will produce something else but will always be the same when run, random.choice(list) will always be the same, etc. 
# When you use the same seed, the sequence is predictable because the RNG starts at the same point in its internal state. This gives the appearance that the values are "saved," but in reality, it's just the deterministic nature of the algorithm.
print("\nRandom Seed: 13")
random.seed(13)
print(random.random())
print(random.randint(1, 10))
print(random.sample(c, 3)) # 3 elements from list c

# When you decide to change the seed, a new random "playground" is created and can/will have different values then previous declared seeds
print("\nRandom Seed: bitcoin")
random.seed("bitcoin")
print(random.random())
print(random.randint(1, 10))
print(random.sample(c, 3)) # 3 elements from list c

# If we reset the seed to the one before, you can see that all those random results now mimic the algorithm set from the OG RNG
print("\nRandom Seed: 13")
random.seed(13)
print(random.random())
print(random.randint(1, 10))
print(random.sample(c, 3)) # 3 elements from list c. Notice how this always samples the exact same elements from when we previously seeded the same value!
print()

# NOTE: Since the random module can reproduce results, its best used for testing as its not secure. But for production, you should import the secrets module instead for cryptography, authentication, tokens, passwords, etc.
# This module generates true randomness. The main disadvantage is the algorithm is more processor intensive and thus takes longer to generate a random value. 
import secrets

below = secrets.randbelow(10) # return random int in range 0 to specified
print(below)

bits = secrets.randbits(4) # generates a random int with specified random bit places as the ceiling. Ex: 4 bit places in binary has a ceiling of 1111 which is 15, so the above will return a random int between 0 and 15:
print(bits)

choice = secrets.choice(c) # chooses a truly random elements from a non-zero sequence
print(choice)
