#conditional statments
#Theme park ticket 
#height = int(input("What is your hieght in cm ? "))
height = 120
bill = 0
if height >= 120:
    print("You can ride the rolercoaster")
    #age = int(input("what is your age?"))
    age = 17
    if age <=12:
        print("Child ticket price is : $5")
        bill = 5
    elif age <=18:
        print("Youth ticket price is : $7")
        bill = 7
    else:
        print("Adult ticket price is : $12")
        bill = 12
    
    #wants_photos = input("Do you wants your photos ? type y for yes : ")
    wants_photos = "y"
    if wants_photos == "y":
        bill +=3

    print(f"total amount is : {bill}")    
else:
    print("You have to grow taller before you can ride")

#Modulo Operator = remainder
