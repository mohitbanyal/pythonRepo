print("Welcome tp Python Pizza Deliveries")

size = input("What size pizza do you want ? S, M or L : ")

bill = 0

if size == "S":
    bill = 15
elif size == "M":
    bill = 20
else:
    bill = 25

pepperoni = input("Do you want pepperoni on your pizza ? Y or N : ")

if pepperoni == "Y":
    bill +=2

extra_cheese = input("Do you want extra cheese? Y or N : ")
if extra_cheese == "Y":
    bill += 1

print(f"Your total bill is : {bill}")

