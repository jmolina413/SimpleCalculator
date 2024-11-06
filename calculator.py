# calculator.py

def add(x, y):
    """Add Function"""
    return x + y

def subtract(x, y):
    """Subtract Function"""
    return x - y

def multiply(x, y):
    """Multiply Function"""
    return x * y

def divide(x, y):
    """Divide Function"""
    try:
        return x / y
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."

def main():
    print("Simple Calculator")
    print("Choose Operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

    while True:
        choice = input("Enter choice(1/2/3/4): ")

        if choice in ('1', '2', '3', '4'):
            try: 
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
            except ValueError:
                print("Invalid input. Please enter a number.")
                continue

            if choice == '1':
                print(f"{num1} + {num2} =   {add(num1, num2)}")

            elif choice == '2':
                print(f"{num1} - {num2} =   {subtract(num1, num2)}")

            elif choice == '3':
                print(f"{num1} * {num2} =   {multiply(num1, num2)}")

            elif choice == '4':
                print(f"{num1} / {num2} =   {divide(num1, num2)}")
            else:
                print("Invalid choice. Please select a valid operation.")
            
            next_calc = input("Do you want to perform another calculation? (yes/no): ")
            if next_calc.lower() != 'yes':
                break

if __name__ == "__main__":
    main()