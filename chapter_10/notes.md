# Windows Privilege Escalation
- Typical privilege escalation:
  - exploit a poorly-coded driver
  - exploit a nativer Windows kernel issue
  - but these methods risk system instability
- Other methods:
  - > System administrators in large enterprises commonly schedule tasks or services that
    - > execute child processes,
    - > or run VBScript or PowerShell scripts to automate activities.
  - >  Vendors, too, often have automated, built-in tasks that behave the same way.
- > We’ll try to take advantage of any high-privilege processes that handle files or execute binaries that are writable by low-privilege users.
- We will learn to use Windows Management Instrumentation (WMI) to monitor the creation of new processes.
  - We will grab info such as:
    - filepaths
    - the user that create that process
    - the privileges
- > Then we’ll hand off all filepaths to a file-monitoring script that continuously keeps track of any new files created, as well as what gets written to them.
  - > This tells us which files the high-privilege processes are accessing.
- Finally, we will then intercept the file-creation process
  - > by injecting our own scripting code into the file
    - > and make the high-privilege process execute a command shell.
      - This doesn't involve any API hooking, avoiding AV detection.

## Creating the Vulnerable Blackhat Service
[[bhservice.py](bhservice.py)]
- Downloaded from [bhservice_task.vbs](bhservice_task.vbs) from [this link](https://nostarch.com/download/BHPCode.zip).

## Creating a Process Monitor
- El Jefe
  - > ...a very simple process-monitoring system.

## Process Monitoring with WMI
[[process_monitor.py](process_monitor.py)]
- Here, we use WMI to:
  - monitor the system for certain events
    - and receive a callback when those event occur
- Using this interface, we will log:
  - process creation time
  - user who spawned the process
  - executable that was launched, and its cmd args
  - process ID
  - parent process ID

## Windows Token Privileges
[[process_monitor.py](process_monitor.py)]
- Windows tokens:
  - > “an object that describes the security context of a process or thread"
- Interesting Privileges:
  - SeBackupPrivilege
  - SeDebugPrivilege
  - SeLoadDriver

## Winning the Race
[[file_monitor.py](file_monitor.py)]

## Code Injection
