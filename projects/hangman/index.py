import requests
import json
import random
import string

req = requests.get("https://www.randomlists.com/data/words.json")
words = json.loads(req.text)['data']

def valid_word(words):
    word = random.choice(words)

    while '-' in word or ' ' in word:
        word = random.choice(words)

    return word

def hangman():
    word = valid_word(words)
    word_letters = set(word) # each letter in the word
    alphabet = set(string.ascii_uppercase)
    used_letters = set()

    while len(word_letters) > 0:
        print("Your used letters: ", ' '.join(used_letters))
        #32:01
        user_letter = input("Guess a letter: ").upper()

        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)

            if(user_letter in word_letters):
                word_letters.remove(user_letter)

        elif user_letter in used_letters:
            print("You already used that letter, try another one!")

        else:
            print("Invalid character, try again!")


hangman()

