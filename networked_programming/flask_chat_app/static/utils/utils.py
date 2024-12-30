import random
from string import ascii_uppercase

# create a random code for a chat room. Check if the chat room already exists as well
def generate_unique_code(length: int, rooms_dict: dict) -> str:
    while True:
        code = ""
        for _ in range(length):
            code += random.choice(ascii_uppercase)

        if code not in rooms_dict:
            break

    return code