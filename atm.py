pin = "1234"
balance = 1000
transactions = []
withdrawal_limit =50000

print("welcome to My Atm")

entered_pin = input("Enter your 4-digit PIN:")

if entered_pin == pin:
    print("PIN Accepted\n")
    while True:
        print("----ATM Menu----")
        print("1. Check Balance")
        print("2. Deposite Money")
        print("3. Withdraw Money")
        print("4. Transaction History")
        print("5. Exit")

        choice = input("Enter your choices:")

        if choice == "1":
             print(f"Your Balance: {balance}Rs\n") 

        elif choice == "2":
             try:
                amount = int(input("Enter amount to deposit:"))
                if amount <= 0:
                   print(" Amount must be positive.\n")
                else:
                     balance += amount
                     transactions.append(f"Deposited: {amount} Rs")
                     print(f"{amount} Rs Deposited Successfully\n")
             except ValueError:
                 print("Invalid input.\n")

        elif choice == "3":
            try:
                amount = int(input("Enter amount to withdraw:"))
                if amount <= 0:
                    print("Amount must be positive.\n")
                elif amount > balance:
                    print("Insufficent Balance!\n")
                elif amount > withdrawal_limit:
                    print(f"Withdrawl limit exceeded! (Max {withdrawal_limit} Rs per day)\n)")
                else:
                    balance -= amount
                    transactions.append(f"withdrew: {amount} Rs")
                    print(f"{amount} Rs Withdrawn Successfully\n")
            except ValueError:
                print("Invalid input.\n")

        elif choice == "4":
             if not transactions:
                 print("No Transaction Yet\n")
             else:
                 print("Transaction History:")
                 for t in transaction[-5:]:
                     print("-", t)
                 print()

        elif choice == "5":
            print("Thank you for using our ATM!")
            break

        else:
              print("Invalid Choice, try again!\n") 
else:
      print("Wrong PIN! Access Denied.")
