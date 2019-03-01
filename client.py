import socket
import random

# using loop back address and port 5000
host = "144.96.33.160"
port = 80

# initializing socket object
s = socket.socket()

# binding loop back address and port to socket
s.connect((host, port))

# generating random number, casting it to string (int cant be decoded, only string can)
message = str(random.randint(1, 10000))

while message != 'n':
    # sending encoded number to server
    print("sending number to server: ", message)
    s.send(message.encode('utf-8'))

    # receiving acknowledgement
    data = s.recv(1024).decode('utf-8')
    print("Received from server: '", data, "' ")

    # Prompting user if they would like to send another number
    decision = input("Would you like to send another number? (y/n): ")
    if decision == 'y':
        # send number
        message = str(random.randint(1, 10000))
        print("")
    else:
        message = "n"

# terminate connection
s.close()


