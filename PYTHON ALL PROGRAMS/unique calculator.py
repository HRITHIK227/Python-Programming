import math

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Cannot divide by zero!"
    return x / y

def square_root(x):
    if x < 0:
        return "Cannot calculate the square root of a negative number!"
    return math.sqrt(x)

def unique_calculator():
    print("Welcome to the Unique Calculator!")
    while True:
        print("\nChoose an operation:")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Square Root")
        print("6. Quit")
        
        choice = input("Enter your choice (1/2/3/4/5/6): ")

        if choice == '6':
            print("Thank you for using the Unique Calculator. Goodbye!")
            break

        if choice not in ('1', '2', '3', '4', '5'):
            print("Invalid choice. Please select a valid operation.")
            continue

        if choice == '5':
            num = float(input("Enter a number: "))
            result = square_root(num)
            print(f"The square root of {num} is {result}")
        else:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))

            if choice == '1':
                result = add(num1, num2)
                operation = "+"
            elif choice == '2':
                result = subtract(num1, num2)
                operation = "-"
            elif choice == '3':
                result = multiply(num1, num2)
                operation = "*"
            elif choice == '4':
                result = divide(num1, num2)
                operation = "/"

            print(f"{num1} {operation} {num2} = {result}")

if __name__ == "__main__":
    unique_calculator()
