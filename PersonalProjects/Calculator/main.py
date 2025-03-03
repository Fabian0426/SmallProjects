import math


def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    return x / y

def power(x, y):
    if x == 0 and y == 0:
        return "Error! 0^0 is undefined."
    result = 1
    y = int(y)
    for _ in range(y):
        result *= x
    return result

def sqrt(x):
    if x < 0:
        return "Error! Square root of a negative number is undefined."
    return x ** 0.5

def logarithmic(x, y):
    if x < 0 or y < 0:
        return "Error! Logarithmic function is undefined."
    return math.log(x, y)



def main():
    while True:
        print("Options:")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Power")
        print("6. Square Root")
        print("7. Logarithm")
        print("8. Exit")

        choice = input("Choose an option: ")


        if choice == '1':
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            print(f"Result: {add(num1, num2)}\n")
        elif choice == '2':
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            print(f"Result: {subtract(num1, num2)}\n")
        elif choice == '3':
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            print(f"Result: {multiply(num1, num2)}\n")
        elif choice == '4':
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            print(f"Result: {divide(num1, num2)}\n")
        elif choice == '5':
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            print(f"Result: {power(num1, num2)}\n")
        elif choice == '6':
            num1 = float(input("Enter first number: "))
            print(f"Result: {sqrt(num1)}\n")
        elif choice == '7':
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            print(f"Result: {logarithmic(num1, num2)}\n")
        else:
            print("Invalid choice!\n")

if __name__ == "__main__":
    main()