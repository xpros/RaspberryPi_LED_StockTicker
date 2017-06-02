#!/usr/bin/python
'''
Created on June 2 2017 

@author: matthassel
'''
import sys
import json
import pprint
import urllib

class StockQuote():
    
    def __init__(self):
        self.symbol = 'AAPL'
        self.query_format = 'json'
        self.baseurl = 'https://query.yahooapis.com/v1/public/yql?env=store://datatables.org/alltableswithkeys&'

    def stockurl(self):
        '''Creates and returns a yql query for the yahoo.finance.quote database for a stock.'''
        query = {}
        query['q'] = 'select * from yahoo.finance.quotes where symbol="{}"'.format(self.symbol)
        query['format'] = self.query_format
        url = self.baseurl + urllib.urlencode(query)
        return url
    
    def requesturl(self, url):
        response = urllib.urlopen(url)
        return response

    def response_parser(self, response):
        '''Parses the urllib response from yahoo's yql api and returns a json object.'''
        if self.query_format == 'json':
            return json.loads(response.read().decode('utf-8'))
        else:
            sys.exit(1)

    def quote(self):
        url = self.stockurl()
        response = self.requesturl(url)
        output = self.response_parser(response)['query']['results']['quote']
        return output

if __name__ == '__main__':
    pp = pprint.PrettyPrinter(indent=4)
    app = StockQuote()
    app.symbol = 'AMD'
    pp.pprint(app.quote())
