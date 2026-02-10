# Extending Burp Proxy
- > Burp Suite also allows you to create your own tooling, called extensions.
    - > We’ll take advantage of this feature to write some handy tooling for performing attacks and extended reconnaissance.
- Extensions that we will build:
    1. this one will intercept HTTP requests from Burp proxy, and use it as a seed for a "mutation fuzzer" in Burp Intruder.
    2. this one will interact with Microsoft Bing API to:
        - show all virtual hosts located on the same IP as the target site
        - any subdomains for the target domain
    3. this one will create a wordlist from a target site, to be used in a brute-force password attack.
- We have to install a few things:
    - Burpsuite
    - Jython
        - I downloaded it from [this site](https://www.jython.org/download), as given in the book.
            - The version I got was `2.7.4`.

## Burp Fuzzing
[[bhp_fuzzer.py](bhp_fuzzer.py)]
- `IIntruderPayloadGeneratorFactory`
    - `registerExtenderCallbacks()`
    - `getGeneratorName()`
    - `createNewInstance()`
- `IIntruderPayloadGenerator`
    - `hasMorePayloads()`
    - `getNextPayload()`
    - `reset()`
    - and then our custom fuzzer: `mutate_payload()`

## Use Bing for Burp
 