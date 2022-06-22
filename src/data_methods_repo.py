import pymongo
from tcp_server import ClientSocket, TCP_server
from addresses_global import DATA_METHODS_REPO_IP_PORT
import json

METHODS = [
    "nice",
    "naive"
]

mymongo = pymongo.MongoClient("mongodb://localhost:27017")
database = mymongo["cold_database"]
COLLECTION = database["collection"]

def main():
    server = TCP_server()
    server.bind(DATA_METHODS_REPO_IP_PORT[1])
    server.listen()
    while True:
        client = ClientSocket(server.accept())
        request = json.loads(client.recv())
        if request["need"] == "METHOD":
            to_send = METHODS
        else:
            to_send = [x["string"] for x in COLLECTION.find()]
        client.send(json.dumps({"string" : to_send}).encode())
        client.close()

if __name__ == "__main__":
    main()