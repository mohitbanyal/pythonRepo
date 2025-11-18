import random
import string

from words import words

def get_valid_word(words):
    word = random.choice(words)
    while '-' in word or ' ' in word:
        word = random.choice(word)

    return word.upper()

def hangman():
    word = get_valid_word(words)
    word_letters = set(word) #set to save letters in word
    alphabet = set(string.ascii_uppercase)
    used_letters = set() # save letter that user has guesses
    lives = 6
    #getting user input
    while len(word_letters) >0 and lives >0:
        #show user letter they have user
        print('You have ', lives, 'lives left and you have guessed ',' '.join(used_letters))
        #show user letter that they have guess and - where they haven't
        list = [letter if letter in used_letters else '-' for letter in word]
        print('Current word: ',' '.join(list))
        user_letter = input('Guess a letter: ').upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
            else:
                lives = lives-1

        elif user_letter in used_letters:
            print('You have already guessed that character. Please try again.')

        else:
            print('Invalid character. Please try agian.')

    if lives == 0:
        print('You have died. Word was: ', word)
    else:
        print('Yay! you guess the word', word,'!!')


hangman()


