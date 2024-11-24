import json
import csv

# Python classes - OOP Beginners course w. free code camp on youtube
# 1. basics
# 2. class attributes and @classmethod
# 3. Keep track of all instances of a class and working with .csv, and factories
# 4. __repr__ and JSON-like data
# 5. @staticmethod
# 6. parent classes, child classes and inheritance



# 1. basics
class Device:
    # method -- notice how "self" is needed, its kinda like JavaScript "this"
    def calc_total_price(self, p, q):
        return p * q
    
item1 = Device()
print(type(item1)) # notice the class instance of type Device
item1.name = "iPhone"  
item1.seller = "Apple Store"
print(item1.seller); # Apple Store
item1.price = 100
item1.quantity = 5
print(item1.calc_total_price(item1.price, item1.quantity)) # 500

item2 = Device()
item2.name = "Laptop"    
item2.price = 1000
item2.quantity = 3
print(item2.calc_total_price(item2.price, item2.quantity)) # 3000

# notice how above item1 has a seller property but item 2 does not. If you want to force an instantiated object to have specific properties you can by using the __init__ method (this is similar to making a JavaScript constructor method):
# NOTE: there are a lot of methods that start and end with the double underscore. These are called "magic methods" and all have their use cases
class Player:
    # this constructor will automatically run when an object is instantiated for this class
    # NOTE: you can give parameters "type annotations" (like name should be a string). However, python does not do type checking by default so you can still instantiate with a boolean for name as an example and there won't be an issue. These type annotations are more for readability. But, there are libraries out there that will force type checking at runtime (not compile time -- they aren't quite as good as TypeScript at catching errors).
    def __init__(self, name: str, number, goals=0, assists=0):
        print(f"Number {number}, {name}, has scored {goals} goals and {assists} assists in tonights game")
        # notice how after self parameter, you can list mandatory arguments (otherwise there will be an error if trying to instantiate an object with missing arguments). This means we can avoid specifically attributing properties one line at a time like the Device() class above, but only if we also make sure that once instantiated each new object can have dynamic assignment of properties. Its very similar to assigning this.property in JavaScript.
        # Also note that we can make sure the constructor validates arguments of these properties. Use the "assert" statement/keyword. You can also pass in a second argument to an assert statement that will run if it is caught on object instantiation (see player3 example).
        assert goals >= 0, f"Goals {goals} is not greater than 0!"
        assert assists >= 0
        # now if you try to give any Player() negative goals or assists it will cause an assertion error.
        # NOTE: whenever you define a property where "self" is involved that is called an instance attribute!
        #  NOTE: always make sure to assert before assigning instance attributes in the constructor, as it can avoid potential inconsistencies later on.
        self.name = name
        self.number = number
        self.goals = goals
        self.assists = assists

    # if you assign instance attributes in the constructor as above, then it makes it easy to work with specific values in methods simply by referring to self (as self is equivalent to "this" in JavaScript)
    def total_points(self):
        return self.goals + self.assists

# we can see __init__ was invoked
player1 = Player("Tim Stuzle", 18, 1) # NOTE: notice how we gave both goals and assists default values in the constructor. We *can* instantiate objects without either of these properties being explicitly declared as our defaults will kick in.
print(player1.name) # this only works because of line 34 above (if that line didn't exist, it would be an attribute error)
print(player1.assists)

player2 = Player("Nate Mackinnon", 29, 2, 6)
player1.is_senator = False # NOTE: you can always add more attributes to objects *after* instantiation
print(f"{player2.name} has {player2.total_points()} points!")

# since the -4 is placed below and would catch the assert exception, the program stops running -- uncomment to see it in action
# player3 = Player("Claude Giroux", 28, -4, 3)










# 2. Class attributes are defined in the class body itself (not as a method), and thus any instance of that class can access it. 

# If a class attribute is changed in the class, all instances receive that change. For this reason, it is important to note that you should only ever have methods that can change class attributes when they are explicitly decorated with the syntax "@classmethod". This decorator makes python aware that the class itself is passed as the first argument (as opposed to self when instance attributes are assigned), and also makes it move obvious to others reading your code what the intention is.
class Samurai:
    # class attribute
    game = "Ghost of Tsushima"
    buff = 1.25 # 25%

    # constructor
    def __init__(self, name: str, lvl: int, stance: str, bow_accuracy: float):
        # type assertions for instance attributes
        assert type(name) == str, print(f"argument {name} must be a string")
        assert type(lvl) == int, print(f"argument {lvl} must be an int")
        assert type(stance) == str, print(f"argument {stance} must be a string")
        assert type(bow_accuracy) == float, print(f"argument {bow_accuracy} must be a float")

        self.name = name
        self.lvl = lvl
        self.stance = stance
        self.bow_accuracy = bow_accuracy

    # method for string format opp. __repr__
    def status(self:object) -> None:
        print(f"{self.name} is level {self.lvl}, primarily uses {self.stance} stance, and has a bow accuracy of {self.bow_accuracy}")

    # method for level up by one
    def level_up(self) -> None:
        self.lvl = self.lvl + 1

    # this method aims to improve an instance of the Samurai class, specifically by increasing bow_accuracy by 25% -- notice how it can use a class attribute in an instance function (the reverse is not possible). # NOTE: even though "buff" is a class level attribute, make sure to still refer to "self.buff", otherwise you won't be able to change that on an instance-level basis later on (using Samurai.buff for example makes any class instance always refer to the exact same class attribute of buff -- but referring to self means any instance can changes its own buff attribute independent of other instances)
    def concentration(self):
        self.bow_accuracy = self.bow_accuracy * self.buff
    
    # class method to change class attribute
    @classmethod
    def change_game(cls, value):
        cls.game = value


