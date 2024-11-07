import math  # Importing the math module for advanced mathematical functions

# Basic arithmetic functions

def add(x, y):
    """Add two numbers."""
    return x + y

def subtract(x, y):
    """Subtract the second number from the first."""
    return x - y

def multiply(x, y):
    """Multiply two numbers."""
    return x * y

def divide(x, y):
    """Divide the first number by the second, handling division by zero."""
    try:
        return x / y
    except ZeroDivisionError:
        return "Error: Cannot divide by zero"

# Advanced mathematical functions

def power(x, y):
    """Raise x to the power of y."""
    return x ** y

def square_root(x):
    """Calculate the square root of a number."""
    if x < 0:
        return "Error: Cannot calculate the square root of a negative number"
    return math.sqrt(x)

def logarithm(x):
    """Calculate the natural logarithm (log base e) of a number."""
    if x <= 0:
        return "Error: Logarithm undefined for zero or negative values"
    return math.log(x)

def log_base_10(x):
    """Calculate the base-10 logarithm of a number."""
    if x <= 0:
        return "Error: Logarithm undefined for zero or negative values"
    return math.log10(x)

def sine(x):
    """Calculate the sine of an angle in degrees."""
    return math.sin(math.radians(x))

def cosine(x):
    """Calculate the cosine of an angle in degrees."""
    return math.cos(math.radians(x))

def tangent(x):
    """Calculate the tangent of an angle in degrees."""
    return math.tan(math.radians(x))

def factorial(x):
    """Calculate the factorial of a non-negative integer."""
    if x < 0:
        return "Error: Factorial undefined for negative numbers"
    elif not float(x).is_integer():
        return "Error: Factorial only defined for integers"
    return math.factorial(int(x))

# Main function to run the calculator logic

def main():
    print("Advanced Calculator")
    print("Choose Operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Power")
    print("6. Square Root")
    print("7. Logarithm (base e)")
    print("8. Logarithm (base 10)")
    print("9. Sine")
    print("10. Cosine")
    print("11. Tangent")
    print("12. Factorial")

    while True:
        choice = input("Enter choice (1-12): ")

        # Check if the choice is valid for operations that need two numbers
        if choice in ('1', '2', '3', '4', '5'):
            try:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
            except ValueError:
                print("Invalid input. Please enter a number.")
                continue

            if choice == '1':
                print(f"{num1} + {num2} = {add(num1, num2)}")
            elif choice == '2':
                print(f"{num1} - {num2} = {subtract(num1, num2)}")
            elif choice == '3':
                print(f"{num1} * {num2} = {multiply(num1, num2)}")
            elif choice == '4':
                print(f"{num1} / {num2} = {divide(num1, num2)}")
            elif choice == '5':
                print(f"{num1} ^ {num2} = {power(num1, num2)}")

        # Operations that only need one number
        elif choice in ('6', '7', '8', '9', '10', '11', '12'):
            try:
                num = float(input("Enter number: "))
            except ValueError:
                print("Invalid input. Please enter a number.")
                continue

            if choice == '6':
                print(f"Square root of {num} = {square_root(num)}")
            elif choice == '7':
                print(f"Natural log of {num} = {logarithm(num)}")
            elif choice == '8':
                print(f"Log base 10 of {num} = {log_base_10(num)}")
            elif choice == '9':
                print(f"Sine of {num} degrees = {sine(num)}")
            elif choice == '10':
                print(f"Cosine of {num} degrees = {cosine(num)}")
            elif choice == '11':
                print(f"Tangent of {num} degrees = {tangent(num)}")
            elif choice == '12':
                if num.is_integer() and num >= 0:
                    print(f"{int(num)}! = {factorial(int(num))}")
                else:
                    print("Error: Factorial is only defined for non-negative integers.")

        else:
            print("Invalid choice. Please select a valid operation.")

        next_calc = input("Do you want to perform another calculation? (yes/no): ")
        if next_calc.lower() != 'yes':
            break

# Run the calculator if the script is executed directly
if __name__ == "__main__":
    main()
