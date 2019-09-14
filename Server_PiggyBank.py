import socket
import time

balance=0
lt=0

localtime = time.asctime( time.localtime(time.time()))

myfile=open('piggy_bank.txt','a+')
myfile.write('\n {} '.format(localtime))
myfile.write('Credit        Debit       Amount \n')

def deposit(v):
    global balance
    global lt
    if v>0:
        balance=balance+v
        lt= v
        myfile.write('                           {}'.format(lt))
        myfile.write('                          {} \n'.format(balance))
        myfile.write('---------------------------------------------------------------------------- \n')
    else:
        print('Ops! Invalid Format.')


def withdraw(w):
    global balance
    global lt
    if balance>=w:
        balance=balance-w
        lt=-w
        myfile.write('                                          {}'.format(lt))
        myfile.write('           {} \n'.format(balance))
        myfile.write('---------------------------------------------------------------------------- \n')
    else:
        print('Ops! Invalid Format.')

def statement():
    global balance
    global lt
    socket.send(str(balance).encode(encoding='utf_8',errors='strict'))
    socket.send(str(lt).encode(encoding='utf_8',errors='strict'))
    print('Your current balance is ',balance)
    print('Your last transaction was ',lt)
    return [balance,lt]

def tran(t):
    myfile.seek(0)
    for lines in myfile.readlines():
        socket.send(str(lines).encode(encoding='utf_8',errors='strict'))



#Creating timestamp
localtime = time.asctime( time.localtime(time.time()))
log=open("log.txt",'a+')
#Using list for database
username1 = ['hinguparth23', 'phingu']
password1 = ['parth', 'pooja']

#Starting Server
print("Starting the Server")
ss = socket.socket()

#Binding Server
ss.bind(("localhost",8091))

#logging
log.write('{}'.format(localtime))
log.write('{} \n'.format(': Starting and Binding the Server'))


ss.listen(5)
user=''
while user!='Invalid':
    print("Waiting for client")
    socket,add = ss.accept()

    #logging
    log.write('{}'.format(localtime))
    log.write('{} \n'.format(': Waiting for client'))

    print("Connected to ",add)

    #logging
    log.write('{}'.format(localtime))
    log.write('{}'.format(': Connected to the Server '))
    log.write('{} \n'.format(add))

    username = socket.recv(1024).decode()
    print("Client sent -> ",username)

    password = socket.recv(1024).decode()
    print("Client sent -> ",password)

    log.write('{}'.format(localtime))
    log.write('{} \n'.format(': Credentials recieved'))

    if username in username1 and password in password1:
        print('Valid')
        socket.send("Valid".encode(encoding='utf_8',errors='strict'))
    

        user = ""
        while user != "Invalid":
            socket.send(str(balance).encode(encoding='utf_8',errors='strict'))

            user=socket.recv(1024).decode()
            if user == "deposit":
                deposit_value=socket.recv(1024).decode()
                v=int(deposit_value)
                deposit(v)
                statement()
            else:
                if user == 'withdraw':
                    withdrawal_value=socket.recv(1024).decode()
                    w=int(withdrawal_value)
                    withdraw(w)
                    statement()
                else:
                    if user == 'last transaction':
                        last_transaction=socket.recv(1024).decode()
                        t=int(last_transaction)
                        tran(t)
    else:
        print('Invalid')
        socket.send("Invalid".encode(encoding='utf_8',errors='strict'))

        log.write('{}'.format(localtime))
        log.write('{} \n'.format(': Credentials Authenticated'))

    socket.close()
ss.close()
