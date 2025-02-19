# A program that takes a list as input and doubles each element

def double_element(numbers):
    for i in range(len(numbers)):
        numbers[i] *= 2 #short hand for numbers[i] = numbers[i] * 2
        
    
myList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print("the original list", myList)

double_element(myList)
print("the double elements list:", myList)