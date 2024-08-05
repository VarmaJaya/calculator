import os
from art import logo
def calculator():

    def add(a,b):
        return a+b
    def sub(a,b):
        return a-b
    def multiply(a,b):
        return a*b
    def divide(a,b):
        return a/b

    operations = {
        "+":add,
        "-":sub, 
        "*":multiply, 
        "/":divide
        }
    print(logo)
    num1 = float(input("Please enter your first number: "))


    for operation in operations:
        print(operation)

    should_continue = True

    while should_continue:

        operation_symbol = input("please choose the operation: ")
        num2 = float(input("Please enter your next number: "))
        calculation_function= operations[operation_symbol]
        answer = calculation_function(a=num1, b=num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")
        if input(f"if you want to continue with {answer} type 'y' or if you want to start again type 'n' ") == "y":
            num1 = answer
        else:
            should_continue = False
            os.system("cls")
            calculator()
            
            
calculator()

    


