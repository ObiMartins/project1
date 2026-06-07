
#Mathematical functions (BODMAS)
#BODMAS stands for Brackets, Orders (i.e. powers and square roots, etc.), Division and Multiplication, 
# Addition and Subtraction. It is a rule that defines the order of operations to evaluate 
# a mathematical expression.

#Division
def divide(a, b):
    quotient = a / b 
    return print(f"{a} divided by {b} equals {quotient: .2f}")

divide(100, 5)

#Multiplication
def multiply(a, b):
    product = a * b
    return print(f"{a} multiplied by {b} equals {product}")

multiply(100, 5)

#Addition
def add(a, b):
    sum = a + b
    return print(f"{a} plus {b} equals {sum}")

add(100, 5)

#Substraction
def substract(a, b):
    difference = a - b
    return print(f"{a} minus {b} equals {difference}")

substract(100, 5)




