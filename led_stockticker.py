#!/usr/bin/python
''' Created on Oct 10, 2013

@author: matthassel
'''
import yahooStockQuote.yahooStockQuote as yql
import string2matrix.string2matrix as str2mat
import daemon
#from daemon import runner
from threading import Thread
from time import sleep
from copy import copy
from sys import exit


class ledStockTicker():

    def __init__(self):
        #self.stdin_path = '/dev/null'
        #self.stdout_path = '/dev/tty'
        #self.stderr_path = '/dev/tty'
        #self.pidfile_path = '/tmp/led.pid'
        #self.pidfile_timeout = 5
        self.app_text = str2mat.Text2LED() # initialize test to matrix app
        self.app_ticker = str2mat.LED_TICKER() # Initialize LED ticker
        self.stock_quotes = []
        self.main()

    def stock_data(self,delay=30):
        '''Queries yahoo site for stock(s) info'''
        print "stock_data called"
        def get_data(s):
            print "stock_date --> get_data called"
            yql_app = yql.StockQuote(s)
            local_stocks.append(yql_app.main())
            #print "gettig stockquotes", local_stocks
        delay = delay * 60
        stocks = ['amd', 'mu', 'csco', 'goog']
        while True:
            local_stocks = []
            threads = [] # creating a list of threads
            for s in stocks:
                s = Thread(target=get_data, args=(s,)) # create a new thread
                threads.append(s) # append thread to thread list

            # start all threads
            [x.start() for x in threads]

            # Wait for all of them to finish
            [x.join() for x in threads]
            global stock_quotes
            self.stock_quotes = []
            self.stock_quotes = local_stocks
            print "stocks are going through", self.stock_quotes
            sleep(delay)
            
    def stock_ticker_start(self):
        print "stock_ticker_start called"
        stock_quotes_copy = []
        while True:
            if self.stock_quotes:
                stock_quotes_copy = copy(self.stock_quotes)
            if not stock_quotes_copy:
                pass
            else:
                for stock in stock_quotes_copy:
                    color = "yellow"
                    self.app_ticker.ticker = self.app_ticker.ticker + self.app_text.add_to_ticker(stock[0].strip(' '), color)
                    self.app_ticker.ticker = self.app_ticker.ticker + self.app_text.add_to_ticker("-", color)
                    if "Down" in stock:
                        color = "red"
                        #print "red"
                    elif "Up" in stock:
                        color = "green"
                        #print "green"
                    for info in stock[1:4]:
                        self.app_ticker.ticker = self.app_ticker.ticker + self.app_text.add_to_ticker(info.strip('( )').replace(',', ''), color)
                        self.app_ticker.ticker = self.app_ticker.ticker + self.app_text.add_to_ticker(" ", color)
                        #print app_ticker.ticker
                self.app_ticker.main()
    
    
    def main(self):
    #def run(self):
        self.main_threads = []
        try:
            print "started main"
            self.p1 = Thread(target=self.stock_data)
            self.p1.daemon = True
            self.p2 = Thread(target=self.stock_ticker_start)
            #self.p2.daemon = True
            self.main_threads.append(self.p1)
            self.main_threads.append(self.p2)
            # start main threads
            [x.start() for x in self.main_threads]
        except KeyboardInterrupt:
            # join threads
            [x.join() for x in self.main_threads]



if __name__ == "__main__":
    with daemon.DaemonContext():
        ledStockTicker()
    #app =  ledStockTicker()
    #dameon_runner = runner.DaemonRunner(app)
    #dameon_runner.do_action()
        
