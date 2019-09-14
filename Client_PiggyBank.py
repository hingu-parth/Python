import socket;

conn = socket.socket()
conn.connect(("localhost",8091))

user=input('Kindly enter your name: ')


print('Hi,', user, 'Welcome to the Piggy Bank')

username = input("Enter a Username> ")
conn.send(username.encode(encoding='utf_8',errors='strict'))

password = input("Enter a Password> ")
conn.send(password.encode(encoding='utf_8',errors='strict'))

user=conn.recv(1024).decode()
print('-->  ',user)
while user!='Invalid':
    balance=conn.recv(1024).decode()
    print('Your initial Balance is: ',balance)

    while user != "Invalid":
        user=input('Would you like to Deposit, Withdraw amount or view Last Transactions? ')
        conn.send(user.encode(encoding='utf_8',errors='strict'))

        if user =='deposit':   
            deposit_value=input("Kindly enter deposite value")
            conn.send(deposit_value.encode(encoding='utf_8',errors='strict'))
            balance=conn.recv(1024).decode()
            lt=conn.recv(1024).decode()
            print('Your current balance is ',balance)
            print('Your last transaction was ',lt)

        else:
            if user=='withdraw':
                withdrawal_value=input("Kindly enter deposite value")
                conn.send(withdrawal_value.encode(encoding='utf_8',errors='strict'))
                balance=conn.recv(1024).decode()
                lt=conn.recv(1024).decode()
                print('Your current balance is ',balance)
                print('Your last transaction was ',lt)

            else:
                if user=='last transaction':
                    last_transaction=input('Enter number of transactions to be viewed: ')
                    conn.send(last_transaction.encode(encoding='utf_8',errors='strict'))
                    
                    last=conn.recv(1024).decode()
                    print(last)
                else:
                    if user=='exit':
                        user='Invalid'
                        conn.send(user.encode(encoding='utf_8',errors='strict'))
                        print('See you soon')
