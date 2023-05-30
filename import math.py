import math


def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        print("Error: Cannot divide by zero!")

def power(x, y):
    return x ** y

def square_root(x):
    if x >= 0:
        return math.sqrt(x)
    else:
        print("Error: Invalid input for square root!")

def factorial(x):
    return math.factorial(x)

def solve_equation(equation, variable):
    x = sympy.symbols(variable)
    solution = sympy.solve(equation, x)
    return solution

def calculator():
    print("Welcome to the Calculator!")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Power")
    print("6. Square Root")
    print("7. Factorial")
    print("8. Solve Equation")
    print("0. Exit")

    while True:
        choice = input("Enter your choice (0-8): ")

        if choice == '0':
            print("Thank you for using the Calculator!")
            break

        elif choice in ['1', '2', '3', '4', '5']:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))

            if choice == '1':
                print("Result:", add(num1, num2))
            elif choice == '2':
                print("Result:", subtract(num1, num2))
            elif choice == '3':
                print("Result:", multiply(num1, num2))
            elif choice == '4':
                print("Result:", divide(num1, num2))
            elif choice == '5':
                print("Result:", power(num1, num2))

        elif choice == '6':
            num = float(input("Enter a number: "))
            print("Result:", square_root(num))

        elif choice == '7':
            num = int(input("Enter a number: "))
            print("Result:", factorial(num))

        elif choice == '8':
            equation = input("Enter an equation: ")
            variable = input("Enter the variable to solve for: ")
            try:
                solution = solve_equation(equation, variable)
                print("Solution:", solution)
            except sympy.SympifyError:
                print("Error: Invalid equation!")

        else:
            print("Invalid choice. Please try again.")

        print()  # Print an empty line for separation

calculator()

import math


def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        print("Error: Cannot divide by zero!")

def power(x, y):
    return x ** y

def square_root(x):
    if x >= 0:
        return math.sqrt(x)
    else:
        print("Error: Invalid input for square root!")

def factorial(x):
    return math.factorial(x)

def solve_equation(equation, variable):
    x = sympy.symbols(variable)
    solution = sympy.solve(equation, x)
    return solution

def calculator():
    print("Welcome to the Calculator!")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Power")
    print("6. Square Root")
    print("7. Factorial")
    print("8. Solve Equation")
    print("0. Exit")

    while True:
        choice = input("Enter your choice (0-8): ")

        if choice == '0':
            print("Thank you for using the Calculator!")
            break

        elif choice in ['1', '2', '3', '4', '5']:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))

            if choice == '1':
                print("Result:", add(num1, num2))
            elif choice == '2':
                print("Result:", subtract(num1, num2))
            elif choice == '3':
                print("Result:", multiply(num1, num2))
            elif choice == '4':
                print("Result:", divide(num1, num2))
            elif choice == '5':
                print("Result:", power(num1, num2))

        elif choice == '6':
            num = float(input("Enter a number: "))
            print("Result:", square_root(num))

        elif choice == '7':
            num = int(input("Enter a number: "))
            print("Result:", factorial(num))

        elif choice == '8':
            equation = input("Enter an equation: ")
            variable = input("Enter the variable to solve for: ")
            try:
                solution = solve_equation(equation, variable)
                print("Solution:", solution)
            except sympy.SympifyError:
                print("Error: Invalid equation!")

        else:
            print("Invalid choice. Please try again.")

        print()  # Print an empty line for separation

calculator()

