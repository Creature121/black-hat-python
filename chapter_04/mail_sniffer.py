from scapy.all import Packet, sniff


def packet_callback(packet: Packet):
    print(packet.show())


def main():
    sniff(prn=packet_callback, count=1)


if __name__ == "__main__":
    main()
