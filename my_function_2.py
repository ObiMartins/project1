
    #Number addition from user
def add():
    num1 = input (f"Enter number 1: ")
    num2 = input(f"Enter number 2: ")
    sum = str(int(num1) + int(num2))
    print(f"Sum of {num1} and {num2} is {sum}")

    #Number multiplication from user
def multiply():
    num1 = input (f"Enter number 1: ")
    num2 = input(f"Enter number 2: ")
    product = str(int(num1) * int(num2))
    print(f"Product of {num1} and {num2} is {product}")

    #Number division from user
def divide():
    num1 = input (f"Enter number 1: ")
    num2 = input(f"Enter number 2: ")
    quotient = str(int(num1) / int(num2))
    print(f"Quotient of {num1} and {num2} is {quotient}")


    #Number substraction from user
def substract():
    num1 = input (f"Enter number 1: ")
    num2 = input(f"Enter number 2: ")
    difference = str(int(num1) - int(num2))
    print(f"Difference of {num1} and {num2} is {difference}")



print("============Number addition from user====================")
add()
print()
print("============Number multiplication from user====================")
multiply()
print()
print("============Number division from user====================")
divide()
print()
print("============Number subtraction from user====================")
substract()