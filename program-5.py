
class BankAccount:
    def __init__(self, name):
        self.name = name
        self.__balance = 0
        self.transactions = []

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            self.transactions.append("Deposit: " + str(amount))
            print("Deposit successful")
        else:
            print("Invalid amount")

    def withdraw(self, amount):
        if amount > 0 and amount <= self.__balance:
            self.__balance -= amount
            self.transactions.append("Withdrawal: " + str(amount))
            print("Withdrawal successful")
        else:
            print("Invalid amount or insufficient balance")

    def transfer(self, other, amount):
        if amount > 0 and amount <= self.__balance:
            self.__balance -= amount
            other.__balance += amount
            self.transactions.append("Transfer: " + str(amount))
            other.transactions.append("Received: " + str(amount))
            print("Transfer successful")
        else:
            print("Invalid amount or insufficient balance")

    def show_balance(self):
        print("Balance:", self.__balance)

    def show_transactions(self):
        print("Transaction History:")
        for t in self.transactions:
            print(t)


try:
    a1 = BankAccount("Vinutha")
    a2 = BankAccount("Rahul")

    a1.deposit(float(input("Enter deposit amount: ")))
    a1.withdraw(float(input("Enter withdrawal amount: ")))
    a1.transfer(a2, float(input("Enter transfer amount: ")))

    print("\nAccount 1:")
    a1.show_balance()
    a1.show_transactions()

    print("\nAccount 2:")
    a2.show_balance()
    a2.show_transactions()

except ValueError:
    print("Enter a valid number")
