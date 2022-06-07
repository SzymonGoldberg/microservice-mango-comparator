from src.commons.tcp_server import TCP_server, ClientSocket
import socket

def main():
    server = TCP_server()
    server.bind(8080)
    server.listen()
    client = ClientSocket(server.accept())
    client.send(tuple([socket.gethostname(), 8800]))
    client.close()

if __name__ == "__main__":
    main()