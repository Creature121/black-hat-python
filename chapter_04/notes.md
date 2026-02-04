# Chapter 4: Owning the Network with `scapy`

## Stealing Email Credentials
[[mail_sniffer.py](mail_sniffer.py), [mail_sniffer_bpf.py](mail_sniffer_bpf.py)]
- > We’ll build a very simple sniffer to capture Simple Mail Transport Protocol (SMTP), Post Office Protocol (POP3), and Internet Message Access Protocol (IMAP) credentials.
- Berkeley Packet Filter (BPF) Filter
    - made up of 3 parts:
        - a descriptor, what you are looking for (host, interface, port)
        - direction of traffic flow
        - the protocol