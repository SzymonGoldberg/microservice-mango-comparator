from tcp_server import ClientSocket, TCP_server
from addresses_global import COLD_DATASET_IP_PORT
import json

DATABASE = [
    "hello",
    "have a nice day",
    "nevermind"
]

def main():
    server = TCP_server()
    server.bind(COLD_DATASET_IP_PORT[1])
    server.listen()
    while True:
        client = ClientSocket(server.accept())
        request = json.loads(client.recv())
        client.send(json.dumps({"string" : DATABASE[request["string_id"]]}).encode())
        client.close()

if __name__ == "__main__":
    main()