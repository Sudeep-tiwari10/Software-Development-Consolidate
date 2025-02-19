
#Fibonacci Numbers Using Recursion
def fibonacci(n):
    """
    Recursively calculates the nth Fibonacci number.
    
    Args:
        n (int): The position in the Fibonacci sequence (0-based index).
        
    Returns:
        int: The nth Fibonacci number.
    """
    # Base cases
    if n == 0:
        return 0
    elif n == 1:
        return 1
    
    # Recursive step
    return fibonacci(n - 1) + fibonacci(n - 2)

n = int(input("Enter the position (n) to find the nth Fibonacci number: "))
print(f"The {n}th Fibonacci number is {fibonacci(n)}")


# Factorial Using Recursion
def factorial(n):
    """
    Recursively calculates the factorial of a number.
    
    Args:
        n (int): The number to calculate the factorial for.
        
    Returns:
        int: The factorial of n.
    """
    # Base case
    if n == 0:
        return 1
    
    # Recursive step
    return n * factorial(n - 1)

# Example usage
n = int(input("Enter a number to calculate its factorial: "))
print(f"The factorial of {n} is {factorial(n)}")