# NOTE: we didn't even declare an instance of the Samurai class yet, but the class attribute is available always
print(Samurai.game)
jin = Samurai("Jin", 67, "moon", 94.44)
umezawa = Samurai("Umezawa", 85, "jitte", 10.0)
umezawa.status()
umezawa.level_up()
print(umezawa.lvl)
umezawa.level_up()
umezawa.status()
print(umezawa.game)
print(jin.game)

# notice how umezawa changed the game (which is a class variable), but both he and jin now have it changed because this came from an @classmethod!
umezawa.change_game("Assassin's Creed")
print(umezawa.game)
print(jin.game)

# NOTE: the below method is built into every class declaration, and allows you to see all attributes that belong to the class by returning a dictionary. For classes themselves, it reveals all the attributes as well as their place in memory
print(Samurai.__dict__)
# see the difference between that and when called on an instance of the class: this returns only instance attributes (NOT class ones). Its a very easy way to get all current properties -- in a way, its a dictionary of what our "status()" function does.
print(jin.__dict__)

# call concentration method!
umezawa.concentration()
umezawa.status()

# you can also overwrite class attributes for an instance (which will not manipulate it for other class instances):
umezawa.buff = 2.5 # 2.5x as good now!
umezawa.concentration()
umezawa.status()

# you can see jin buff is not changed, even thought we could apply umezawa's
print(jin.buff)





# 3. Keep track of all instances of a class and working with .csv
class Chip:
    # make a class attribute of an empty list
    all_chips = [] 

    def __init__(self, brand, flavour, size, price):
        # pretend asserts are here...
        self.brand = brand
        self.flavour = flavour
        self.size = size
        self.price = price

        # since anything in the constructor is run automatically when an instance is declared, we can just add the instance to our class attribute. But this time, we want to make sure we reference the class itself and not an instance:
        Chip.all_chips.append(self)

    # now lets say we want to apply a discount only to a certain flavour of chips
    def discount(self):
        if self.flavour == "Regular":
            self.price = self.price - 0.50
            print(self.price)
        else:
            print("pass")
            pass

    # say we have a csv (chips.csv) and we want each record to become a Chip instance
    # we can create instances with this factory method
    @classmethod    
    def instantiate_from_csv(cls):
        # this will get us the content of our chips.csv file. it basically says open that file and pass "read" permission to the file
        with open("chips.csv", "r") as target_csv_file:
            # now we can get our content converted into a list of dictionaries
            # NOTE: DictReader function automatically interprets the first row of a csv file as headers, so any lines of csv code beneath will be properly used instead
            reader = csv.DictReader(target_csv_file)
            # lets also put this into a list
            csv_chips = list(reader)

        # now use that list and make each dictionary a Chip object
        for item in csv_chips:
            Chip(
                brand=item.get("brand"),
                flavour=item.get("flavour"),
                size=item.get("size"),
                # not a bad idea to force coercion if we know we expect a dedicated type
                price=float(item.get("price")),
            )
    
    # now lets say we want to return all instances of Chip of a certain brand by allowing a passed in argument for brand_value
    @classmethod
    def get_brand(cls, brand_name:str) -> list:
        # we can filter out any instance that doesn't match the argument
        # NOTE: lambda is kinda of like an inline arrow function in JavaScript: it is used to define small and anonymous functions
        return (list(filter(lambda chip: chip.brand and (chip.brand == brand_name), cls.all_chips)))
    
    # NOTE: say we want to get a JSON-like representation of our object instance(s), then using the __repr__ magic method is useful. Essentially, when we call the __repr__ method on an instance of this class, it will return what we define below which could be anything. This is useful mainly for printing and debugging purposes:
    def __repr__(self):
        return f"{{\"brand\": \"{self.brand}\", \"flavour\": \"{self.flavour}\", \"size\": \"{self.size}\", \"price\": {self.price}}}"

chip1 = Chip("Lays", "Ketchup", "250g", 3.99)
chip2 = Chip("Humpty Dumpty", "Regular", "250g", 4.50)
chip3 = Chip("Lays", "Dill Pickle", "30g", 0.99)
chip4 = Chip("Selection", "Regular", "200g", 1.98)
chip5 = Chip("Ruffles", "All Dressed", "620g", 7.79)

# now that each instance has been added to a list of the class, we can do neat stuff like lets get a list of all the flavours:
for chip in Chip.all_chips:
    print(chip.flavour)

