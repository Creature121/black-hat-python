# Common Trojanning Tasks on Windows
- Trojan common tasks:
  - grab keystrokes
  - take screenshots
  - execute shellcode
    - > to provide an interactive session to tools like CANVAS or Metasploit.
- > We’ll wrap things up with some sandbox detection techniques to determine if we are running within an antivirus or forensics sandbox.

## Keylogging for Fun and Keystrokes
[[keylogger.py](keylogger.py)]
- `PyWinHook` library
  - allows us to trap all keyboard events
  - takes care of all the low-level programming; we can just focus on the core logic

## Taking Screenshots
[[screenshotter.py](screenshotter.py)]
- Using `pywin32` library to use the Windows API to grab screenshots.
- > (Learn more about device contexts and GDI programming on the Microsoft Developer Network [MSDN] at https://msdn.microsoft.com.)

## Python Shellcode Execution
[[shell_exec.py](shell_exec.py)]

## Sandbox Detection
[[sandbox_detect.py](sandbox_detect.py)]
- check if running in a sandbox:
  - monitor recent user input
  - look for keystrokes, mouse clicks, double-clicks
    - > A typical machine has many user interactions on a day in which it has been booted, whereas a sandbox environment usually has no user interaction...
  - detect if sandbox operator is sending fast, suspicious, repeated input
  - check the time between last user interaction and machine running time
