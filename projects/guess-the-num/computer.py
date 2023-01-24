import random

def guess(x):
    random_mun = random.randint(1, x)
    guess_num = 0

    while guess_num != random_mun:
        guess_num = int(input(f"Write a number: "))

        if guess_num > random_mun:
            print("Too high, try again!")
        elif guess_num < random_mun:
            print("Too low, try again!")

    print("You guessed the number!")

guess(7)