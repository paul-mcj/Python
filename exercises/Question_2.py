# Question 2: Write a program which can compute the factorial of a given numbers. The results should be printed in a comma-separated sequence on a single line. Suppose the following input is supplied to the program: 8 Then, the output should be: 40320

num = int(input("Enter an int: "))
fList = []
answer = 1

for nums in range(num):
    if(num == 0):
        break
    if (num == 1):
        fList.append(1)
        break
    else:
        nums += 1
        fList.append(nums)
        answer *= (nums)

print(f"The factorial of {num} is: {answer}")

# need to do this in order to print factors in desc order
fList.reverse()

print(f"Here is a list of the factors: {fList}")


# NOTE: given solution
def fact(x):
    if x == 0:
        return 1
    return x * fact(x - 1)

x=int(input())
print(fact(x))