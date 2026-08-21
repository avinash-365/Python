from abc import ABC , abstractmethod
import random 
from datetime import date

class person:
    def __init__(self,cust_name,cust_age,cust_address):
        self.name = cust_name
        self.age = cust_age
        self.address = cust_address

    def display(self):
        print(f"Customer name: {self.name}\nCustomer age: {self.age}\nCustomer address: {self.address}")

class customer(person):
    def __init__(self,cust_name,cust_age,cust_address,cust_bank_name = "SBI"):
        super().__init__(cust_name,cust_age,cust_address)
        self.bank_name = cust_bank_name
        self.id = random.randint(1000,9999)

    def display(self):
        print(f"ID: {self.id}\nBank: {self.bank_name}") 
        return super().display()
        

class account(ABC):
    total_accounts = 0
    def __init__(self,acc_holder,acc_balance = 0):
        self.number = random.randint(10000000000000,99999999999999)
        self.holder_name = acc_holder
        self.__balance = acc_balance
        account.total_accounts += 1
        self.transactions = []

    @classmethod 
    def get_total_accounts(cls):
        return cls.total_accounts

    @staticmethod
    def validate_account_number(acc_no):
        if len(str(acc_no)) == 14: 
            return True 

        else: 
            return False

    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self,acc_balance):    
        self.__balance = acc_balance

    def __str__(self):
        return f"Account No: {self.number}\nBalance: {self.balance}\nAccount Type: {self.account_type()}"

    @abstractmethod
    def withdraw(self,amount):
        pass

    @abstractmethod
    def account_type(self):
        pass

    def deposit(self,amount):
        if amount <= 0:
            raise invalidAmountError("The amount should be positive.!")
        else:
            self.__balance += amount
            self.transactions.append(f"Deposited: {amount} | New Balance: {self.balance}")

    def __eq__(self, other):
        if self.number == other.number: 
            return True 
        else: 
            return False
        
    def print_statement(self):
        if len(self.transactions) == 0:
            print("No transactions yet!")  

        else:
            print(f"--- Transaction History ---")
            for t in self.transactions:
                print(t)

class saving_acc(account):
    def __init__(self, acc_holder,interest_rate, acc_balance=0,):
        super().__init__(acc_holder, acc_balance)
        self.rate = interest_rate

    def withdraw(self,amount):
        if amount <= 0:
            raise invalidAmountError("The amount should be positive.!")
        if amount > self.balance:
            raise insufficientFundsError("Balance Low !")
        else:
            self.balance -= amount
            self.transactions.append(f"Withdrew: {amount} | New Balance: {self.balance} | Date: {date.today()}")

    def add_interest(self):
        # Formula: (Balance * Rate) / 100
        interest_amount = (self.balance * self.rate) / 100
        
        if interest_amount > 0:
            self.balance += interest_amount
            self.transactions.append(f"Interest Added: {interest_amount} | New Balance: {self.balance} | Date: {date.today()}")
            print(f" ₹{interest_amount} interest added! New Balance is ₹{self.balance}")
        else:
            print("Balance is zero or negative. No interest added.")

    def account_type(self):
        return "Saving Account"

class current_acc(account):
    def __init__(self, acc_holder,overdraft_limit ,acc_balance=0):
        super().__init__(acc_holder, acc_balance)
        self.overdraft_limit = overdraft_limit

    def withdraw(self,amount):
        if self.balance + self.overdraft_limit <     amount:
            raise insufficientFundsError("The overdraft limit has been exceeded.!")

        else:
            self.balance -= amount
            self.transactions.append(f"Withdrew: {amount} | New Balance: {self.balance} | Date: {date.today()}")

    def account_type(self):
        return "Current Account"

class transaction:
    pass
    # aa class no use account ma lai lidho chhe

class bank:
    def __init__(self):
        self.customers = []
        self.accounts = []

    def add_customer(self, customer_obj):
        self.customers.append(customer_obj)
        print("\nCustomer Successfully Added!")

    def add_account(self,account_obj):
        self.accounts.append(account_obj)
        print("\nAccount Added Successfully!")

class insufficientFundsError(Exception):
    def __init__(self, message="Low balance!"):
        super().__init__(message)

class invalidAmountError(Exception):
    def __init__(self, message="The amount is invalid.!"):
        super().__init__(message)

