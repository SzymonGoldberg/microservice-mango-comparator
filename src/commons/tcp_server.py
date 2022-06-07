import socket

class ClientSocket:
    def __init__(self, socket_addr :tuple) -> None:
            self._socket, self._addr = socket_addr
        
    def send(self, message):
        return self._socket.send(message)

    def recv(self, message):
        return self._socket.recv(2048)

class TCP_server:
    def __init__(self) -> None:
        self._socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def bind(self, port) -> None:
        self._socket.bind((socket.gethostname(), port))

    def listen(self) -> None:
        self._socket.listen(5)

    def accept(self):
        return self._socket.accept()

    def close(self) -> None:
        self._socket.close()
