class BankAccount: #This is the constructor of the class
    def __init__(self, account_number, balance, account_holder):
        self.__balance = balance 
        self.__account_number = account_number  
        self.__account_holder = account_holder  # These are the variables of the class
        

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited: {amount}. New balance: {self.__balance}")
        else:
            print("Deposit amount must be positive.") # This is the deposti method where it allows user to deposit money into the account and it checks if the amount is positive or not. 
            # If it is positive then it adds the amount to the balance and prints the new balance. If it is negative then it prints a message saying that the deposit amount must be positive.

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrew: {amount}. New balance: {self.__balance}")
        else:
            print("Insufficient funds or invalid withdrawal amount.") # This is the withdraw method where the user can withdraw money and if there is not enough 
            # money within the account then it will print a message saying there is not enough money.

    def accountinfo(self): # This method is how we get the account information
        return {
            "Account Number": self.__account_number, 
            "Account Holder": self.__account_holder,
            "Balance": self.__balance
        }
    
    def get_balance(self):
        return self.__balance # This method is how we get the balance



# This is Example Usage of bankaccount class
a = int(input("Enter account number: "))
b = input("Enter account holder name: ")
c = int(input("Enter initial balance: "))
d = int(input("Enter withdrawal amount: "))
e = int(input("Enter deposit amount: "))

a1 = BankAccount(a, c, b)
#update balance using deposit and withdraw methods.
a1.deposit(e)
print(a1.get_balance())  
a1.withdraw(d)  
print(a1.accountinfo()) # A hypothetical example where all methods are used.



# Mamaaaaa
