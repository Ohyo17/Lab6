import socket

ClientSocket = socket.socket()
host = '192.168.56.103'
port = 8888

print('Waiting for connection')
try:
    ClientSocket.connect((host, port))
except socket.error as e:
    print(str(e))

Response = ClientSocket.recv(1024)
print(Response)
print("----Welcome to online calculator for Square Root / Log / Exponential-----\n")
while True:

    function = input("Enter Sqrt / Log / Expo or (Exit to exit the program) : ")
    if(function == 'Log'):
               value = input("Please enter 1 value:")
    elif(function == 'Sqrt'):
               value = input("Please enter 1 value:")
    elif(function == 'Expo'):
               value = input("Please enter 1 value:")
    elif(function == 'Exit'):
               break

    message = function + " " + value
    ClientSocket.send(str.encode(message))
    Response = ClientSocket.recv(1024)
    print(Response.decode('utf-8'))

ClientSocket.close()
