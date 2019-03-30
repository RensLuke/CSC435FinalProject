from SocketBuilder import SocketObj
from threading import Thread


def establish_connection():
    new_socket = SocketObj('127.0.0.1', 5000, 'server')
    Thread(target=new_socket.server_connection()).start()


def main():
    establish_connection()


if __name__ == '__main__':
    main()


