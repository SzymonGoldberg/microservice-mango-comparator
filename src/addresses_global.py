import socket

COLD_DATASET_IP_PORT = (socket.gethostname(), 9999)
JOURNAL_IP_PORT = (socket.gethostname(), 9191)
SCHEDULER_IP_PORT = (socket.gethostname(), 8080)