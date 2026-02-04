import ipaddress
import os
import socket
import struct
import sys
import threading
import time

SUBNET = "192.168.5.0/24"
MESSAGE = "PYTHONRULES!"


class IP:
    def __init__(self, buffer=None):
        header = struct.unpack("<BBHHHBBH4s4s", buffer)

        self.ver = header[0] >> 4
        self.ihl = header[0] & 0xF

        self.tos = header[1]
        self.len = header[2]
        self.id = header[3]
        self.offset = header[4]
        self.ttl = header[5]
        self.protocol_num = header[6]
        self.sum = header[7]
        self.src = header[8]
        self.dst = header[9]

        self.src_address = ipaddress.ip_address(self.src)
        self.dst_address = ipaddress.ip_address(self.dst)

        self.protocol_map = {1: "ICMP", 6: "TCP", 17: "UDP"}
        try:
            self.protocol = self.protocol_map[self.protocol_num]
        except Exception as _e:
            print(f"No protocol for {self.protocol_num}")
            self.protocol = str(self.protocol_num)


class ICMP:
    def __init__(self, buffer):
        header = struct.unpack("<BBHHH", buffer)

        self.type = header[0]
        self.code = header[1]
        self.sum = header[2]
        self.id = header[3]
        self.seq = header[4]


def udp_sender():
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sender:
        for ip in ipaddress.ip_network(SUBNET).hosts():
            # print(f"Sending to host: {str(ip)}")
            sender.sendto(bytes(MESSAGE, "utf-8"), (str(ip), 65212))
        # print("Done!")


class Scanner:
    def __init__(self, host):
        self.host = host
        if os.name == "nt":
            socket_protocol = socket.IPPROTO_IP
        else:
            socket_protocol = socket.IPPROTO_ICMP

        self.socket = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket_protocol)
        self.socket.bind((host, 0))
        self.socket.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)

        if os.name == "nt":
            self.socket.ioctl(socket.SIO_RCVALL, socket.RCVALL_ON)

    def sniff(self):
        hosts_up = set([f"{str(self.host)}"])
        try:
            while True:
                raw_buffer = self.socket.recvfrom(65535)[0]
                ip_header = IP(raw_buffer[0:20])
                if ip_header.protocol == "ICMP":
                    # print("Found ICMP!")
                    offset = ip_header.ihl * 4
                    buffer = raw_buffer[offset : offset + 8]
                    icmp_header = ICMP(buffer)
                    if icmp_header.type == 3 and icmp_header.code == 3:
                        # print("Found type 3, code 3!")
                        if ipaddress.ip_address(
                            ip_header.src_address
                        ) in ipaddress.IPv4Network(SUBNET):
                            # print("In Subnet!")
                            if raw_buffer[len(raw_buffer) - len(MESSAGE) :] == bytes(
                                MESSAGE, "utf-8"
                            ):
                                # print("Has Message!")
                                target = str(ip_header.src_address)
                                # print(f"Target: {target}")
                                if target != self.host and target not in hosts_up:
                                    hosts_up.add(str(ip_header.src_address))
                                    print(f"Host Up: {target}")
        except KeyboardInterrupt:
            if os.name == "nt":
                self.socket.ioctl(socket.SIO_RCVALL, socket.RCVALL_OFF)
            print("\nUser Interuppted.")
            if hosts_up:
                print(f"\n\nSummary: Hosts up on {SUBNET}")
                for host in sorted(hosts_up):
                    print(f"{host}")
            print("")
            sys.exit()


if __name__ == "__main__":
    if len(sys.argv) == 2:
        host = sys.argv[1]
    else:
        host = "192.168.5.129"
    scanner = Scanner(host)
    time.sleep(5)
    t = threading.Thread(target=udp_sender)
    t.start()
    scanner.sniff()
