import random

random_int = random.randint(1,10)
print(random_int)

random_number_0_to_1 = random.random() *10
print(random_number_0_to_1)

#this may not give upper bound due to upper bound rounding
random_float = random.uniform(1,10)
print(random_float)

random_coin = random.randint(0,1)

if random_coin == 0:
    print("Heads")
else:
    print("Tails")