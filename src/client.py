import socket, json
from tcp_client import Tcp_client
from addresses_global import SCHEDULER_IP_PORT

def get_compute_unit_addr():
    compute_addr = None
    try:
        client_socket = Tcp_client()
        client_socket.connect(SCHEDULER_IP_PORT)
        
        client_socket.send("{ \"method\" : 0 }")
        compute_addr = client_socket.receive()
        client_socket.close()
    except OSError:
        print("connection with sheduler goes wrong")
        return
    json_compute_addr = json.loads(compute_addr)
    return tuple([json_compute_addr['host'], json_compute_addr['port']])


def main():
    compute_addr = get_compute_unit_addr()
    client_socket = Tcp_client()
    client_socket.connect(compute_addr)

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