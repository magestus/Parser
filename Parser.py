# -*- coding: utf-8 -*-
import urllib.request
from bs4 import BeautifulSoup


def get_html(url):
    response = urllib.request.urlopen(url)
    return str(response.read())

def parse(html):
    soup = BeautifulSoup(html, 'html.parser')
    table = soup.find('div', {"class": "Search-list"})
    print(table)

def main():
    parse(get_html('https://www.fabrikant.ru/trades/procedure/search/'))

if __name__ == "__main__":
    main()