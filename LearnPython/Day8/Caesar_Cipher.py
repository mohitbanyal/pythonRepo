import string
from art import caesar_art

print(caesar_art)

list = string.ascii_lowercase 

def caesar_method(user_input,shift_number,encode_or_decode):
    processed_text = ""
    if encode_or_decode == "decode":
            shift_number *= -1
    for letter in user_input:
        if letter not in list:
             processed_text += letter
        else:
            index = list.index(letter) + shift_number
            index %= len(list)
            processed_text +=list[index]
    
    print(f"Your {encode_or_decode}d text is: {processed_text}")

should_restart = True

while should_restart:
    process = input("Please type 'encode' to Encrypt and 'decode' for Decrypt:\n")
    text = input("Please type your text:\n")
    shift_amount = int(input("please type the shifting number:\n"))

    caesar_method(user_input=text, shift_number= shift_amount, encode_or_decode=process)
    print("")
    restart = input("Type 'yes' to restart or type 'no' to end:\n")

    if restart == 'no':
        should_restart = False
        print("GoodBye!")
