
#Mathematical functions (BODMAS)
#BODMAS stands for Brackets, Orders (i.e. powers and square roots, etc.), Division and Multiplication, 
# Addition and Subtraction. It is a rule that defines the order of operations to evaluate 
# a mathematical expression.

#Division

def divide():
    try:
        a = int(input(f"Enter the first number:"))
        b = int(input(f"Enter the second number:"))

        quotient = a / b 
        return print(f"{a} divided by {b} equals {quotient: .2f}")
    except ZeroDivisionError as e:
         print("Error: Division by zero is not allowed.:", e)
    except ValueError as v:
        print("Error: Invalid input. Please enter numeric values.:", v)

divide()

#Multiplication
def multiply():
    try:
        a = int(input(f"Enter the first number:"))
        b = int(input(f"Enter the second number:"))
        product = a * b
        return print(f"{a} multiplied by {b} equals {product}")
    except ValueError as v:
        print("Error: Invalid input. Please enter numeric values.:", v)


multiply()

#Addition
def add():

    try:
        a = int(input(f"Enter the first number:"))
        b = int(input(f"Enter the second number:"))
        sum = a + b
        return print(f"{a} plus {b} equals {sum}")
    except ZeroDivisionError as e:
        print("Error: Invalid input. Please enter numeric values.:", e)
    except ValueError as v:
        print("Error: Invalid input. Please enter numeric values.:", v)


add()

#Substraction
def substract():

    try:
        a = int(input(f"Enter the first number:"))
        b = int(input(f"Enter the second number:"))
        difference = a - b
        return print(f"{a} minus {b} equals {difference}")
    except ZeroDivisionError as e:
        print("Error: Invalid input. Please enter numeric values.:", e)
    except ValueError    as v:
        print("Error: Invalid input. Please enter numeric values.:", v)

substract()


print("This is the end of the mathematical operations.")


