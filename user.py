class Bank:
    def __init__(self,name) -> None:
        self.name = name
        self.__bank_balance = 0
        self.__users = {}
        self.__admins = {}
        self.__transaction_record = {}
        self.__loan_enabled = True
        self.__loan_given = 0
        self.loan_count = {}
        self.__is_bankrupt = False 
    
    def make_user_account(self,user):
        account_no = 100000+len(self.__users)+1
        balance = 0
        self.__transaction_record[account_no] = []
        self.loan_count[account_no] = 0
        self.__users[account_no] = {'name':user.name,'email':user.email,'address':user.address,
        'account_type':user.account_type, 'balance':balance}
        print(f'Account is created. Your account number is {account_no}')
    
    def make_admin_account(self,admin):
        admin_id = 100+len(self.__admins)+1
        self.__admins[admin_id] = {'name':admin.name,'email':admin.email,'address':admin.address}
        print(f'Account is created. Your admin id is {admin_id}')
    
    def del_user_account(self,account_no,admin_id):
        if admin_id in self.__admins:
            if account_no in self.__users:
                del self.__users[account_no]
                print(f'Account {account_no} has been deleted')
            else:
                print('Account not available')
        else:
            print('Invalid Id')

    def user_account_list(self,admin_id):
        if admin_id in self.__admins:
            print('-----------List of users---------')
            for key,value in self.__users.items():
                print(key,value)
        else:
            print('Invalid Id')
    
    def bank_total_balance(self,admin_id):
        if admin_id in self.__admins:
            print(f'Total Balance of the bank - {self.__bank_balance}')
        else:
            print('Invalid Id')

    def total_loan(self,admin_id):
        if admin_id in self.__admins:
            print(f'Total loan of the bank - {self.__loan_given}')
        else:
            print('Invalid Id')
    
    def change_loan_status(self,enable,admin_id):
        if admin_id in self.__admins:
            if enable == 1:
                self.__loan_enabled = True
                print('Loan feature is turned on')
            elif enable == 0:
                self.__loan_enabled = False
                print('Loan feature is turned off')
            else:
                print('Invalid input')
        else:
            print('Invalid Id')
    
    def change_bankruptcy_status(self,enable,admin_id):
        if admin_id in self.__admins:
            if enable == 1:
                self.__is_bankrupt = True
            elif enable == 0:
                self.__is_bankrupt = False
            else:
                print('Invalid input')
        else:
            print('Invalid Id')
    
    def deposit_money(self,account_no,amount):
        if account_no in self.__users and amount>0:
            self.__users[account_no]['balance'] += amount
            self.__bank_balance += amount
            self.__transaction_record[account_no].append(f'Deposited {amount}')
            print(f'{amount} tk has been deposited')
        else:
            print('Account not available')

    def withdraw_money(self,account_no,amount):
        if account_no in self.__users and amount<=self.__users[account_no]['balance']:
            if self.__is_bankrupt == False:
                self.__users[account_no]['balance'] -= amount
                self.__bank_balance -= amount
                self.__transaction_record[account_no].append(f'Withdrew {amount}')
                print(f'{amount} tk has been withdrawn')
            else:
                print('Bank is bankrupt')
        elif account_no in self.__users and amount>self.__users[account_no]['balance']:
            print('Withdrawal amount exceeded')
        else:
            print('Account not available')
    
    
    def transaction_history(self,account_no):
        if account_no in self.__users:
            print(f'transaction history of account {account_no}')
            for value in self.__transaction_record[account_no]:
                print(value)
        else:
            print('Account not available')
    
    def check_balance(self,account_no):
        if account_no in self.__users:
            print(f'Balance of account {account_no}',end=' = ')
            print(self.__users[account_no]['balance'])
        else:
            print('Account not available')
    
    def take_loan(self,amount,account_no):
        if self.__loan_enabled == True:
            if account_no in self.__users and self.loan_count[account_no]<2:
                if self.__is_bankrupt == False: 
                    self.loan_count[account_no] += 1
                    self.__users[account_no]['balance'] += amount
                    self.__loan_given += amount
                    self.__transaction_record[account_no].append(f'Received Loan {amount}')
                    print(f'{amount} tk loan has been sanctioned for account {account_no}')
                else:
                    print('Bank is bankrupt')
            elif account_no in self.__users and self.loan_count[account_no]>=2:
                print('Loan limit exceeded')
            else:
                print('Account not available')
        else:
            print('Loan is currently unavailable')
    
    def transfer_money(self,amount,sender_account_no,receiver_account_no):
        if sender_account_no in self.__users and receiver_account_no in self.__users:
            if amount <= self.__users[sender_account_no]['balance']:
                if self.__is_bankrupt == False:
                    self.__users[sender_account_no]['balance'] -= amount
                    self.__users[receiver_account_no]['balance'] += amount
                    self.__transaction_record[sender_account_no].append
                    (f'transferred {amount } to {receiver_account_no}')
                    self.__transaction_record[receiver_account_no].append
                    (f'Received {amount } from {sender_account_no}')
                    print(f'{amount} tk has been tranferred')
                else:
                    print('Bank is bankrupt')
            else:
                print('Not enough balance')
        else:
            print('Account does not exist')



