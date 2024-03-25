import socket
import threading
import sys

def sendMsgs(s, peer_address):
    while True:
        msg = input("> ")
        s.sendto(msg.encode(), peer_address)
        if msg == "--exit":
            break

def receiveMsgs(s):
    while True:
        data, addr = s.recvfrom(4096)
        msg = data.decode()
        if msg == "--exit":
            print("Your peer has decided to exit, type --exit to exit")
            break
        print("Received message:", msg, "\n> ", end='')

def communicate():
    myport = int(input("Enter your port number: "))

    while True:
        peer = input("Which peer do you want to talk to? ")
        peerport = int(input("Enter your peer's port number: "))

        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.bind(('0.0.0.0', myport))

        peer_address = (peer, peerport)

        send = threading.Thread(target=sendMsgs, args=(s, peer_address), daemon=True)
        receive = threading.Thread(target=receiveMsgs, args=(s,), daemon=True)

        send.start()
        receive.start()

        send.join()
        receive.join()

        s.close()

        cont = input("Do you want to message another peer? ").lower()
        if cont == "no":
            break

    sys.exit()

if __name__ == "__main__":
    communicate()
    print("Type '--exit' to stop messaging\n")