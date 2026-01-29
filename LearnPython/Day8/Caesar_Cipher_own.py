import string


def encoding():
    user_input = input("Type message to encode:\n")
    letter_shift = int(input("Type the shift number :\n"))
    encode_word = ""
    for char in user_input:
        if char.isupper():
            index = letter_list_upper.find(char) + letter_shift
            if index > 26:
                index = index - 26 
            encode_word += letter_list_upper[index+letter_shift]
        elif char.islower():
            index = letter_list_lower.find(char) + letter_shift
            if index > 26:
                index = index - 26 
            encode_word += letter_list_lower[index]
        else:
            encode_word += char

    print(encode_word)


def decoding():
    user_input = input("Type message to Decode :\n")
    letter_shift = int(input("Type the shift number :\n"))
    decode_word = ""
    for char in user_input:
        if char.isupper():
            index = letter_list_upper.find(char) - letter_shift
            decode_word += letter_list_upper[-index]
        elif char.islower():
            index = letter_list_lower.find(char)- letter_shift
            decode_word += letter_list_lower[index]
        else:
            decode_word += char

    print(decode_word)

letter_list_lower = string.ascii_lowercase
letter_list_upper = string.ascii_uppercase

encode_decode = input("Type 'encode' for Encrypting and 'decode' for decrypting:\n")

if encode_decode == "encode":
    encoding()
elif encode_decode == "decode":
    decoding()
else:
    print("Wrong input")


