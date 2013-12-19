'''
Created on Sep 8, 2013

@author: matthassel
'''
'''
Currently: This app can return stock quote current price.

With this method, I am going to have to define a list of filters.
for example, to return the current price now, I have to 
filter for yfs_l84_"symbol".

The plus side to this project is the standard library modules.
'''

import urllib.request
from html.parser import HTMLParser
import re

def stock_url(symbol):
    baseurl = 'http://finance.yahoo.com/q?s='
    url = baseurl + symbol
    return url

def request_url(url):
    req = urllib.request.Request(url)
    req.add_header('User-agent', 'Mozilla/5.0')
    f = urllib.request.urlopen(url)
    html = str(f.read())
    return html

class MyParser(HTMLParser):
    def __init__(self):
        super(MyParser, self).__init__(strict = False)
        self.in_select = False
        self.htmldata = []

    def handle_starttag(self, tag, attrs):
        current_price_id = 'yfs_l84_' + symbol.lower()
        current_change_id = 'yfs_c63_' + symbol.lower()
        current_percent_change_id = 'yfs_p43_' + symbol.lower()
        if tag == "span":
            for x in attrs:
                print(x)
                if x[1] == current_price_id:
                    self.in_select = True
                if x[1] == current_change_id:
                    self.in_select = True
                if x[1] == current_percent_change_id:
                    self.in_select = True
        if tag == "td":
            for x in attrs:
                print(x)   
    def handle_endtag(self, tag):
        if tag == "span" and self.in_select:
            self.in_select = False
    def handle_data(self, data):
        if self.in_select:
            return self.htmldata.append(data.strip())
    

if __name__ == '__main__':
    #symbol = str(input("What stock symbol would you like to query? ").lower())
    symbol = 'MU'
    url = stock_url(symbol)
    print(url)
    html = request_url(url)
    print(html)
    parse = MyParser()
    parse.feed(html)
    print(parse.htmldata)