# Import the numpy library
from numpy import percentile

# Function to perform addition
def add(x, y):
    return x + y

# Function to perform subtraction
def subtract(x, y):
    return x - y

# Function to perform multiplication
def multiply(x, y):
    return x * y

# Function to perform division
def divide(x, y):
    if y == 0:
        return "Division by zero is not allowed."
    return x / y

# Main program
while True:
    print("Options:")
    print("Enter '+' for Addition")
    print("Enter '-' for Subtraction")
    print("Enter '*' for Multiplication")
    print("Enter '/' for Division")
    print("Enter 'p' for Percentile")
    print("Enter 'quit' to end the program")

    choice = input("Enter your choice: ")

    if choice == "quit":
        break

    if choice in ["+", "-", "*", "/"]:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == "+":
            result = add(num1, num2)
        elif choice == "-":
            result = subtract(num1, num2)
        elif choice == "*":
            result = multiply(num1, num2)
        elif choice == "/":
            result = divide(num1, num2)

        print(f"Result: {result}")

    elif choice == "p":
        data = input("Enter a list of numbers separated by spaces: ").split()
        data = [float(x) for x in data]
        percentile_value = float(input("Enter the percentile value (0-100): "))
        result = percentile(data, percentile_value)
        print(f"{percentile_value}th percentile: {result}")

    else:
        print("Invalid choice. Please try again.")
