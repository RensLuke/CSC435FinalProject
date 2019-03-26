from screenshot import ScreenShotObj
from SocketBuilder import SocketObj
from SendScreenShots import SendScreenShotObj
from threading import Thread


def main():
    new_socket = SocketObj('127.0.0.1', 5000, 'server')
    try:
        new_socket.sock.listen(5)
        print('Server started.')
        while 'connected':
            client_conn, client_addr = new_socket.sock.accept()
            print('Client connected IP:', client_addr)
            SS = ScreenShotObj()
            new_video_stream = SendScreenShotObj(client_conn, SS)
            thread = Thread(target=new_video_stream.send())
            thread.start()
    finally:
        sock.close()


if __name__ == '__main__':
    main()


