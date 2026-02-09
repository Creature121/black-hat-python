# Chapter 5: Web Hackery
- > In most modern networks, web applications present the largest attack surface and therefore are also the most common avenue for gaining access to the web applications themselves.
- 3 scenarios:
    - we know the open-source web framework that the target uses.
        - we will create a map of the directories in the web app, tarverse it locally, and use it to detect reall useful files and directories on the target
    - we only know the URL of the target.
        - we will try to fuzz out the site map.
    - we know the base URL, and the login page
        - we'll try to brute force a login

## Using Web Libraries
- We'll be trying to use the standard libraries.

### The `urllib2` Library for Python 2.x
### The `urllib` Library for Python 3.x
[[get_request.py](get_request.py), [post_request.py](post_request.py)]
### The `requests` Library
[[make_request.py](make_request.py)]
### The `lxml` and `BeautifulSoup` Packages
[[request_lxml.py](request_lxml.py), [request_bs4.py](request_bs4.py)]

## Mapping the WordPress Framework
[[mapper.py](mapper.py)]
- > Download and unzip a local copy of WordPress.
    - > Here, we’re using version 5.4 of WordPress.
        - which I have done so.
- "http://boodelyboo.com/" does not work anymore...

## Bruteforcing Directories and File Locations
- Spiders for crawling and discovering as much of the web app as possible.
- But we want to find any bit of info...
    - > ...that can provide sensitive information or expose functionality that the software developer did not intend.
- > For this example, we’ll use a list from SVNDigger.
    - Which I have [downloaded](chapter_05/all.txt).
        - Their link didn't work, I go it from this [github repo](https://github.com/nathanmyee/SVNDigger).
- "http://testphp.vulnweb.com" is a working site!