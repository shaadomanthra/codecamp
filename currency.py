amt = input("Enter the amount in rupee:")
amt = int(amt)
c = input("Enter the conversion (dollar/dhiram/euro):")

if c == 'dollar':
    conv = amt / 73
    print("Amount in dollars is ",conv)
elif c == 'dhiram':
    conv = amt / 20
    print("Amount in dhirams is ",conv)
elif c == 'euro':
    conv = amt / 89
    print("amount in euro is ",conv)
else:
    print("I dont understand")
