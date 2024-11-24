from pet import Pet
from cat import Cat
from dog import Dog

def main():
    chubby_wubby = Pet("cat", "Camo", 10)
    chubby_wubby.call_name()

    bo = Cat("cat", "Bowster", 10, True)
    bo.likes_yarn()

    allen = Cat("cat", "Allen", 13)
    allen.likes_yarn()
    print(repr(allen))
    print(str(allen))

    denver = Dog("dog", "Denver", 2)
    print(repr(denver))
    print(str(denver))

    # since the name property has been set as "read only" in the Pet constructor (which is a Dog superclass), you cannot alter it after initialization, so the statement below will cause an error:
    # denver.name = "charlie"

    # NOTE: recognize that even though the attribute is private in the constructor (ie. "__name"), you can't have the underscores there, accessing just the variable name is required:
    print(denver.name)

    # also note that while you can't change the attribute "name", you CAN change the "__name" for the object, BUT since the object has already be instantiated, the reassignment is ignored as opposed to throwing an error:
    denver.__name = "charlie"
    print(denver.name) # Denver

    # using setter methods are the correct way to alter a property:
    # denver.name = "Jizzanthepuss" #this throws exception in setter method
    denver.name = "charlie"
    print(denver.name) # charlie

    # encapsulated methods CAN change the name property -- changing it DIRECTLY is only possible via setter method:
    denver.dark_side()
    print(denver.name)

    # this method is private, so it will cause an error if you try to invoke it:
    # print(allen.prep_body())

    # however, this method calls other methods within the class and can be accessed. those hidden methods are ABSTRACTED. this is similar to encapsulation, where you want to restrict important class attributes and methods to other developers using the class.
    print(allen.send_email())

    # notice how allen is a Cat and Denver is a Dog. Both can use a method like send_email. This is POLYMORPHISM in action!



if __name__ == "__main__":
    main()