my_bank = bank()
while True:
    print('''
===== BANK MANAGEMENT SYSTEM =====

1. Create New Account
2. Deposit Money
3. Withdraw Money
4. Transfer Money
5. Check Balance
6. Print Statement
7. View Total Accounts (classmethod)
8. Exit
''')

    choice = int(input("Enter Your Choice:"))

    if choice == 1:
        print("\n--- Please Enter Basic Details ---")
        cust_name = input("Enter Customer Name: ")
        cust_age = int(input("Enter Customer Age: "))
        cust_address = input("Enter Customer Address: ")

        # 1. Create a customer object and add it to the bank.
        cust_obj = customer(cust_name, cust_age, cust_address)
        my_bank.add_customer(cust_obj)

        print("\n1. Saving Account\n2. Current Account")
        sub_choice = int(input("Enter Your Choice for Account Type: "))

        if sub_choice == 1:
            interest_rate = float(input("Enter Interest rate: "))
            
            # Create a Savings Account object.
            sav_obj = saving_acc(acc_holder=cust_name, interest_rate=interest_rate)
            # Open an account at the bank.
            my_bank.add_account(sav_obj)
            
            print(f"\n Saving Account Successfully Opened! Your A/c No is: {sav_obj.number}")

        elif sub_choice == 2:
            overdraft_limit = int(input("Enter Overdraft Limit: "))
            
            # Create an object of the Current Account (the Current_Acc class will be used here).
            cur_obj = current_acc(acc_holder=cust_name, overdraft_limit=overdraft_limit)
            # Open an account at the bank.
            my_bank.add_account(cur_obj)
            
            print(f"\n Current Account Successfully Opened! Your A/c No is: {cur_obj.number}")

        else:
            print("Invalid Choice! Account not created.")

    elif choice == 2:
        account_number = int(input("Pelase Enter Your Account Number to deposite : "))

        account_found = False
        for acc_obj in my_bank.accounts:
            if acc_obj.number == account_number:
                account_found = True
                amount = int(input("Enter To amount Deposit: "))
                try:
                    acc_obj.deposit(amount)
                    print("Sucessfully Deposit")
                except invalidAmountError as e:
                    print(e)
                break
        if not account_found:
            print("Account not found!")

    elif choice == 3:
        account_number = int(input("Please Enter Your Account Number to withdraw: "))
        account_found = False
        
        for acc_obj in my_bank.accounts:
            if acc_obj.number == account_number:
                account_found = True
                amount = int(input("Enter amount to Withdraw: "))
                try:
                    acc_obj.withdraw(amount)
                    print(f" Successfully Withdrawn! New Balance: {acc_obj.balance}")
                except (insufficientFundsError, invalidAmountError) as e:
                    print(f" Error: {e}")
                break
                
        if not account_found:
            print(" Account not found!")

    elif choice == 4:
        sender_ac = int(input("Enter Sender Account Number: "))
        receiver_ac = int(input("Enter Receiver Account Number: "))
        amount = int(input("Enter Amount to transfer: "))

        sender_obj = None
        receiver_obj = None

        for acc in my_bank.accounts:
            if acc.number == sender_ac:
                sender_obj = acc
            if acc.number == receiver_ac:
                receiver_obj = acc

        if sender_obj is not None and receiver_obj is not None:
            
            if sender_obj == receiver_obj:
                print("Error: The sender and receiver accounts must not be the same.!")
            else:
                try:
                    sender_obj.withdraw(amount)   #  sender  
                    receiver_obj.deposit(amount)  #  receiver   
                    
                    print(f"\nSuccessfully Transferred ₹{amount} to Account No: {receiver_obj.number}")
                    print(f"Your (Sender) New Balance is: ₹{sender_obj.balance}")
                
                except (insufficientFundsError, invalidAmountError) as e:
                    print(f"\nTransfer Failed: {e}")
                    
        else:
            if sender_obj == None:
                print("Sender Account not found!")
            if receiver_obj == None:
                print("Receiver Account not found!")


    elif choice == 5:
        account_number = int(input("Please Enter Your Account Number: "))
        account_found = False
        
        for acc_obj in my_bank.accounts:
            if acc_obj.number == account_number:
                account_found = True
                # Magic method __str__ call 
                print(acc_obj) 
                break
                
        if not account_found:
            print("Account not found!")

    elif choice == 6:
        account_number = int(input("Please Enter Your Account Number: "))
        account_found = False
        
        for acc_obj in my_bank.accounts:
            if acc_obj.number == account_number:
                account_found = True
                acc_obj.print_statement()
                break
                
        if not account_found:
            print("Account not found!")
    
    elif choice == 7:
        total = account.get_total_accounts()
        print(f"Total Accounts in Bank: {total}")

        search_ac = int(input("Enter Account Number to view details: "))
        acc_found = False

        for acc in my_bank.accounts:
            if acc.number == search_ac:
                acc_found = True
                
                print("\n" + "="*35)
                print("   ACCOUNT & CUSTOMER DETAILS")
                print("="*35)
                
                print(f"Account Number : {acc.number}")
                print(f"Account Type   : {acc.account_type()}")
                print(f"Current Balance: ₹{acc.balance}")
                
                if isinstance(acc, saving_acc):
                    print(f"Interest Rate  : {acc.rate}%")
                elif isinstance(acc, current_acc):
                    print(f"Overdraft Limit: ₹{acc.overdraft_limit}")
                
                print("-" * 35)

                cust_found = False
                for cust in my_bank.customers:
                    if cust.name == acc.holder_name:
                        cust_found = True
                        print(f"Customer ID    : {cust.id}")
                        print(f"Holder Name    : {cust.name}")
                        print(f"Age            : {cust.age}")
                        print(f"Address        : {cust.address}")
                        print(f"Bank Name      : {cust.bank_name}")
                        break
                
                if not cust_found:
                    print(f"Holder Name    : {acc.holder_name}")

                print("="*35 + "\n")
                break

        if not acc_found:
            print("Account not found!")

    elif choice == 8:
        break

    else:
        print("Error :Please Enter Vaild Choice")