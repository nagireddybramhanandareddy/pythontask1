class ATM:
    def __init__(self, balance):
        self.balance = balance

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds")
        else:
            self.balance -= amount
            print("Withdrawal successful")

    def deposit(self, amount):
        self.balance += amount
        print("Deposit successful")

    def check_balance(self):
        print("Your balance is", self.balance)

atm = ATM(1000)

while True:
    print("1. Withdraw")
    print("2. Deposit")
    print("3. Check balance")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        amount = int(input("Enter the amount to withdraw: "))
        atm.withdraw(amount)
    elif choice == 2:
        amount = int(input("Enter the amount to deposit: "))
        atm.deposit(amount)
    elif choice == 3:
        atm.check_balance()
    elif choice == 4:
        break
    else:
        print("Invalid choice")
