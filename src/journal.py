from tcp_server import *
from addresses_global import JOURNAL_IP_PORT
import json

JOURNAL = []

def main():
    server = TCP_server()
    server.bind(JOURNAL_IP_PORT[1])
    server.listen()
    while True:
        client = ClientSocket(server.accept())
        request = json.loads(client.recv())
        JOURNAL.append({
            "input" : request["input"], 
            "cmp_string_id" : request["cmp_string_id"],
            "method_id" : request["method_id"],
            "result" : request["result"]})
        client._socket.close()
        print(JOURNAL)

if __name__ == "__main__":
    main()