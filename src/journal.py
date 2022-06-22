from tcp_server import *
from addresses_global import JOURNAL_IP_PORT
import json
import pymongo

JOURNAL = []

mymongo = pymongo.MongoClient("mongodb://localhost:27017")
database = mymongo["cold_database"]
COLLECTION = database["archive"]


def filter_data(data):
    if data["result"] < 0.1:
        print("result too low - data rejected")
        return False
    return True


def main():
    server = TCP_server()
    server.bind(JOURNAL_IP_PORT[1])
    server.listen()
    while True:
        client = ClientSocket(server.accept())
        request = json.loads(client.recv())
        JOURNAL.append(
            {
                "input": request["input"],
                "cmp_string_id": request["cmp_string_id"],
                "method_id": request["method_id"],
                "result": request["result"],
            }
        )
        if filter_data(JOURNAL[-1]):
            COLLECTION.insert_one(JOURNAL[-1])

        client._socket.close()
        print(JOURNAL[-1])


if __name__ == "__main__":
    main()
