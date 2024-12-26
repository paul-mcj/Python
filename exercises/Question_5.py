# Question 5: Define a class which has at least two methods: getString: to get a string from console input printString: to print the string in upper case. Also please include simple test function to test the class methods.

class Mouse():
    def __init__(self):
        self.the_string = ""

    def getString(self):
        self.the_string = input()

    def printString(self):
        print(self.the_string.upper())

mouse_1 = Mouse()
mouse_1.getString()
mouse_1.printString()