import requests
import json
import random
import string

req = requests.get("https://www.randomlists.com/data/words.json")
words = json.loads(req.text)['data']

def hangman():
    word = random.choice(words).upper()
    word_letters = set(word) # each letter in the word
    alphabet = set(string.ascii_uppercase)
    used_letters = set()

    tries = 10

    while len(word_letters) > 0 and tries > 0:
        print("Your used letters: ", ' '.join(used_letters))
        
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print("Current word: ", ' '.join(word_list))
        print(f"Current tries: {tries}")

        user_letter = input("Guess a letter: ").upper()

        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)

            if(user_letter in word_letters):
                word_letters.remove(user_letter)
            
            else:
                tries = tries - 1

        elif user_letter in used_letters:
            print("You already used that letter, try another one!")

        else:
            print("Invalid character, try again!")

    if tries == 0:
        print("No more tries left. Word was", word)
    else:
        print("You won!")


hangman()

