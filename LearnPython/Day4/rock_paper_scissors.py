import random
rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper and 2 for Scissors.\n"))

game_images = [rock,paper,scissors]


computer_choice = random.randint(0,2)

if 0 <= user_choice <=2:
    print(game_images[user_choice])
    print(f"Computer Chose:\n{game_images[computer_choice]}")

if user_choice < 0  or  user_choice >=3:
    print("invalid choice. You lose!")
elif user_choice == 0 and computer_choice == 2:
    print("You win!")
elif computer_choice == 0 and user_choice == 2:
    print("You lose!")
elif user_choice > computer_choice:
    print("You win!")
elif computer_choice > user_choice:
    print("You lose!")
elif user_choice == computer_choice:
    print("It's a draw!")





#r>s, s>p, p>r 
# def computer_choice(choice):
#     if choice == 0:
#         print("Computer chose: \n"+rock)
#     elif choice == 1:
#         print("Computer chose: \n"+paper)
#     else:
#         print("Computer chose: \n"+scissors)


# computer_choices = random.randint(0,2)

# if user_choice == 0:
#     print(rock)
#     computer_choice(computer_choices)
#     if computer_choices == 1:
#         print("You lose.")
#     elif computer_choices == 0:
#         print("It's a draw")
#     else:
#         print("You win.")
# elif user_choice == 1:
#     print(paper)
#     computer_choice(computer_choices)
#     if computer_choices == 2:
#         print("You lose.")
#     elif computer_choices == 1:
#         print("It's a draw")
#     else:
#         print("You win.")
# elif user_choice == 2:
#     print(scissors)
#     computer_choice(computer_choices)
#     if computer_choices == 0:
#         print("You lose.")
#     elif computer_choices == 2:
#         print("It's a draw")
#     else:
#         print("You win.")
# else:
#     print("Choice not valid")




