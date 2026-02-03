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

## Building a TCP Proxy
[[proxy.py](proxy.py)]
- Building a TCP Proxy will be useful when you are in environments where you cannot load tools like Wireshark, or anything that requires loading drivers to sniff loopback.
- The proxy has 4 main functions:
    - `hexdump()`: display communication to the console
    - `receive_from()`: receive data from an incoming socket
    - `proxy_handler()`: manage traffic
    - `server_loop()`: setup a listening socker and pass it to `proxy_handler()`
- `[(len(repr(chr(i))) == 3) and chr(i) or "." for i in range(256)]`
    - This works based on 2 rules of how Python works:
        1. Boolean expressions return one of their operands rather than a boolean value.
        2. Python lazily evaluates if-expressions.

## SSH with Paramiko
[[ssh_cmd.py](ssh_cmd.py), [ssh_rcmd.py](ssh_rcmd.py), [ssh_server.py](ssh_server.py)]
- > In Python, you could use raw sockets and some crypto magic to create your own SSH client or server
    - > but why create when you can reuse?
        - > Paramiko, which uses PyCrypto, gives you simple access to the SSH2 protocol.
- > We’ll use some of the demo files later, so make sure you download them from the Paramiko GitHub repo as well...
    - So I have downloaded [them](chapter_02/demos).
- Need to study `paramiko` module more deeply.

## SSH Tunneling
[[rforward.py](demos/rforward.py)]
- Basically, rather than tunneling in plaintext, we use SSH to tunnel.
    - `paramiko` makes this easy.
- We gain access to system A, but we want system B.
    - We can't directly access B, but A can. But A doesn't have the tools we need.
        - So we do a reverse SSH connection to our box, and tunnel our commands to B through A.
            - We basically forward a local port to the remote port of A, in order to access B.
            - [rforward.py](demos/rforward.py), from what we donwloaded earlier, implements this well, so there is nothing to code here.