#Tip Calculator 
print("Welcome to the Tip Calculator")
total_bill = float(input("What was the total bill? \n$"))
tip = int(input("How much tip would you like to give ? 10 , 12, or 15 \n"))
number_of_people = int(input("How many people to split the bill ? \n"))
bill_with_tip = total_bill + (1 + tip/100)
#amount = round((total_bill + (total_bill / tip) ) / number_of_people,2)

amount = round(bill_with_tip / number_of_people,2)

print(f"Each person should pay : ${amount}")
