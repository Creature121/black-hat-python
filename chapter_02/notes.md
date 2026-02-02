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

## Replacing Netcat
[[netcat.py](netcat.py)]
- > Netcat is the utility knife of networking...
    - > With it, you can read and write data across the network, meaning you can use it to execute remote commands, pass files back and forth, or even open a remote shell.
- `subprocess` library
    - > ...provides a powerfulprocess-creation interface that gives you a number of ways to interact with client programs.
    - check_ouput()
        - > ...runs a command on the local operating system and then returns the output from that command.
- `argparse` module
    - helps in creating a cmd interface.
    - `epilog` contains the text that will be shown when the user uses `--help`.
- > Remember that the script reads from stdin and will do so until it receives the end-of-file (EOF) marker. To send EOF, press CTRL-D on your keyboard:...
    - For Windows, you send EOF by triggering `CTRL-Z`+`Enter`.