# Chapter 1: Setting Up Your Python Environment
The gist of this chapter is:
1. Installing and running a Kali VM.
2. Setting up Python 3.
3. And then installing an IDE.

## Experience
1. Finding a viruatlization hypervisor that was easy to setup and performant on my system took a long time.
    - I tried [Oracle VirtualBox](https://www.virtualbox.org/).
        - VMs were too slow, and required me to turn off the virtualization-based security measures my Windows system used to get more performance.
        - But it had the feature I wanted the most (among others): snapshots
    - Then I tried the Windows build of [QEMU](https://www.qemu.org/).
        - Cmd only, very verbose and low level, but I was willing to learn upto a certain extent.
            - But it got too complicated too quickly, and I couldn't spend too much time learning all the commands and necessary flags...
        - Moreover, performance was lackluster as well.
    - Finally found out about [VMWare Workstation Pro](https://www.vmware.com/products/desktop-hypervisor/workstation-and-fusion)
        - I found out that it allowed me to use the Pro version free for personal use, so I tried it.
            Everything is working well, and it is extremely performant compared to everything I have tried until now, so was able to successfully complete this step.
2. Setting up Python 3.
    - This was surprisingly tedious.
    - I thought I could just use my [uv package manager](https://github.com/astral-sh/uv), all from project handling to python version download and management.
        - [But it only supports downloading versions until Python 3.8 at minimum.](https://github.com/astral-sh/uv/issues/10454)
        - And I needed Python 3.7.5 for the book.
    - So then I went ahead and search for ways to get Python 3.7.5 on my Kali.
        - Tried downloading the source and compiling it myself.
            - Took too long when I enabled opimisations, more than 1hr, and barely any progress.
                - So I compiled it without optimisations, and it built, but it didn't build some sort of `ctypes` module.
                    - and unfrotunately there was this line in the book:
                        - > ...and a comparison of the *ctypes* and *struct* libraries.
                    - so then this was not acceptable either.
        - Tried to get some sort of PPA to download from
            - In short, the PPA and tools I used failed.
        - After a long time, I found out about [Astral's Standalone Python Builds](https://github.com/astral-sh/python-build-standalone).
            - And it had [a build of Python 3.7.5](https://github.com/astral-sh/python-build-standalone/releases/tag/20191025)
            - So I downloaded, tested it (it works I believe), placed it in my bin folder, and added it to my PATH.
    - For Windows, use the [Python Install Manager](https://www.python.org/downloads/release/pymanager-252/), honestly the easiest way...
3. Then I installed VSCode.
    - This was the only easy step.
    - [Downloaded it from the site](https://code.visualstudio.com/download), installed it, ran it.
    - I also initialised a Python project using uv with its required Python version as 3.7.5 (uv was able to discover it from my path and use it).
    - Installed my required extensions, and now I am good to go.