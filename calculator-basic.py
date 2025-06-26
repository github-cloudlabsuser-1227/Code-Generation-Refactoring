# create basic calculator with functions for add, subtract, multiply, divide
def add(x, y):
    """Add two numbers."""
    return x + y

def subtract(x, y):
    """Subtract two numbers."""
    return x - y

def multiply(x, y):
    """Multiply two numbers."""
    return x * y

def divide(x, y):
    """Divide two numbers."""
    if y != 0:
        return x / y
    else:
        raise ZeroDivisionError("Division by zero error")

def main():
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")

    choice = input("Enter choice (1/2/3/4/5): ").strip()

    if choice in ['1', '2', '3', '4']:
        while True:
            try:
                num1 = float(input("Enter first number: "))
                break
            except ValueError:
                print("Invalid input. Please enter a numeric value.")
        while True:
            try:
                num2 = float(input("Enter second number: "))
                break
            except ValueError:
                print("Invalid input. Please enter a numeric value.")

        try:
            if choice == '1':
                print(f"{num1} + {num2} = {add(num1, num2)}")
            elif choice == '2':
                print(f"{num1} - {num2} = {subtract(num1, num2)}")
            elif choice == '3':
                print(f"{num1} * {num2} = {multiply(num1, num2)}")
            elif choice == '4':
                print(f"{num1} / {num2} = {divide(num1, num2)}")
        except ZeroDivisionError as e:
            print(e)
    elif choice == '5':
        print("Exiting the calculator.")
    else:
        print("Invalid input")

if __name__ == "__main__":
    main()