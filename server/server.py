from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread
import time
from person import Person

def wait_for_connection():
    run = True
    while run:
        client, addr = SERVER.accept()

# GLOBAL CONSTANTS
HOST = 'localhost'
PORT = 5500
ADDR = (HOST, PORT)
MAX_CONNETIONS = 10
BUFSIZ = 512

# GLOBAL VARIABLES
persons = []
SERVER = socket(AF_INET, SOCK_STREAM)
SERVER.bind(ADDR)  # set up server

if __name__ == "__main__":
    SERVER.listen(MAX_CONNETIONS)  # open server to listen for connections
    print("[STARTED] Waiting for connections...")
    ACCEPT_THREAD = Thread(target=wait_for_connection)
    ACCEPT_THREAD.start()
    ACCEPT_THREAD.join()
    SERVER.close()