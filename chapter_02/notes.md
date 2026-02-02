# Chapter 2: Basic Networking Tools

- Hackers can do a lot with basic network access.
    - But when deep in a target's infrastructure,
        - they might not find any of the necessary network tools.
            - but they might find a Python install.
- We'll be covering the `socket` module.
    - And we'll build:
        - clients
        - servers
        - a TCP proxy
        - our own *netcat*, complete with a command shell

## Python Networking in a Paragraph
- `socket` module
    - > This module exposes all of the necessary pieces to
        - quickly  write TCP/UDP clients and severs
        - use raw sockets
        - etc.

## TCP Client
[[tcp_client.py](tcp_client.py)]
- AF_INET indicates it uses IPv4.
- SOCK_STREAM indicates it uses TCP.

## UDP Client
[[udp_client.py](udp_client.py)]
- Very similar to a TCP client, only 2 changes:
    - uses SOCK_DGRAM, instead of SOCK_STREAM
    - no .connect(); UDP is connectionless

## TCP Server
[[tcp_server.py](tcp_server.py)]