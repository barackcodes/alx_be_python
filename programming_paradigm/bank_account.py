class BankAccount:
    def __init__(self,accont_balance = 0):
        self.account_balance = accont_balance
        
    def deposit(self,amount):
        if amount > 0:
            self.account_balance += amount
        else:
            print("Deposit amount must be positive.")
    
    def withdrawal(self, amount):
        if amount <= 0:
            print("Withdrawal must be positive.")
            return False
        if amount <= self.account_balance:
            self.account_balance -= amount
            return True
        else:
            def display_balance(self):
                print("Current Balance: {self.account_balance:.2f}")