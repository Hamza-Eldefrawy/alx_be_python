class BankAccount:
    def __init__(self, initial_balance=0):
        """
        Initialize the account.
        The initial_balance is optional and defaults to 0.
        """
        self.account_balance = initial_balance

    def deposit(self, amount):
        """
        Adds the specified amount to the account balance.
        """
        if amount > 0:
            self.account_balance += amount

    def withdraw(self, amount):
        """
        Deducts amount if funds are sufficient.
        Returns True if successful, False if insufficient funds.
        """
        if amount <= self.account_balance:
            self.account_balance -= amount
            return True
        else:
            return False

    def display_balance(self):
        """
        Prints the current balance in a user-friendly format.
        """
        print(f"Current Balance: ${self.account_balance:.2f}")
