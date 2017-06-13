'''
Created on Sep 10, 2013

@author: matthassel

Example:

'''
from time import sleep
import numpy as np
from myalphabet import *
from copy import copy
from Adafruit_8x8 import ColorEightByEight

class Text2LED():
    
    def __init__(self):
        pass

    def map_string_to_matrix(self, string):
        '''takes a string, converts it to uppercase, and 
        returns the matching matrix variable if a letter match
        is made.
        
        USAGE:
        mapStringToMatrix("teststring")
        '''
        string = string.upper()
        matrixOfText = []
        for l in string:
            matrixOfText.append([matrix for (letter, matrix) in \
                    myalphabet if letter == l])
        return matrixOfText
    
    def get_column(self, matrix, i):
        '''returns a single column from a matrix'''
        return [row[:,i] for row in matrix]
    
    def matrix_to_column_list(self, text):
        text2tick = {}
        start = 0
        for z in range(len(text)):
            for c in range(0,8):
                try:
                    col = self.get_column(text[z], c)
                    text2tick[start] = col
                    start += 1
                except IndexError:
                    break
        return text2tick    
    
    def add_to_ticker(self, string, color="green"):
        ticker = []
        if color == "red":
            color = 256
        elif color == "yellow":
            color = 257
        else:
            color = 1
        text2tick = self.matrix_to_column_list(self.map_string_to_matrix(string))
        for i in range(len(text2tick)):
            #print "i: ", i,": ",text2tick[i]
            total = 0
            display = []
            for list in text2tick[i]:
                for index, item in enumerate(list):
                    #print(index, item)
                    if index == 0 and item != 0:
                        total += 1
                    if index == 1 and item != 0:
                        total += 2
                    if index == 2 and item != 0:
                        total += 4
                    if index == 3 and item != 0:
                        total += 8
                    if index == 4 and item != 0:
                        total += 16
                    if index == 5 and item != 0:
                        total += 32
                    if index == 6 and item != 0:
                        total += 64
                    if index == 7 and item != 0:
                        total += 128
            total = total * color 
            display.append(total)
            ticker = ticker + display
        return ticker

class LED_TICKER():
        
    def __init__(self):
        self.grid1 = ColorEightByEight(address=0x70)
        self.grid2 = ColorEightByEight(address=0x71)
        self.grid3 = ColorEightByEight(address=0x72)
        self.grid4 = ColorEightByEight(address=0x74)
        self.ticker = []
        self.buffer = []
        self.display = []
        
    def scrolling_ticker_text(self):
        for i in self.ticker:
            self.display = []
            self.display.append(i)
            self.buffer = self.display + self.buffer
            self.update_ticker_w_buffer()
            sleep(0.04)
            
    def update_ticker_w_buffer(self):
        self.grid1.disp.writeMyDisplay(self.buffer[0:8])
        self.grid2.disp.writeMyDisplay(self.buffer[8:16])
        self.grid3.disp.writeMyDisplay(self.buffer[16:24])
        self.grid4.disp.writeMyDisplay(self.buffer[24:32])
        self.ticker[len(self.ticker):] = []
        self.buffer[len(self.buffer):] = []
        self.display[len(self.display):] = []
    
    def main(self):
        self.scrolling_ticker_text()
        self.update_ticker_w_buffer()

if __name__ == '__main__':
    color = "yellow"
    app_text = Text2LED()
    app_ticker = LED_TICKER()
    app_ticker.ticker = app_ticker.ticker + app_text.add_to_ticker("It has been ", color) + \
                                            app_text.add_to_ticker("0", "red") + \
                                            app_text.add_to_ticker(" days since Murphy has had an accident!!", "yellow") + \
                                            app_text.add_to_ticker("                 ", "yellow")
    app_ticker.main()
