# Question 4: Write a program which accepts a sequence of comma-separated numbers from console and generate a list and a tuple which contains every number. Suppose the following input is supplied to the program: 
# 34,67,55,33,12,98 
# Then, the output should be: ['34', '67', '55', '33', '12', '98'] ('34', '67', '55', '33', '12', '98')

user_input = input("Enter comma separated list of ints: ")

# replace commas with empty space
clean_str = user_input.split(",")

print(list(clean_str), tuple(clean_str))