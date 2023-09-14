class BankAccount:
   def __init__(self, account_number,account_holder_name,initial_balance=0.0):
      self.__account_number =account_number
      self.__account_holder_name= account_holder_name
      self.__account_balance = initial_balance
   def deposit(self, amount):
      if amount > 0:
        self.__account_balance += amount 
        print("Deposited ₹{}.New balance: ₹{}". format(amount, self.__account_balance))
      else:
         print("Invalid deposit amoun. please deposit a positive amount.")
   def withdrawal(self, amount):
     if amount > 0 and amount <= self. __account_balance:
        self.__account_balance -= amount
        print("withdrawal ₹{}.New balance: ₹{}" .format(amount,self.__account_balance))
     else:
        print("Invalidwithdrawal amount or insufficient balance.")
   def display_balance(self):
        print("Account balance for {}(Account #{}): ₹{}".format(self.__account_holder_name,self.__account_number,self. __account_balance))
# create an instance of the BankAccount class 
Account = BankAccount(account_number="123456789",account_holder_name="sai",initial_balance =5000.0)
# Test deposit and withdrawal functionality 
Account.display_balance()
Account.deposit(500.0)
Account.withdrawal(200.0)
Account.display_balance()
      
       
