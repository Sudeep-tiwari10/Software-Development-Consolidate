# Task 1: Hello World Program
print("Hello, World!")

# Task 2: Basic Arithmetic Operations
# Taking input from the user
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

# Performing arithmetic operations
print("Addition:", num1 + num2)
print("Subtraction:", num1 - num2)
print("Multiplication:", num1 * num2)
print("Division:", num1 / num2)


# Task 3: Even or Odd
# Taking input from the user
number = int(input("Enter a number: "))

# Checking if the number is even or odd
if number % 2 == 0:
    print(f"{number} is Even")
else:
    print(f"{number} is Odd")
