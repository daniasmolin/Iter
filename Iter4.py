import random
import string

def random_letters_generator(limit=10):
    for _ in range(limit):
        yield random.choice(string.ascii_lowercase)

for letter in random_letters_generator(5):
    print(letter)