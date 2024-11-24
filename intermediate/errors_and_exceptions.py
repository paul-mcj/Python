# Python programs terminate when an error occurs, so exceptions can be used to handle these 

def main():
    user_input = int(input("Enter a number: "))
    if user_input < 0:
        # exception will be called and line number will be shown -- by default any Exception class called can receive a message as a first argument
        raise Exception("number should be positive")
    
    # assertion errors will be raised if its not true -- you can add a custom message as well
    assert(user_input < 10), "number needs to be less than 10"

    # try // except block can continue the program after the exception block is run, so by passing things that might get stuck in the try block can be very useful, particularly for fetching data
    try:
        a = 5 / 0 # will trigger error
    except Exception as e:
        print(f"dividing by zero isn't possible: {e}")

    # you can try to do multiple things in a try block, and depending on specific exceptions (of which there could be multiple), the FIRST STATEMENT TO TRIGGER will cause the respective exception to trigger
    try:
        b = [1,2,3] 
        b[5] # index error
        a = 5 + "5" # type error
    except IndexError as e:
        # as it stands, the index error will print because it triggers in the try block before the type error does
        print(e)
    except TypeError as e:
        print(e)
    
    # else blocks will run after a try // except block if nothing in the corresponding try is triggered (otherwise, the except is run as expected):
    try:
        coffee = "yum"
    except Exception as e:
        print(e)
    else:
        print("no exception for coffee :)")
    # the finally block will always run, regardless of if try, except, or else is run. this is used as the "cleanup" stage
    finally:
        print("finally")

    # sometimes, its better to define a custom error -- in this case, create a new class and have it take in Exception as a base class
    # if doing this, always try to keep the class as concise as possible
    class ValueTooHighError(Exception):
        pass

    # it can do anything a normal class can do, so you can customize it with class variables, constructors, static methods, etc. 
    class ValueTooLowError(Exception):
        def __init__(self=object, message=str, value=str) -> object:
            self.message = message
            self.value = value

    def test_value(x):
        if x > 100:
            raise ValueTooHighError("value is too high")
        if x < 50:
            raise ValueTooLowError("too low: ", x)

    try:
        # NOTE: again, depending on what is caught first in the try block, this will trigger certain exceptions 

        # test_value(200)
        test_value(40)

    except ValueTooHighError as e:
        print(e)
    except ValueTooLowError as e:
        print(e.message, e.value)

    # NOTE: custom exceptions are useful because it gives other devs who work with your code more information about what exactly is occurring when something goes wrong in the program

if __name__ == "__main__":
    main()