from SocketBuilder import SocketObj
from threading import Thread

WIDTH = 1920
HEIGHT = 1080


def main():
    new_socket = SocketObj('127.0.0.1', 5000, 'client')
    Thread(target=new_socket.client_connection(1920, 1080)).start()


if __name__ == '__main__':
    main()
