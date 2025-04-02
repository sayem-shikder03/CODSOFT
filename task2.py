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

def calculator():
    while True:  
        print("\nSimple CALCULATOR")
        print("Operations available:")
        print("1. Addition ('+')")
        print("2. Subtraction ('-')")
        print("3. Multiplication ('*')")
        print("4. Division ('/')")
        print("5. Exit")

        choice = input("\nSelect an option (1-5): ")

        if choice == "5":
            print("Exiting calculator. Goodbye!")
            break 

        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            if choice == "1":
                result = add(num1, num2)
            elif choice == "2":
                result = subtract(num1, num2)
            elif choice == "3":
                result = multiply(num1, num2)
            elif choice == "4":
                result = divide(num1, num2)
            else:
                print("Invalid option! Please enter 1, 2, 3, or 4.")
                continue 

            print(f"Result:{result}")

        except ValueError:
            print("Error! Please enter valid numbers.")

if __name__ == "__main__":
    calculator()