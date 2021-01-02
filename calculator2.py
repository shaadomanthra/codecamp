a  = input("Enter one number:")
a = int(a)
b = input("Enter second number:")
b = int(b)
opr = input("Enter the operation (add/subtract/multiply):")

if opr == 'add':
    result = a + b
    print('The adddition is ',result)
elif opr == 'subtract':
    result = a - b
    print('The subtraction is ', result)
elif opr == 'multiply':
    result = a * b
    print("The multiplication is ", result)
else:
    print("I dont understand what you asked for!")
