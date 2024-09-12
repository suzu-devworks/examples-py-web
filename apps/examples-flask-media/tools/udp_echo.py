import os
import socket


def main() -> None:
    UDP_IP = os.getenv("UDP_IP", "127.0.0.1")
    UDP_PORT = int(os.getenv("UDP_PORT", 5501))
    print(f"Listening on UDP {UDP_IP}:{UDP_PORT}")

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # Internet  # UDP
    sock.bind((UDP_IP, UDP_PORT))

    while True:
        data, addr = sock.recvfrom(1024)  # buffer size is 1024 bytes
        print(addr, ":", data)


if __name__ == "__main__":
    main()
