import random

friends = ["Mohit", "Jazz", "Alice", "Bob", "Charlie", "David"]

friends.append("Puneet")
friends.extend(["Sumit", "Morris"])

#print(friends)

#option 1
who_will_pay_bill = random.choice(friends)

#print(who_will_pay_bill)

#option 2
random_index = random.randint(0,len(friends)-1)
#print(friends[random_index])

fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]

dirty_dozen = [fruits,vegetables]

print(dirty_dozen[1][1])
