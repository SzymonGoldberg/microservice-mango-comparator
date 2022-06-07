import socket
from time import sleep
from commons.tcp_client import Tcp_client


def main():
    try:
        client_socket = Tcp_client()
        client_socket.connect((socket.gethostname(), 8080))
        
        client_socket.send("{ \"method\" : 0 }")
        port = client_socket.receive()
        client_socket.close()
    except OSError:
        print("connection with sheduler goes wrong")
        return

    client_socket = Tcp_client()
    for _ in range(10):
        try:
            client_socket.connect(port)
        except OSError:
            print("cannot connect to compute unit, retrying in 10 seconds")
            sleep(5)
    try:
        client_socket.send("{ \"string\":\"" + input("insert you string to compare") 
            + "\", \"compare string\": 0")
        result =  client_socket.receive()
        client_socket.close()
    except OSError:
        print("problem with sending/receiving from computing unit occured")
        return
    print("result = ",result)

if __name__ == "__main__":
    main()