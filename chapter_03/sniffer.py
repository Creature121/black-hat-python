import socket
import os

HOST = "192.168.216.128"


def main():
    if os.name == "nt":
        socket_protocol = socket.IPPROTO_IP  # Windows allows us to sniff all protocols
    else:
        socket_protocol = (
            socket.IPPROTO_ICMP
        )  # Linux needs us to specify which protocol to sniff

    sniffer = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket_protocol)
    sniffer.bind((HOST, 0))

    sniffer.setsockopt(
        socket.IPPROTO_IP, socket.IP_HDRINCL, 1
    )  # Include IP Headers in the captured packets

    if os.name == "nt":
        sniffer.ioctl(socket.SIO_RCVALL, socket.RCVALL_ON)

    print(sniffer.recvfrom(65565))

    if os.name == "nt":
        sniffer.ioctl(socket.SIO_RCVALL, socket.RCVALL_OFF)


if __name__ == "__main__":
    main()
