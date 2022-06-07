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


try:
    client = Tcp_client()
    
    client.connect((socket.gethostname(), int(input("choose a port > "))))
    while True:
        userMsg = input("enter message to send > ")
        if userMsg == "":
            break
        sent = client.send(userMsg)
        print("amount of sent bytes: ", sent)
        if sent == 0:
            raise ConnectionRefusedError
        received = client.receive()
        print(received)
        if len(received) == 0:
            break

except ConnectionRefusedError:
    print("cannot connect to server")
except ConnectionResetError:
    print("server is not open")
finally:
    print("server disconnected")
    client.close()
