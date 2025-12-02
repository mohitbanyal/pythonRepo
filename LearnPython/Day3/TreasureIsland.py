print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/______/_
*******************************************************************************
      ''')
print("Welcome to Treasure Island.\nYour mission is to find the Treasure.")

cross_road = input('You\'re at a cross road, where you want to go? "Left" or "Right"?\n').upper()

if cross_road == "LEFT":
    river_choice= input('Yay! You\'ve come to an river! '
                        'There is an Island in the middle of the road. '
                        'Type "Wait" to wait the boat? '
                        'Type "swim" to swim across\n').upper()
    if river_choice == "WAIT":
        print("You boarded the boat and reached the island unharmed." \
        " There is an house on the island with three doors. One Red, one Yellow and one Blue. " \
        "Which color do you choose? \n")
        door_choice = input("You found Three Doors. Red, Yellow and Blue. Which one will you choose? ").upper()
        if door_choice == "RED":
            print("It's a room full of fire. Game Over!")
        elif door_choice == "BLUE":
            print("You enter a room of beasts. Game Over!")
        elif door_choice == "YELLOW":
            print("Yay!, You found the Treasure. You won!")
        else:
            print("You choose the door that doesn't exist. Game Over!")
    else:
        print("You got attacked by an angry trout. Game Over!")
else:
    print("You fell in the hole. Game Over!")