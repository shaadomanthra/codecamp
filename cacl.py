a = input("Enter first number:")
a = int(a)

b = input("Enter the second number:")
b = int(b)

m = input("Enter the operation (add/subtract):")

if m == 'add':
    result = a + b
    print("the addition is ",result)
elif m == 'subtract':
    result = a - b
    print("The subtraction is ",result)
else:
    print("I dont understand!")