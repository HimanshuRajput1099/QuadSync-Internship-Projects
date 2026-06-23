accounts = {}

def create_account():
    acc_no = input("Enter Account Number: ")

    if acc_no in accounts:
        print("Account already exists!")
        return

    name = input("Enter Account Holder Name: ")
    balance = float(input("Enter Initial Balance: "))

    if balance < 0:
        print("Balance cannot be negative!")
        return

    accounts[acc_no] = {
        "name": name,
        "balance": balance
    }

    print("Account Created Successfully!")

def deposit():
    acc_no = input("Enter Account Number: ")

    if acc_no not in accounts:
        print("Account not found!")
        return

    amount = float(input("Enter Amount: "))

    if amount <= 0:
        print("Invalid amount!")
        return

    accounts[acc_no]["balance"] += amount
    print("Amount Deposited Successfully!")

def withdraw():
    acc_no = input("Enter Account Number: ")

    if acc_no not in accounts:
        print("Account not found!")
        return

    amount = float(input("Enter Amount: "))

    if amount > accounts[acc_no]["balance"]:
        print("Insufficient Balance!")
        return

    accounts[acc_no]["balance"] -= amount
    print("Amount Withdrawn Successfully!")

def check_balance():
    acc_no = input("Enter Account Number: ")

    if acc_no not in accounts:
        print("Account not found!")
        return

    print("Current Balance:", accounts[acc_no]["balance"])

def show_accounts():
    if not accounts:
        print("No accounts available.")
        return

    for acc_no, details in accounts.items():
        print("-------------------")
        print("Account No:", acc_no)
        print("Name:", details["name"])
        print("Balance:", details["balance"])

while True:
    print("\n===== BANKING SYSTEM =====")
    print("1. Create Account")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Check Balance")
    print("5. Show All Accounts")
    print("6. Exit")

    choice = input("Enter Your Choice: ")

    if choice == "1":
        create_account()
    elif choice == "2":
        deposit()
    elif choice == "3":
        withdraw()
    elif choice == "4":
        check_balance()
    elif choice == "5":
        show_accounts()
    elif choice == "6":
        print("Thank You!")
        break
    else:
        print("Invalid Choice!")