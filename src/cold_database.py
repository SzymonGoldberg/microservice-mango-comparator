from tcp_server import ClientSocket, TCP_server
from addresses_global import COLD_DATASET_IP_PORT
import json, pymongo

DATABASE = ["hello", "have a nice day", "nevermind"]

mymongo = pymongo.MongoClient("mongodb://localhost:27017")
database = mymongo["cold_database"]
COLLECTION = database["collection"]


def main():
    server = TCP_server()
    server.bind(COLD_DATASET_IP_PORT[1])
    server.listen()
    while True:
        client = ClientSocket(server.accept())
        request = json.loads(client.recv())
        query = {"_id": request["string_id"]}
        string_to_send = COLLECTION.find_one(query)["string"]
        client.send(json.dumps({"string": string_to_send}).encode())
        client.close()


if __name__ == "__main__":
    main()
