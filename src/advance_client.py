import json
from time import sleep
from tcp_client import Tcp_client
from addresses_global import SCHEDULER_IP_PORT, DATA_METHODS_REPO_IP_PORT

def get_compute_unit_addr(method_id):
    compute_addr = None
    try:
        client_socket = Tcp_client()
        client_socket.connect(SCHEDULER_IP_PORT)
        
        client_socket.send("{ \"method\" :" + str(method_id) +"}")
        compute_addr = client_socket.receive()
        client_socket.close()
    except OSError:
        print("connection with sheduler goes wrong")
        return
    json_compute_addr = json.loads(compute_addr)
    return tuple([json_compute_addr['host'], json_compute_addr['port']])


def get_from_data_methods_repo(what):
    info = what + "is not available"
    try:
        client_socket = Tcp_client()
        client_socket.connect(DATA_METHODS_REPO_IP_PORT)
        
        client_socket.send("{ \"need\" : \""+ what + "\" }")
        info = client_socket.receive()
        client_socket.close()
    except OSError:
        print("connection with data methods goes wrong")
        return
    return json.loads(info)
    
def main():
    print("available methods: ", get_from_data_methods_repo("METHOD")["string"])
    print("available strings: ", get_from_data_methods_repo("STRING"))
    
    to_cmp = input("choose string to compare(insert index from list above) ->")
    input_str = input("insert you string to compare -> ")
    compute_addr = get_compute_unit_addr(input("choose method ->"))
    client_socket = Tcp_client()
    sleep(1)
    client_socket.connect(compute_addr)

    try:
        client_socket.send("{ \"string\":\"" + input_str + "\", \"cmp\": "+ to_cmp +"}")
        result =  client_socket.receive()
        client_socket.close()
    except OSError:
        print("problem with sending/receiving from computing unit occured")
        return
    print("result = ", json.loads(result)["result"])

if __name__ == "__main__":
    main()