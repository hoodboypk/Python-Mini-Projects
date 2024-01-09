from art import logo
import os

def add(n1,n2):
    return n1 + n2

def subtract(n1,n2):
    if(n1 >= n2):
        return n1 - n2
    elif(n2 > n1):
        return n2 - n1

def multiply(n1,n2):
    return n1*n2

def divide(n1,n2):
    return n1/n2

def power(n1,n2):
    return n1**n2

def mod(n1,n2):
    return n1 % n2

operations = {
    "+" : add,
    "-" : subtract,
    "*" : multiply,
    "/" : divide,
    "^" : power,
    "%" : mod
}

def calculator():
    print(logo)
    num1 = int(input("Enter the first number: "))

    for symbol in operations:
        print(symbol)

    should_continue = True

    while should_continue:
        operation_symbol = input("Pick an operation: ")
        num2 = int(input("Enter another number: "))
        calculation_function = operations[operation_symbol]
        answer = calculation_function(num1,num2)
        print(f'{num1} {operation_symbol} {num2} = {answer}')

        if input(f"Enter 'y' to continue with {answer} or 'n' to start a new calculation: ") == 'y':
            num1 = answer
        else:
            should_continue = False
            os.system('cls')
            calculator()


calculator()