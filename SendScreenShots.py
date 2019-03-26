class SendScreenShotObj:
    def __init__(self, client_conn, SS):
        self.client_conn = client_conn
        self.SS = SS
        pass

    def send(self):
        self.is_not_used()
        while 'recording':
            pixels = self.SS.takescreenshot()

            pixel_length = len(pixels)
            size_len = (pixel_length.bit_length() + 7) // 8

            # Send the size of the pixels length
            try:
                self.client_conn.send(bytes([size_len]))
            except ConnectionResetError:
                print("Connection Terminated")
                break

            # Send the actual pixels length
            size_bytes = pixel_length.to_bytes(size_len, 'big')
            try:
                self.client_conn.send(size_bytes)
            except ConnectionResetError:
                print("connection Terminated")

            # Send pixels
            try:
                self.client_conn.sendall(pixels)
            except ConnectionResetError:
                print("connection Terminated")
                break

    def is_not_used(self):
        pass



