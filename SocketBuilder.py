import socket


class SocketObj:
    def __init__(self, host, port, socket_type):
        self.sock = socket.socket()
        self.host = host
        self.port = port
        if socket_type == 'server':
            self.sock.bind((self.host, self.port))
        elif socket_type == 'client':
            pass

    def client_connection(self):
        self.is_not_used()

    def server_connection(self):
        self.is_not_used()

    def is_not_used(self):
        pass



