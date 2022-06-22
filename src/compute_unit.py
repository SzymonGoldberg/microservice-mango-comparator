import sys
from tcp_server import TCP_server, ClientSocket
from tcp_client import Tcp_client
from addresses_global import COLD_DATASET_IP_PORT, JOURNAL_IP_PORT
import json, difflib


nice = lambda str1, str2: difflib.SequenceMatcher(None, str1, str2).ratio()
naive = lambda str1, str2: sum(n1 == n2 for n1, n2 in zip(str1, str2))

METHODS = [nice, naive]


def save_to_journal(input_string, cmp_string_id, method_id, result):
    try:
        journal_connection = Tcp_client()
        journal_connection.connect(JOURNAL_IP_PORT)
        journal_connection.send(
            json.dumps(
                {
                    "input": input_string,
                    "cmp_string_id": cmp_string_id,
                    "method_id": method_id,
                    "result": result,
                }
            )
        )
    except OSError:
        print("journal is not working now")
    finally:
        journal_connection.close()


def get_data_from_cold(string_id):
    cold_dataset_connection = Tcp_client()
    cold_dataset_connection.connect(COLD_DATASET_IP_PORT)
    cold_dataset_connection.send(json.dumps({"string_id": string_id}))
    result = json.loads(cold_dataset_connection.receive())["string"]
    cold_dataset_connection.close()
    return result


def main(port, method):
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
        result = METHODS[method](request["string"], cmp_string)
        client.send(json.dumps({"result": result}).encode())
        save_to_journal(request["string"], request["cmp"], 0, result)
    except OSError:
        print("compute unit is broken")
    finally:
        server.close()


if __name__ == "__main__":
    main(int(sys.argv[1]), int(sys.argv[2]))
