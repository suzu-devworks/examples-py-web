import os
import socket

UDP_IP = "0.0.0.0"


def main() -> None:
    UDP_PORT = int(os.environ["UDPPORT"])
    print(f"Listening on UDP port {UDP_PORT}")

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # Internet  # UDP
    sock.bind((UDP_IP, UDP_PORT))

    while True:
        data, addr = sock.recvfrom(1024)  # buffer size is 1024 bytes
        print(addr, ":", data)


if __name__ == "__main__":
    main()
