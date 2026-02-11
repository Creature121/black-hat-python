# Common Trojanning Tasks on Windows
- Trojan common tasks:
  - grab keystrokes
  - take screenshots
  - execute shellcode
    - > to provide an interactive session to tools like CANVAS or Metasploit.
- > We’ll wrap things up with some sandbox detection techniques to determine if we are running within an antivirus or forensics sandbox.

## Keylogging for Fun and Keystrokes
- `PyWinHook` library
  - allows us to trap all keyboard events
  - takes care of all the low-level programming; we can just focus on the core logic
