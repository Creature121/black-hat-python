# Github Command and Control
- > In this chapter, we’ll create a trojan framework...
  - > ...we’ll be able to assign it all sorts of nefarious tasks.

## Setting up a GitHub Account
- Created private repo ["bhptrojan"](https://github.com/Creature121/bhptrojan).
- `config` holds unique configuration files for each trojan.
  - > We’ll implement a special import hack to allow our trojan to import libraries directly from our GitHub repo.
- `modules` contains any modular code that the trojan should pick up and execute.
- `data` will be the spot where trojans will upload collected data.

## Creating modules
[[dirlister.py](dirlister.py), [environment.py](environment.py)]

## Configuring the Trojan
[[abs.json](abs.json)]
- We can tell what are trojan should do through configuration files.

## Building a Github-Aware Trojan
[[git_trojan.py](git_trojan.py)]

## Hacking Python's `import` Functionality
[[git_trojan.py](git_trojan.py)]
- Basically, we make Python retrieve packages (that we want) that it doesn't find locally from our remote repo.
