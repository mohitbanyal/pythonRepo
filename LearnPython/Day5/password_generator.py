import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#random password with suffling
# easy_password = random.choices(letters,k=nr_letters) + random.choices(symbols,k=nr_symbols) +random.choices(numbers,k=nr_numbers)
# random.shuffle(easy_password)
# print("Your password : " +"".join(easy_password))


#password using different letter symbol at different level
password = ""
for alphabets in random.choices(letters,k=nr_letters):
    password += alphabets

for symbol in random.choices(symbols,k=nr_symbols):
    password += symbol

for number in random.choices(numbers,k=nr_numbers):
    password += number

print("Your random password is : " + password)

#password using range
range_password =""

for char in range(0,nr_letters):
    range_password += random.choice(letters)

for char in range(0,nr_symbols):
    range_password += random.choice(symbols)

for char in range(0,nr_numbers):
    range_password += random.choice(numbers)

print(f"Your Easy Password is : {range_password}")

#password using range and random shuffle list

range_password_list =[]

for char in range(0,nr_letters):
    #range_password_list += random.choice(letters)
    range_password_list.append(random.choice(letters))

for char in range(0,nr_symbols):
    #range_password_list += random.choice(symbols)
    range_password_list.append(random.choice(symbols))

for char in range(0,nr_numbers):
    #range_password_list += random.choice(numbers)
    range_password_list.append(random.choice(numbers))


random.shuffle(range_password_list)
hard_password = ""
for char in range_password_list:
    hard_password += char

print(f"Your hard password is : {hard_password}")




