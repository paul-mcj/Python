from dataclasses import dataclass

@dataclass
class Pet:
    def __init__(self:object, animal: str, name: str, age: int) -> None:
        self.animal = animal
        # private attribute prefixes with __
        # in python, there is always a chance for access, but making variables private sends strong indicators to other developers to not touch them. this contrasts to other languages, where private and protected variables literally cannot be accessed. 
        self.__name = name
        self.age = age
    
    def call_name(self: object) -> str:
        print(f"Hello {self.name}")

    def __str__(self:object) -> str:
        return f"{self.name} is a {self.animal}"
    
    # NOTE: This decorator is a getter method which is "read-only" and is a way to provide encapsulation of class attributes/methods. It is normally done in place of class attributes. This is useful for critical data components of the instantiated object that once set up should never change, and should never be altered.
    # normally, we would set in the constructor "self.name = name". BUT, we are explicitly saying with @property that name is "read only". 
    @property
    def name(self:object) -> object:
        return self.__name
    
    # this is how to use the setter method to change a property
    @name.setter
    def name(self:object, new_name:str) -> str:
        # often, setters can come with encapsulation exceptions
        if len(new_name) > 10:
            raise Exception("Name is too long")
        else:
            self.__name = new_name

     # NOTE: you only need setter (and getter) methods when it comes to class attributes/properties directly. It is ENTIRELY POSSIBLE TO ALTER A PRIVATE PROPERTY IF THAT CHANGE SPECIFICALLY COMES FROM WITHIN A CLASS METHOD! This is how encapsulation works:
     # setting the __name of a Pet should only ever be allowed because of the  @name.setter method above. BUT, we can force a change and that will work because of this encapsulated METHOD:
    def dark_side(self:object) -> str:
        self.__name = "Darth Vader"


    # all the methods below are being used to demonstrate abstraction. say we want to be able to send an email to trim and tails for a haircut for our pet. this email needs to connect to some smpt server first, and then needs to draft the email body before sending.
    def __connect(self:object, smpt_server:object) -> None:
        pass

    def __prep_body(self:object) -> None:
        pass
    
    def __send(self:object) -> None:
        pass
    
    # since all the above 3 methods are set to private, they should only ever be called in this class
    def send_email(self:object) -> None:
        self.__connect("email server 569287")
        self.__prep_body()
        self.__send()
        return f"Hello, I would like to set up an appointment for {self.__name}. They are a {self.animal}, {self.age} years old. Thanks!" 
