import socket

class Client:
    def communicate(self) -> None:
        print("connection from: ", self._addr)
        while True:
            recv = self._socket.recv(2048)
            if len(recv) == 0:
                break
            print("message: ", recv.decode("utf-8"), " size: ", len(recv))
            self._socket.send(recv)
        print("client with address: ", self._addr, " DISCONNECTED")

    def __init__(self, socket_addr: tuple) -> None:
        self._socket, self._addr = socket_addr


class TCP_server:
    def __init__(self) -> None:
        self._socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def bind(self, port: tuple) -> None:
        self._socket.bind((socket.gethostname(), port))

    def listen(self) -> None:
        self._socket.listen(5)

    def accept(self) -> None:
        ip_port = self._socket.accept()
        Client(ip_port).communicate()

    def close(self) -> None:
        self._socket.close()


try:
    server = TCP_server()
    server.bind(int(input("choose a port > ")))
    server.listen()
    while True:
        server.accept()
except OSError:
    print("address already in use")
finally:
    server.close()