# we get pass because this instance is Ketchup
chip1.discount()
# we get the discount because this instance is Regular
chip2.discount()

# retrieve a list composed of all matching instances of brand = "Lays". NOTE: it will retrieve us data in a format our defined __repr__. This get_brand method allows any string argument, so its reusable at least for finding brands on instances, it dones't need to be "Lays" all the time...
print(Chip.get_brand("Lays"))

# now lets try to instantiate some records from the csv file and print them out -- we will get some dictionaries because thats what we coded into the class method:
Chip.instantiate_from_csv()






# 4 __repr__ and JSON data

# using __repr__, we can see string JSON-like data for one specific instance because we defined that __repr__ method in the class:
print(chip2.__repr__)

print("\n")

# we can also loop through the entire class to get all *individual* __repr__ JSON-like data:
for chip in Chip.all_chips:
    print(repr(chip))

print("\n")

# NOTE: This is all well and good for debugging, but everything above regarding JSON-like data is just that: JSON *LIKE* data. the __repr__ defined function is just a tool we can use but it doesn't do anything with actual JSON. 
# NOTE: If we want to use actual JSON conversion, "import json" module and use the dumps() method specifically on an object instance using the __dict__ method:
print(json.dumps(chip2.__dict__))
print("\n")

# now we can convert all class instances to actual json data with a few steps:
all_chip_instances = [ch.__dict__ for ch in Chip.all_chips]
chip_data = {"Chips.all_chips": all_chip_instances}
# chip_data is now fully JSON data!! we can print below to see:
print(json.dumps(chip_data, indent=4))

# TODO: now lets write that JSON data to a new file








# 5. @staticmethod
class Candybar:
    all = []
    manufacturer = "Mondelez"

    def __init__(self:object, name:str, size:str, rating:float) -> None:
        # NOTE: in candybars.csv, one of the records has a string of 15 instead of an int for rating on purpose. we can assert for validation, but we will also need to validate in the classmethod that instantiates our instances
        assert type(rating) == float, print(f"looks like there is an error with rating: {rating} -- must be a float")

        self.name = name
        self.size = size
        self.rating = rating

    # lets make some objects from the candybars.csv file in this factory method
    @classmethod
    def create_candybar_instances(cls:object) -> None:
        with open("candybars.csv", "r") as target_csv_file:
             reader = csv.DictReader(target_csv_file)
             csv_candybars = list(reader)
        
        for bar in csv_candybars:
            Candybar(
                name=bar.get("name"),
                size=bar.get("size"),
                # convert to int to meet the requirement of the assert statement in the constructor
                rating=float(bar.get("rating")),
            )
        Candybar.all = csv_candybars
        print(csv_candybars)

    # NOTE: static methods have logical connections to the class but are not based on instances either, so they DO NOT take in "self" or "cls" as arguments. static methods are kinda just like "regular functions" that happen to sit inside the class because it shares some kind of logical grouping.
    # this static method wants to check if an argument string has more than 7 characters in it
    @staticmethod
    def longer_than_seven_chars(name:str) -> bool:
        return True and len(name) > 7 
    
    def __repr__(self):
        # generic way to return the exact name of the class of the object instance
        return self.__class__.__name__

# call factory method to make some instances
Candybar.create_candybar_instances()

# NOTE: notice how the static method can be used just by passing it a string argument. How does this differ than just making a outside function? It might be considered logically grouped to this Candybar class because maybe we want to grab all candybars that have a name longer than 7 characters, and then do something with all of them.
print(f"The name 'Mars' is name longer than 7 chars: {Candybar.longer_than_seven_chars("Mars")}")
print(f"The name 'Jersey Milk' is longer than 7 chars: {Candybar.longer_than_seven_chars("Jersey Milk")}")


# NOTE: so whats the difference between @classmethod vs @staticmethod?
# static methods have something to do with the class, but do not take in the class or an instance of the class as an argument. this is because the method itself is stateless and does not rely on any instance or class-specific data to operate.
# class methods have something to do with the class as well, but take in "cls" as the first argument because often you want to manipulate some data structure or class attribute of the class








# 6. parent classes, child classes and inheritance
# say we have a granola bar that has all the same attributes as a Candybar, but with a few additional attributes. Instead of creating an entirely new class, we can use inheritance:
class Granolabar (Candybar):
    def __init__(self, name, size, rating, health_level=0):
        # needs to call super function to have access to all parent methods and attributes
        super().__init__(name, size, rating)

        # assign specific Granolabar attributes that aren't inherited
        self.health_level = health_level

# Granolabar instance
gran1 = Granolabar("Kashi", "normal", 6.5)

# this is an attribute that does not belong to superclass
gran1.health_level = 5
print("\n")

# can use methods of superclass no issue. With this __repr__ specifically, we can see what class it is (notice its "Granolabar")
print(gran1.__repr__)

# now notice that if we make an instance of Candybar, the __repr__ method says "Candybar"
alternate_candybar = Candybar("alternate", "big boi", 11.11)
print(alternate_candybar.__repr__)

# we can also see attributes of super class, no issue:
print(gran1.manufacturer)