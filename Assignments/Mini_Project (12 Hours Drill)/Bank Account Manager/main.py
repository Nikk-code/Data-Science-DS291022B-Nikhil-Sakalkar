import random
import sys
 
class ATM():
    def __init__(self, name, account_number, balance = 0):
        self.name = name
        self.account_number = account_number
        self.balance = balance
         
    def account_detail(self):
        print("\n----------ACCOUNT DETAIL----------")
        print(f"Account Holder: {self.name.upper()}")
        print(f"Account Number: {self.account_number}")
        print(f"Available balance: RS.{self.balance}\n")
         
    def deposit(self, amount):
        self.amount = amount
        self.balance = self.balance + self.amount
        print("Current account balance: RS.", self.balance)
        print()
 
    def withdraw(self, amount):
        self.amount = amount
        if self.amount > self.balance:
            print("Insufficient fund!")
            print(f"Your balance is RS.{self.balance} only.")
            print("Try with lesser amount than balance.")
            print()
        else:
            self.balance = self.balance - self.amount
            print(f"RS.{amount} withdrawal successful!")
            print("Current account balance: RS.", self.balance)
            print()
 
    def check_balance(self):
        print("Available balance: RS.", self.balance)
        print()
 
    def transaction(self):
        print("""
            TRANSACTION 
        *********************
            Menu:
            1. Account Detail
            2. Check Balance
            3. Deposit
            4. Withdraw
            5. Exit
            0. Close
        *********************
        """)
        
        while True:
            try:
                option = int(input("Enter 1, 2, 3, 4 or 5:"))
            except:
                print("Error: Enter 1, 2, 3, 4, or 5 only!\n")
                continue
            else:
                if option == 1:
                    atm.account_detail()
                elif option == 2:
                    atm.check_balance()
                elif option == 3:
                    amount = int(input("How much you want to deposit(RS.):"))
                    atm.deposit(amount)
                elif option == 4:
                    amount = int(input("How much you want to withdraw(RS.):"))
                    atm.withdraw(amount)
                elif option == 5:
                    print(f"""
                printing receipt..............
          ******************************************
              Transaction is now complete.                         
              Transaction number: {random.randint(10000, 1000000)} 
              Account holder: {self.name.upper()}                  
              Account number: {self.account_number}                
              Available balance: RS.{self.balance}                    
 
              Thanks for choosing us as your bank                  
          ******************************************
          """)
                elif option == 0:
                    sys.exit()
                 
 
print("*******WELCOME TO HDFC BANK*******")
print("___________________________________________________________\n")
print("----------ACCOUNT CREATION----------")
name = input("Enter your name: ")
account_number = input("Enter your account number: ")
print("Congratulations! Account created successfully......\n")
 
atm = ATM(name, account_number)
 
while True:
    trans = input("Do you want to do any transaction?(y/n):")
    if trans == "y":
        atm.transaction()
    elif trans == "n":
        print("""
    -------------------------------------
   | Thanks for choosing HDFC bank |
   | Visit us again!                     |
    -------------------------------------
        """)
        break
    else:
        print("Wrong command!  Enter 'y' for yes and 'n' for NO.\n")