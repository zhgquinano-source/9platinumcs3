class BankAccount:
    def __init__(self, account_number, balance):
        # Initialize private attributes
        self._account_number = None
        self._balance = 0.0
        
        # Use setter methods to set initial values
        self.set_account_number(account_number)
        self.set_balance(balance)

    # Setter method for account_number
    def set_account_number(self, account_number):
        self._account_number = account_number

    # Getter method for account_number
    def get_account_number(self):
        return self._account_number

    # Setter method for balance that prevents negative values
    def set_balance(self, balance):
        if balance < 0:
            print("The balance must be not be a negative number.")
        else:
            self._balance = balance

    # Getter method to retrieve the balance
    def get_balance(self):
        return self._balance

# Displays the bank account info
print("a1 = BankAccount(12345, 1000)\n")

# Create an object of the BankAccount class
a1 = BankAccount(12345, 1000)

# Print initial account details matching the sample output
print("Output:")
print("Account 1")
print("Account Number:", a1.get_account_number())
print(f"Balance: {a1.get_balance():.2f}\n")

# Try updating the balance to a negative value
print("Update balance to -100")
a1.set_balance(-100)
# Print final account details to show the balance remains unchanged
print("Account Number:", a1.get_account_number())
print(f"Balance: {a1.get_balance():.2f}")
