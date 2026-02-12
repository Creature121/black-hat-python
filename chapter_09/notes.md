# Fun With Exfiltration
- > Depending on the defense mechanisms in place, this last part of your attack can prove to be tricky.
  - there may be local/remote systems that:
    - validate processes that open remote connections
    - whether those processes should be able to send information
      - or initiate connections outside the internal network
- First, we'll write a script to encrypt/decrypt data.
    - Then another script that encrypts data and transfers it using 3 methods:
      - email
      - file transfers
      - POSTs to a web server

## Encrypting and Decrypting Files
[[cryptor.py](cryptor.py)]
- We basically do hybrid encryption/decryption.
  - We genrate RSA 2048 bit private/public key and save it.
  - we create an AES (EAX mode) session key, and use that to encrypt/decrypt the data
  - encrypt the session key with public key, decrypt with private key
  - combine encrypted session key, nonce, digest tag, and ciphertext in one package, and send it over
    - this payload is what we encrypt/decrypt.
  - We also have zlib.compression()/decompression() to reduce the size of the plaintext before/after encryption/decryption.

## Email Exfiltration
[[email_exfil.py](email_exfil.py)]

## File Transfer Exfiltration
[[transmit_exfil.py](transmit_exfil.py)]

## Exfiltration via a Web Server
[[paste_exfil.py](paste_exfil.py)]
- Internet Explorer COM automation
  - `Iexplore.exe` process is typically trusted and whitelisted.

## Putting it All Together
[[exfil.py](exfil.py)]
