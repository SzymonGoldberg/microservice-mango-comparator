import json
from tcp_client import Tcp_client
from addresses_global import SCHEDULER_IP_PORT
from time import sleep
from advance_client import get_compute_unit_addr


def main():
    compute_addr = get_compute_unit_addr(0)
    client_socket = Tcp_client()
    sleep(0.1)
    client_socket.connect(compute_addr)

    try:
        client_socket.send(
            '{ "string":"' + input("insert you string to compare -> ") + '", "cmp": 0}'
        )
        result = client_socket.receive()
        client_socket.close()
    except OSError:
        print("problem with sending/receiving from computing unit occured")
        return
    print("result = ", json.loads(result)["result"])


if __name__ == "__main__":
    main()