class User:
    def __init__(self,name,email,address,account_type) -> None:
        self.name = name
        self.email = email
        self.address = address
        self.account_type = account_type

class Admin:
    def __init__(self,name,email,address) -> None:
        self.name = name
        self.email = email
        self.address = address




Brac = Bank('Brac Bank')

while(True):
    print('''-------Welcome------
    Press 1 for going to user panel
    Press 2 for going to admin panel
    Press 3 for exit''')
    y = int(input())
    if y==1:
        while(True):
            print('''----------Welcome to user panel---------
            Press 1 for creating account
            Press 2 for checking balance
            Press 3 for deposit
            Press 4 for withdraw
            Press 5 for transaction history
            Press 6 for taking a loan
            Press 7 for for transferring money
            Press 8 to go back''')
            x = int(input())
            if x==1:
                name = input('Name : ')
                email = input('Email : ')
                address = input('Address : ')
                account_type = input('Account_type(Savings or Current) : ')
                Acc = User(name,email,address,account_type)
                Brac.make_user_account(Acc)
            elif x==2:
                account_no = int(input('Enter account no : '))
                Brac.check_balance(account_no)
            elif x==3:
                amount = int(input('Enter amount : '))
                account_no = int(input('Enter account no : '))
                Brac.deposit_money(account_no,amount)
            elif x==4:
                amount = int(input('Enter amount : '))
                account_no = int(input('Enter account no : '))
                Brac.withdraw_money(account_no,amount)
            elif x==5:
                account_no = int(input('Enter account no : '))
                Brac.transaction_history(account_no)
            elif x==6:
                amount = int(input('Enter amount : '))
                account_no = int(input('Enter account no : '))
                Brac.take_loan(amount,account_no)
            elif x==7:
                amount = int(input('Enter amount : '))
                sender_account_no = int(input('Enter sender account no : '))
                receiver_account_no = int(input('Enter receiver account no : '))
                Brac.transfer_money(amount,sender_account_no,receiver_account_no)
            else:
                break
    elif y == 2:
        while(True):
            print('''---------Welcome to admin panel---------
            Press 1 for creating admin account
            Press 2 for deleting user account
            Press 3 to see all user list
            Press 4 to see total balance of bank
            Press 5 to see total loan amount
            Press 6 to change loan feature on or off
            Press 7 to change bankruptcy status
            Press 8 to go back''')
            x = int(input())
            if x==1:
                name = input('Name : ')
                email = input('Email : ')
                address = input('Address : ')
                Adm = Admin(name,email,address)
                Brac.make_admin_account(Adm)
            elif x==2:
                account_no = int(input('Enter the account number you want to delete : '))
                admin_id = int(input('Enter your ID : '))
                Brac.del_user_account(account_no,admin_id)
            elif x==3:
                admin_id = int(input('Enter your ID : '))
                Brac.user_account_list(admin_id)
            elif x==4:
                admin_id = int(input('Enter your ID : '))
                Brac.bank_total_balance(admin_id)
            elif x==5:
                admin_id = int(input('Enter your ID : '))
                Brac.total_loan(admin_id)
            elif x==6:
                admin_id = int(input('Enter your ID : '))
                enable = int(input('Enter loan feature status(Press 1 for Enabling or 0 for Disabling) : '))
                Brac.change_loan_status(enable,admin_id)
            elif x==7:
                admin_id = int(input('Enter your ID : '))
                enable = int(input('Enter bankruptcy status(Press 1 for Yes or 0 for No) : '))
                Brac.change_bankruptcy_status(enable,admin_id)
            else:
                break
    else:
        break

    
    
        



    


    

    
    

        