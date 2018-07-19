from x10project import BaseExchangeBL, BittrexClient 
from bittrex.bittrex import *

#https://github.com/ericsomdahl/python-bittrex
class BittrexLogic(BaseExchangeBL):

    def __init__(self, acc_name='', api_key='', api_secret=''):
        super().__init__("bittrex", api_key, api_secret)
        self.bittrexClient = Bittrex(self.api_key, self.api_secret, api_version=API_V1_1) 