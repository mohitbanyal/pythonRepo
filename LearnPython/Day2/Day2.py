
#Subscripting String's element at the position, from start and end both
print("Hello"[0]) 
print("Hello"[-1])

#Large Integers, put _ for large number to make more readable
print(123_345_678)

#find datatype of a data, Type checking, Error TypeError
#int str float bool
print(type("Hello"))

#Type conversion , wrong conversion : ValueError
#int() , str(), float(), bool()
int("123")
#print("number of letters in the name : " + str(len(input("Enter your name: "))))

#PEMDAS - Paranthesis Exponents Multiplications/Division Addition/Substraction
#BODMAS - Brackets, Orders, Division, Multiplication, Addition, and Subtraction
#devide
print(type(6 / 2)) # always return float
print(type(6 // 2)) # // removed all decimals after int and change it to int : typecasting to int automatically

#multiply 
print(2 * 3)
print(2 ** 3) # means 2 raise to power 3 : exponetial

#BMI 
bmi = 90/1.73 ** 2
print(bmi)
#Round number, number of digits
print(round(bmi,2))

# Assignment operation
score = 0

score += 1
score -= 1
height = 1.73
is_winning = True
#normal string + int in print will give TypeError : to avoid we can use f-string
# f- string - you dont have to convert each data type to string. f-string can do that
print(f"Your score is = {score} with height = {height}. Is this a win ? = {is_winning}")

