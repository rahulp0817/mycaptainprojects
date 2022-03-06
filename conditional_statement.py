# Fibonacci program

def fibonacci(n):
    if n < 0:
     print(" Incorrect Input ")
    elif n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
print(fibonacci(9))

# To find positive values 

list1 = [12, -7, 5, 64, -14]
for i in list1:
    if i > 0:
        print(i, end = "  ")
        
list2 = [12, 14, -95, 3]
for i in list2:
    if i > 0:
        print(i, end = "  ")
