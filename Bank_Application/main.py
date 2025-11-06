'''
services --> login, withdraw, deposit, transactions, statements, logout
 Creating Tables 
 accounts_table = {account/username:password}
 users_table = {account:[amount,name,email]}
'''
accounts_table = {101: 123, 102: 789}
users_table = { 101 : [1000,'Sowjanya', 'sowji123@gmail.com'], 
                102 : [500, 'Harshitha', 'harshi123@gmail.com']  }

#login function
def login(username:int,password:int):
    print('=========================')
    # checking whether user entered correct details or not
    if username in accounts_table:
        if password == accounts_table[username]: 
            print('*Login Successful*')
            return True
        else:
            print('!Check your password')
            return False
    else:
        print('!Username not found')
        return False


#withdraw func
def withdraw(account:int,withdraw_amount:int):
    print('=========================')
    if account in users_table:
        # checking for sufficient balance
        if withdraw_amount <= users_table[account][0]:
            users_table[account][0] -= withdraw_amount  # deducting amount from balance
            print(f'{withdraw_amount} Withdraw Successful and current balance is :{users_table[account][0]}')

        else:
            print('Insuffcient Balance')
            
    else:
        print('User not found')

#deposit func
def deposit(account:int,deposit_amount:int):
    print('=========================')
    if account in accounts_table:

        users_table[account][0] += deposit_amount  # adding amount to balance
        print(f'{deposit_amount} Deposit Successful and current balance is :{users_table[account][0]}')
    
    else:
        print('User not found')

#transaction func
def transac(sender_ac:int,receiver_ac:int, transfer_amount:int):    
    print('=========================')
    if sender_ac in users_table:
        receiver_ac = int(input('Enter receiver account number: '))
        if receiver_ac in users_table:
            if users_table[sender_ac][0] >= transfer_amount: 
                users_table[sender_ac][0] -= transfer_amount
                users_table[receiver_ac][0] += transfer_amount
                print(f'{transfer_amount} transferred successfull and current_balance is :{users_table[sender_ac][0]}')
            else:
                print('Insufficient Balance')
        else:
            print('Reciever account not found')
    else:
        print('User account not found')

#statements func
def statements(account:int):
    print('==========Not Available rn===============')
    
# balance enquiry func 
def balanceenquiry(account:int):
    print('=========================')
    if account in users_table:
        print(f'Current balance is :{users_table[account][0]}')
    else:
        print('User not found')

#logout func
def logout():
    print('=========================')
    exit()

if __name__ == "__main__":
    print('\n \n **** Welcome to ABC Bank Application ***')
    username = int(input('Enter your account number: '))
    password = int(input('Enter your password: '))
    login_val = login(username = username, password = password)  
    while login_val:
       operations = ("\n"
                     " 1.Withdraw \n",
                     "2.Deposit \n",
                     "3.Transactions \n",
                     "4.Statements \n",
                     "5.Balance Enquiry \n",
                     "6.Logout \n"
                     )
       print(*operations)  
       choice = int(input('Select the operations: '))
       if choice == 1:
           withdraw(account = username, withdraw_amount = int(input('Enter amount to withdraw: '))) 
       elif choice == 2:
           deposit(account = username , deposit_amount = int(input('Enter amount to deposit: '))) 
       elif choice == 3 :
           transac(sender_ac = username, receiver_ac = username, transfer_amount = int(input('Enter the amount to transfer: ')))
       elif choice == 4:
           statements(account = username)
       elif choice == 5:
           balanceenquiry(account = username)
       elif choice == 6:
           logout()
       else:

           print('** Please select the operations in between 1 to 6.. **')
