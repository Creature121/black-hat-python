import ipaddress
import struct


class IP:
    def __init__(self, buffer=None):
        header = struct.unpack("<BBHHHBBH4s4s", buffer)

        self.ver = header[0] >> 4  # Get high-order nibble by right-shift 4
        self.ihl = (
            header[0] & 0xF
        )  # Get low-order nibble by ANDing 0xF (i.e., 00001111)

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
