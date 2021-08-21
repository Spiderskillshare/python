#! /bin/python3
import socket

def Main():
    host = '127.0.0.1'
    port = 5000

    s = socket.socket()
    print(s)
    s.bind((host,port))

    s.listen(1)
    print(s.listen(1))
    
    a, addr = s.accept()
    print("connection reserved u wanna see >: " + str(addr))
    while True:
        #recv with byte
        print("while true")
 #       print("see unencripted :" + str(a.recv(1024))
        data = a.recv(1024).decode('utf-8')
        print("if true")
        if not data:
            print("no data")
            break

        print("from connected user decripted utf-8: " + data)

        data = data.upper()
        print("sending >> " + data)
        a.send(data.encode('utf-8'))
    a.close()


if __name__ == '__main__':
    Main()
