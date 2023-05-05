import random
from words import words
import string

def get_valid_word(words):
    word = random.choice([words])

    while "_" in word or " " in word:
        word = random.choice([words])

    return word.upper()

def hangman():
    word = get_valid_word(words)
    word_letters = set(word)  # creates a set of letters within the (word)
    alphabet = set(string.ascii_uppercase)  # creates upper case set of the alphabet letters using the pre defined function
    used_letters = set()  # creates a new set of empty letters, to be added to afterwards, basically wrong guesses

    lives = 7

    while len(word_letters) > 0 and lives > 0:
        print("You have " + str(lives) + " lives left and You have used these letters:", ' '.join(used_letters))

        word_list = [letter if letter in used_letters else '-' for letter in word]
        print("Current word: ", ' '.join(word_list))

        user_letter = input("Guess a letter: ").upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter) # basically if it's not in the alpabet minus the wrong guesses, it gets added to the list of wrong guesses
            if user_letter in word_letters:
                word_letters.remove(user_letter) # if letter is in the word_letters set, gets removed from the list
                print('')

            else:
                lives = lives - 1
                print("Your letter", user_letter, "is not in word")

        elif user_letter in used_letters:
            print("You have already guessed this letter. Please try again")

        else:
            print("Invalid Choice. Please try again")

    if lives == 0:
        print("You died, sorry. The word was", word)

if __name__ == '__main__':
    hangman()