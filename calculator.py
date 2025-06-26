def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    """
    Divide two numbers.

    Args:
def main():
    """
    Runs a basic command-line calculator that allows the user to perform addition, subtraction,
    multiplication, and division operations until the user chooses to exit.
    """
        b (float): The denominator.

    Returns:
        float: The result of division.

    Raises:
        ValueError: If b is zero.
    """
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b

def main():
    print("Basic Calculator")
    while True:
        print("\nSelect operation:")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Exit")

        choice = input("Enter choice (1/2/3/4/5): ")

        if choice == '5':
            while True:
                try:
                    num1 = float(input("Enter first number: "))
                    break
                except ValueError:
                    print("Invalid input. Please enter a number.")
            while True:
                try:
                    num2 = float(input("Enter second number: "))
                    break
                except ValueError:
                    print("Invalid input. Please enter a number.")
                num2 = float(input("Enter second number: "))
            except ValueError:
                print("Invalid input. Please enter numbers.")
                continue

            if choice == '1':
                print(f"{num1} + {num2} = {add(num1, num2)}")
            elif choice == '2':
                print(f"{num1} - {num2} = {subtract(num1, num2)}")
            elif choice == '3':
                print(f"{num1} * {num2} = {multiply(num1, num2)}")
            elif choice == '4':
            print("Invalid choice.")


if __name__ == "__main__":
    main()      except ValueError as e:
                    print(e)
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()