# Chapter 4: Owning the Network with `scapy`

## Stealing Email Credentials
[[mail_sniffer.py](mail_sniffer.py), [mail_sniffer_bpf.py](mail_sniffer_bpf.py)]
- > We’ll build a very simple sniffer to capture Simple Mail Transport Protocol (SMTP), Post Office Protocol (POP3), and Internet Message Access Protocol (IMAP) credentials.
- Berkeley Packet Filter (BPF) Filter
    - made up of 3 parts:
        - a descriptor, what you are looking for (host, interface, port)
        - direction of traffic flow
        - the protocol
- Installed [Sendmail](https://vmware.github.io/photon/assets/files/html/3.0/photon_admin/installing-sendmail.html) and tested it with [Swaks](https://jetmore.org/john/code/swaks/), and captured something with [mail_sniffer_bpf.py](mail_sniffer_bpf.py), although wasn't able to grab the plaintext...

## ARP Cache Poisoning with Scapy
[[arper.py](arper.py)]
- > ...we will convince a target machine that we have become its gateway, and we will also convince the gateway that in order to reach the target machine, all traffic has to go through us.
- Generated [arper.pcap](arper.pcap) here.

## pcap Processing
[[recapper.py](recapper.py), [detector.py](detector.py)]
- Downloaded [haarcascade_frontalface_alt.xml](training/haarcascade_frontalface_alt.xml) from [the link the author mentioned](http://eclecti.cc/files/2008/03/haarcascade_frontalface_alt.xml) 


