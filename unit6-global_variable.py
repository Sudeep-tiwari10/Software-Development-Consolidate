total = 2 #global variable

def add_to_total(number):
    #we have to add global to use the variable from outside the function.
    global total
    total += number
    return total
print("the running total is:", add_to_total(5))
print("the running total is:", add_to_total(15))
print("the running total is:", add_to_total(10))