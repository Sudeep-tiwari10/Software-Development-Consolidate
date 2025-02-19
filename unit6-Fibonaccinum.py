def Fib(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    
    else:
        return Fib((n-2))+((n-1))
    
print("the fibonacci number is:", Fib(8))



