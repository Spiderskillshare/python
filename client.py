import socket

def Main():
    host = '127.0.0.1'
    port = 5000

    s = socket.socket()
    s.connect((host, port))

    message = input("enter to send >> ")
    while message != 'q':
        s.send(message.encode('utf-8'))
        see = open("see.txt", "w")

        see.write(str(message.encode('utf-8')))
        see.close()
        data = s.recv(1024).decode('utf-8')
        print("you got a message: " + data)
        message = input("-->>")
    s.close()
if __name__ == '__main__':
    Main()
