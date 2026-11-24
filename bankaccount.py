class Bank:
    def __init__(self, acc_no, name, acc_type, balance):
        self.acc_no = acc_no
        self.name = name
        self.acc_type = acc_type
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print("Deposited successfully")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print("Withdrawn successfully")
        else:
            print("Insufficient balance")

    def display(self):
        print("Account Number:", self.acc_no)
        print("Name:", self.name)
        print("Account Type:", self.acc_type)
        print("Balance:", self.balance)

acc = Bank(
    input("Enter account number: "),
    input("Enter name: "),
    input("Enter account type: "),
    float(input("Enter balance: "))
)

amount = float(input("Enter deposit amount: "))
acc.deposit(amount)

amount = float(input("Enter withdrawal amount: "))
acc.withdraw(amount)

acc.display()
