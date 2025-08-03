class BankAccount:
    def __init__(self, initial_balance=0):
        # Encapsulated balance
        self.__account_balance = initial_balance

    def deposit(self, amount):
        # Only accept positive deposits
        if amount > 0:
            self.__account_balance += amount

    def withdraw(self, amount):
        # Only allow withdrawal if funds suffice and amount is positive
        if 0 < amount <= self.__account_balance:
            self.__account_balance -= amount
            return True
        return False

    def display_balance(self):
        # Print the current balance
        print(f"Current Balance: ${self.__account_balance}")
