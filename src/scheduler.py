import random
from tcp_server import TCP_server, ClientSocket
from addresses_global import SCHEDULER_IP_PORT
import socket, json
import subprocess
from compute_unit import main as c

def main():
    try:
        server = TCP_server()
        server.bind(SCHEDULER_IP_PORT[1])
        server.listen()
        while True:
            client = ClientSocket(server.accept())
            request = json.loads(client.recv())
            compute_unit_port = random.randint(6000, 8000)
            method = request["method"]
            p = subprocess.Popen(f"python3 compute_unit.py {compute_unit_port} {method}", shell=True)
            print("new process = ", p.pid)
            request = json.dumps({"host" : socket.gethostname(), "port" : compute_unit_port}).encode()
            client.send(request)
            client.close()
    except OSError:
        print("sheduler server is broken")
    finally:
        server.close()

if __name__ == "__main__":
    main()