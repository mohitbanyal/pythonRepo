import random
from hangman_art import stages, logo
from words import word_list

print(logo)

random_word = random.choice(word_list)
print(random_word)

placeholder =""
for char in random_word:
    placeholder += "_"

print(f"Word to guess: {placeholder}")
correct_words =[]
used_words =[]

game_over = False
lives = 6
while not game_over:
    display =""
    print(f"You have {lives} lives left")
    user_guess = input("Guess your letter: ").lower()
    while user_guess in used_words:
      user_guess = input("You have already guessed this letter. Guess again: ").lower()

    used_words.append(user_guess)
    print("Your Guessed letters are: ",end=" ")
    print(*used_words)

    for char in random_word:
        if char == user_guess:
            display += char
            correct_words.append(char)
        elif char in correct_words:
            display += char
        else:
            display += "_"
    
    print(stages[lives])
    print(display)
    print("")

    if user_guess not in correct_words:
        lives -= 1
        if lives == 0:
            game_over = True 
            print(stages[0])
            print(f"You could not guess. Game Over.Your word was: {random_word}") 
            

    if "_" not in display:
        game_over = True
        print("Yay!! You Win.")





