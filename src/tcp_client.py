import socket


class Tcp_client:
    def __init__(self) -> None:
        self._socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def connect(self, ip_port: tuple) -> None:
        self._socket.connect(ip_port)

    def send(self, string: str) -> int:
        return self._socket.send(bytes(string, "utf-8"))

    def receive(self) -> str:
        return self._socket.recv(2048).decode("utf-8")

    def close(self) -> None:
        self._socket.close()
