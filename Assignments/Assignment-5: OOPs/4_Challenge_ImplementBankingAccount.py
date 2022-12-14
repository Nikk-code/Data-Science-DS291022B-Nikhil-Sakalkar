# Challenge 4: Implement a Banking Account

class Account:
    def __init__(self,title = None,account_balance = 0):
        self.title = title
        self.acount_balance = account_balance
    

class Savings_account(Account):
    def __init__(self,title = None,account_balance = 0 ,intrest_rate = 0):
        super().__init__(title,account_balance)
        self.intrest_rate = intrest_rate

    def display(self):
        super().display()
        return self.intrest_rate
        

saving =Savings_account("Ashish",5000,5)
print("Title : ",saving.title)
print("Account Balance: ",saving.acount_balance)
print("Intrest Rate : ",saving.intrest_rate)
