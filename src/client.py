import socket, json
from tcp_client import Tcp_client


def main():
    try:
        client_socket = Tcp_client()
        client_socket.connect((socket.gethostname(), 8080))
        
        client_socket.send("{ \"method\" : 0 }")
        compute_addr = client_socket.receive()
        client_socket.close()
    except OSError:
        print("connection with sheduler goes wrong")
        return

    client_socket = Tcp_client()
    json_compute_addr = json.loads(compute_addr)
    client_socket.connect(tuple([json_compute_addr['host'], json_compute_addr['port']]))

    try:
        client_socket.send("{ \"string\":\"" + input("insert you string to compare -> ") 
            + "\", \"cmp\": 0}")
        result =  client_socket.receive()
        client_socket.close()
    except OSError:
        print("problem with sending/receiving from computing unit occured")
        return
    print("result = ", json.loads(result)["result"])

if __name__ == "__main__":
    main()