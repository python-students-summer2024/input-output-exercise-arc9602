"""
A little assignment to practice receiving text input from the user in Python programming.
Do not run this file... run main.py instead.
"""


def get_favorite_vegetable():
    """
    Asks the user to enter their favorite vegetable
    and then prints out, "Interesting! I also love X!",
    where X is replaced with the user's favorite vegetable.
    """
    # write your code here.
    veg = input("Hey! What's your favourite vegetable? ")
    print("Interesting! I also love ", veg)


def get_favorite_number():
    """
    Asks the user to enter their favorite number
    and then prints out, "Interesting! I also love X!",
    where X is replaced with the user's favorite number.
    """
    # write your code here.
    num = int(input("Hey! What's your favourite number? "))
    print("Interesting! I also love ", num)


def get_name_and_zodiac_sign():
    """
    Asks the user to enter their name.
    Then ask them to enter their zodiac sign.
    Then print out, "Interesting! My name is also X, and I'm also a Y!",
    where X and Y are replaced by the user's name and zodiac sign, respectively.
    """
    # write your code here.
    name = input("Hey! What's your name? ")
    zod = input("Oh that's nice, what about your zodiac sign? ")
    print("Interesting! My name is also " + name + ", and I'm also a " + zod + "!")


def get_name_and_age():
    """
    Asks the user to enter their name.
    Then ask them to enter their age.
    Then print out, "Interesting! My name is also X, and I'm also Y years old!",
    where X and Y are replaced by the user's name and age, respectively.
    """
    # write your code here.
    name = input("Hey! What's your name? ")
    age = input("Oh that's nice, how old are you? ")
    print("Interesting! My name is also "+name+", and I'm also "+age+" years old!")
