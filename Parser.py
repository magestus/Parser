# -*- coding: utf-8 -*-
import urllib.request
from bs4 import BeautifulSoup


def get_html(url):
    response = urllib.request.urlopen(url)
    return response.read()

def parse(html):
    soup = BeautifulSoup(html, 'html.parser')
    table = soup.find('div', {"class": "Search-wrapper"})
    
    cases = []

    for row in table.find_all('div', {'Search-item-1'}):
        cols = row.find_all('div', {'Search-item-option'})    
        print(cols)
        
        


def main():
    parse(get_html('https://fabrikant.ru/trades/procedure/search/?type=1&query=&procedure_stage=2&price_from=&price_to=&currency=0&date_type=date_publication&date_from=&date_to=&ensure=all&section_type%5B%5D=ds300&count_on_page=10&order_by=default&order_direction=1'))

if __name__ == "__main__":
    main()