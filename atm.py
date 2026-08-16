balance = 5000

print("----- ATM SYSTEM -----")
print("1. Check Balance")
print("2. Deposit Money")
print("3. Withdraw Money")

choice = int(input("Enter your choice: "))

if choice == 1:
    print("Your Balance is:", balance)

elif choice == 2:
    amount = int(input("Enter amount: "))
    balance = balance + amount
    print("Updated Balance:", balance)

elif choice == 3:
    amount = int(input("Enter amount: "))
    
    if amount <= balance:
        balance = balance - amount
        print("Withdrawal Successful!")
        print("Remaining Balance:", balance)
    else:
        print("Insufficient Balance!")

else:
    print("Invalid Choice!")