#!/usr/bin/python
'''
Created on Sep 8, 2013

@author: matthassel
'''

"""
DOES:
* Creates the URL for yahoo urllib.request.urlopen
* Uses Beautiful soup to help parse through the data fromt he page and return useful information
* displays the title, symbol, and current price.
* returns "up" or "down" depending on postive or negative price (to be used for LED color)

"""
# http://finance.yahoo.com/q?s=AMD
#import urllib
#from bs4 import BeautifulSoup

class Quote():
    
    def __init__(self, symbol):
        self.s = symbol
        self.baseurl = 'http://finance.yahoo.com/q?s='

    def stockurl(self):
        url = self.baseurl + self.s
        return url
    
    def requesturl(self, url):
        f = urllib.urlopen(url)
        html = f.read()
        return html
    
#    def beautifyhtml(self, html):
#        currentprice_id = 'yfs_l84_' + self.s.lower()
#        current_change_id = 'yfs_c63_' + self.s.lower()
#        current_percent_change_id = 'yfs_p43_' + self.s.lower()
#        find = []
#        find.append(currentprice_id)
#        find.append(current_change_id)
#        find.append(current_percent_change_id)
#        soup = BeautifulSoup(html)
#        # title of the sites - has stock quote
#        #title = soup.title.string
#        #print(title)
#        # p is where the guts of the information I would want to get
#        #soup.find_all('p')
#        color = soup.find_all('span', id=current_change_id)[0].img['alt']    
#        # drilled down version to get current price:
#        found = []
#        for item in find:
#            found.append(soup.find_all('span', id=item)[0].string)
#        found.insert(0, self.s.upper())
#        found.append(color)
#        return found
    
    def main(self):
        url = self.stockurl()
        html = self.requesturl(url)
        output = self.beautifyhtml(html)
        return output
