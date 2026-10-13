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

    # Setter method for balance with validation against negative values
    def set_balance(self, balance):
        if balance < 0:
            print("The balance must be not be a negative number.")
        else:
            self._balance = float(balance)
