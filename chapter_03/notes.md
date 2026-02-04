# Chapter 3: Writing a Sniffer

- > Network sniffers allow you to see packets entering and exiting a target machine.
    - Sometimes we will be able to use Wireshark or `scapy`.
        - But we will be writing our own sniffer, and get a better understanding of how to interact with low-level networking.

## Building a UDP Host Discovery Tool
- > Our sniffer’s main goal is to discover hosts on a target network.
    - > We’ll use a known behavior of most operating systems to determine if there is an active host at a particular IP address.
        - If we send a UDP datagram to a closed port...
            - we usually get back an ICMP Unreachable message
                - indicating that the host is alive.
            - Othewise we will get nothing.
        - > ...we can probe several ports to ensure we aren’t hitting an active UDP service.
- Why UDP?
    - Makes sniffer simple
    - lightweight, almost no overhead in sending a bunch of them and waiting for responses.

## Packet Sniffing on Windows and Linux
[[sniffer.py](sniffer.py)]
- > The process of accessing raw sockets in Windows is slightly different than on its Linux brethren...
    - > Windows requires us to set some additional flags through a socket input/output control (IOCTL), which enables promiscuous mode on the network interface

## Decoding the IP Layer
- > Let’s work on decoding the IP portion of a packet so that we can pull useful information from it...
- We can either use `ctypes` or `struct` modules to define the data structure.
    - > The `ctypes` module is a foreign function library for Python.
        - > It provides a bridge to C-based languages,
            - > enabling you to use C-compatible data types and call functions in shared libraries.
    - > ...`struct` converts between Python values and C structs represented as Python byte objects.
    - > In other words, the `ctypes` module handles binary data types in addition to providing a lot of other functionality,
        - > while the struct module primarily handles binary data.

### The `ctypes` Module
[[IP_ctypes.py](IP_ctypes.py)]

### The `struct` Module
[[IP_struct.py](IP_struct.py)]
- "<BBHHHBBH4s4s"
    - '<' => endianness.
        - little endian => least significant byte is stored in the lower address
    - 'B' => 1 byte unsigned char
    - 'H' => 2 byte unsigned short
    = '4s' => 4 byte string

## Writing the IP Decoder
[[sniffer_ip_header_decode.py](sniffer_ip_header_decode.py)]

## Decoding ICMP
[[sniffer_with_icmp.py](sniffer_with_icmp.py), [scanner.py](scanner.py)]
- Type 3 => Destination Unreachable class
    - Code Value 3 => Port Unreachable
- `ipaddress` module
 