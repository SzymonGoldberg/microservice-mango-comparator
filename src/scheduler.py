from numpy import save
from tcp_client import Tcp_client
from tcp_server import TCP_server, ClientSocket
from addresses_global import COLD_DATASET_IP_PORT, JOURNAL_IP_PORT
import socket, json, difflib

def get_data_from_cold(string_id):
    cold_dataset_connection = Tcp_client()
    cold_dataset_connection.connect(COLD_DATASET_IP_PORT)
    cold_dataset_connection.send(json.dumps({"string_id" : string_id}))
    result = json.loads(cold_dataset_connection.receive())["string"]
    cold_dataset_connection.close()
    return result

def save_to_journal(input_string, cmp_string_id, method_id, result):
    try:
        journal_connection = Tcp_client()
        journal_connection.connect(JOURNAL_IP_PORT)
        journal_connection.send(json.dumps(
            {"input" : input_string,
            "cmp_string_id" : cmp_string_id,
            "method_id" : method_id,
            "result" : result}))
    except OSError:
        print("journal is not working now")
    finally:
        journal_connection.close()

def compute_unit(port):
    try:
        print("new compute unit opened")
        server = TCP_server()
        server.bind(port)
        server.listen()
        client = ClientSocket(server.accept())
        print("client connected")
        request = json.loads(client.recv())
        print(request)
        cmp_string = get_data_from_cold(request["cmp"])
        result = difflib.SequenceMatcher(None, request["string"], cmp_string).ratio()
        client.send(json.dumps({"result" : result}).encode())
        save_to_journal(request["string"], request["cmp"], 0, result)
    except OSError:
        print("compute unit is broken")
    finally:
        server.close()

def main():
    try:
        server = TCP_server()
        server.bind(8080)
        server.listen()
        client = ClientSocket(server.accept())
        compute_unit_port = 8800
        request = json.dumps({"host" : socket.gethostname(), "port" : compute_unit_port}).encode()
        client.send(request)
    except OSError:
        print("sheduler server is broken")
    finally:
        server.close()
    compute_unit(compute_unit_port)

if __name__ == "__main__":
    main()