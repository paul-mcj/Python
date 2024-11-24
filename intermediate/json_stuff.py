# NOTE: JSON modules are easily available in python
import json  

def main():
    #  example dictionary
    profile = {
    "name": "John Doe",
    "age": 30,
    "is_active": True,
    "email": "johndoe@example.com",
    "hobbies": ["reading", "cycling", "coding"],
    "address": {
        "street": "123 Elm St",
        "city": "Springfield",
        "zip": "12345"
    }}

    # converting python code into JSON is called "encoding" or "serialization" and uses the dumps() method -- "dump" is the word used for the encoding, and the "s" at the end stands for string!!
    # NOTE: its always a good idea to use the "indent" argument because it will format it for the console making it super easy to read! Using "sort_keys" can also be useful, as it will alphabetize key names.
    profile_json = json.dumps(profile, indent=4, sort_keys=True) 
    print(profile_json)
    print()

    # lets add the dictionary data to a new file
    with open("profile.json", "w") as file:
        # not dumps, but dump:
        json.dump(profile, file, indent=5)

    # the process of converting json data into python code is thus "encoding" or "deserialization" and uses "loads", and again the "s" is for string
    profile = json.loads(profile_json)
    print(profile) # see our original dict
    print()

    # we can also read json data from a file and decode it to a dict:
    with open("profile.json", "r") as file:
        decode_profile_json = json.load(file)

    print(decode_profile_json) # now back to dict
    print()

    # its more difficult to deal with json data as class instances. There are two ways you can deal with encoding and decoding: either create a custom method for the conversion, or import JSONEncoder. Its almost always better to just import the latter, as its easier, modular, and reusable -- creating a custom handler for the class is really only better if you need very specific solutions.

    # basic class for example purposes
    class User:
        def __init__(self: object, name: str, age: int) -> None:
            self.name = name
            self.age = age

    paul = User("Paul", 30)

    # this gives a TypeError: Object of type User is not JSON serializable
    # paul_json = json.dumps(paul)

    from json import JSONEncoder, JSONDecoder

    # create a new class and inherit the JSONEncoder
    class UserEncoder(JSONEncoder):
        def default(self:object, obj: object) -> None:
            # if the object is an instance of the User class, convert to a dictionary
            if isinstance(obj, User):
                # since all instances of user defined classes have string representations of what it would be as a dictionary, we can simply return that here
                encoded_obj = obj.__dict__
                # NOTE: creating such a property will be beneficial when decoding later, as it will be a boolean property if the instance if of type User
                encoded_obj[obj.__class__.__name__] = True
                return encoded_obj
                # the other option would be to return an actual dictionary and list off every property which can be consuming if the class has a lot going on
                # return {"name": obj.name, "age": obj.age, obj.__class__.__name__: True}
            else:
                # let base json encoder handle errors
                return JSONEncoder.default(self, obj)

    # pass object instance and "cls" argument of our custom encoder to the dumps method
    paul_json_1 = json.dumps(paul, cls=UserEncoder)
    print(paul_json_1)
    print()

    # other way does the same thing:
    paul_json_2 = UserEncoder().encode(paul)
    print(paul_json_2) 
    print()

    # now lets decode so we can get this json data back into its class form
    def decode_user(dictionary):
        if User.__name__ in dictionary:
            #  create a User object
            return User(name=dictionary["name"], age=dictionary["age"])
        else:
            #  decode into dictionary otherwise
            return dictionary
            
    paul_decoded = json.loads(paul_json_1, object_hook=decode_user)
    print(type(paul_decoded)) # should be a class now!
    print(paul_decoded.__dict__)
    print(paul_decoded.name, paul_decoded.age) # meaning we can access its properties
    print()

    # NOTE: decoding back to classes can also be done via dataclasses pretty efficiently:
    from dataclasses import dataclass

    @dataclass
    class SecondPersonEncoder:
        name: str
        age: int
        User: bool

    paul_decoded_2 = SecondPersonEncoder(**(json.loads(paul_json_1)))
    print(type(paul_decoded_2)) # should be a class now!
    print(paul_decoded_2.__dict__)
    print(paul_decoded_2.name, paul_decoded_2.age) # meaning we can access its properties
    print()

    
            

if __name__ == "__main__":
    main()