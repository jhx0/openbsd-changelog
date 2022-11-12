#!/usr/bin/env python3

import urllib.request
from bs4 import BeautifulSoup as bs

URL = 'https://www.openbsd.org/plus.html'
RED = '\033[32m'
RESET = '\033[0m'

def parseHTML(url):
    return bs(urllib.request.urlopen(url), 'lxml')

def printList():
    counter = 0

    data = parseHTML(URL)

    for element in data.findAll("li"):
        counter += 1
        print("{}{}{}:\t{}".format(RED, counter, RESET, element.getText().rstrip()))

    if not counter:
        print("Changelog empty right now.")
    else:
        print("\nEntries: {}".format(counter))

if __name__ == "__main__":
    printList()
