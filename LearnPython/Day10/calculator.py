import art

def add(a,b):
    return a + b
def multiply(a,b):
    return a * b
def division(a,b):
    return a / b
def subtraction(a,b):
    return a - b

operations = {
    "+" : add,
    "*": multiply,
    "/": division,
    "-": subtraction,
}

def calculator():
    print(art.logo)
    continue_calculation = True
    num1 = int(input("What's the first number?: "))

    while continue_calculation:
        for ops in operations:
            print(ops)
        operation = input("Pick an operation: ")
        num2 = int(input("What's your next number?:"))
        result = operations[operation](num1,num2)
        print(f"{num1} {operation} {num2} = {result}")
        choice = input(f"Type 'y' to continue calculation with {result}, or type " \
                                   "'n' to start a new calculation: ")
        if choice == 'y':
            num1 = result
        elif choice == 'n':
            continue_calculation = False
            print("\x1b[2J\033[H")
            calculator()
        else:
            continue_calculation = False
            print("Invalid input. Good Bye!")


calculator()
