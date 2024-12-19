# Context managers are tools for resource management, which allow you to allocate and release resources when you need to. The "with" keyword is the recommended way to implement context management, as it automatically closes the file (even if an exception occurs) to free up resources and is easy to read! 
with open("test_doc.txt", "w") as file:
    file.write("dfnejkwfbne7gf3i2brf")

# opening and closing databases, as well as "Locking" the GIL when using threads/processes are other popular examples of using context managers

# ||| Context managers for custom classes should use __enter__ and __exit__ methods. This class does the same as above, but its a good demo for showing how you can create your own logic in a class to do the same thing:
class ManagedFile:
    def __init__(self, filename):
        print("init")
        self.filename = filename

    # executes when entering "with" statement to allocate our resources
    def __enter__(self):
        print("enter")
        self.file = open(self.filename, "w")
        return self.file

    # correctly close file
    def __exit__(self, exception_type, exception_value, exception_traceback):
        if self.file:
            self.file.close()
        # if we have an exception we can see those values here
        print(f"exception type: {exception_type}\nexception value: {exception_value}")
        print("exit")

# using with the correct way does everything we anticipate:
with ManagedFile("test_doc.txt") as file:
    print("with ManagedFile occurring")
    file.write("this is now the file text....")

print("continuing....")

# using with to cause an exception to see the difference:
with ManagedFile("test_doc.txt") as file:
    print("with ManagedFile exception occurring")
    # NOTE: since our __exit__ class method properly closes the file, we have no worries about it being open. This is very good practice!
    # incorrect: causes attribute error because file object has no method called xxx.
    # file.xxx("this is now the file text....")


# ||| Context managers can also be used on functions. This means importing the contextlib module and using the contextmanager decorator on our function
from contextlib import contextmanager

# must take in the decorator
@contextmanager
# generator function
def open_managed_file(filename:str) -> None:
    f = open(filename, "w")
    # we can write to the file by allocating our resource (or try to anyway)
    try:
        yield f
    # this is like the __exit__ method because anything in the finally scope always gets executed, so we need to close our file here 
    finally:
        f.close()

# now use the function to write
with open_managed_file("test_doc.txt") as f:
    f.write("foewnfneowioewifn")