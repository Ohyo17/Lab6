import socket
import sys
import time
import math
import errno
from multiprocessing import Process


def calcLog(x):
    print("Calculate Log:",x )
    print(x)
    x = int(x)
    try:
            answer = math.log(x)
    except:
            answer = "Please enter the right value"
    print(answer)
    return answer

def calcSqrt(x):
    print("Calculate Square root",x)
    x = int(x)
    if(x >= 0):
              try:
                   answer = math.sqrt(x)
              except:
                   answer = "Please enter the right value"
    else:
        answer = "Please enter the right value"
    print(answer)
    return answer

def calcExpo(x):
    print("Calculate Exponential",x)
    x = float(x)
    try:
            answer = math.exp(x)
    except:
            answer = "Please enter the right value"
    print(answer)
    return answer

def process_start(s_sock):
    s_sock.send(str.encode('Welcome to the Server for Online Calculator \n'))
    

    while True:
        data = s_sock.recv(2048)

        data = data.decode('utf-8')

        try:
            function, value = data.split(" ",2)
        except:
             print("Data can't received")

        if not data:
            break

        if(function == 'Log'):
                      answer = calcLog(value)
        elif(function == 'Sqrt'):
                      answer = calcSqrt(value)
        elif(function == 'Expo'):
                      answer = calcExpo(value)
        elif(function == 'Exit'):
                      break
        result = "The answer is %s" % str(answer)
        s_sock.sendall(str.encode(result))
    s_sock.close()


if __name__ == '__main__':
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(("",8888))
    print("listening...")
    s.listen(3)
    try:
        while True:
            try:
                s_sock, s_addr = s.accept()
                p = Process(target=process_start, args=(s_sock,))
                p.start()

            except socket.error:

                print('got a socket error')

    except Exception as e:        
                print('an exception occurred!')
                print(e)
                sys.exit(1)
    finally:
     	   s.close()
