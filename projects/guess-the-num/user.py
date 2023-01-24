import random

def guess(x):
    lowest = 1
    highest = x
    result = ''

    while result != 'c':
        if lowest != highest:
            guess_num = random.randint(lowest, highest)
        
        else:
            guess_num = lowest

        result = input(f"Is {guess_num} too high (H), to low (L), or correct (C)?").lower()

        if result == 'h':
            highest = guess_num - 1

        elif result == 'l':
            lowest = guess_num + 1

    print("Number guessed")

guess(99)