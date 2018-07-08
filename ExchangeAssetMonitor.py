#! /usr/bin/env python
# -*- coding: utf-8 -*-

import json
from Utils.MessageSender import MessageType
from ExchangeClients.BinanceClient import BinanceLogic
from ExchangeClients.KucoinClient import KucoinLogic
from ExchangeClients.BitfinexClient import BitfinexLogic
from ExchangeClients.HitBTCClient import HitBTCLogic
from ExchangeClients.IdexClient import IdexLogic
from ExchangeClients.OkexClient import OkexLogic
from Utils.Enums import *
import datetime
import pprint


class AssetMonitor:
    def __init__(self):     
        self.exchangeClients={
                              Exchange.BINANCE: BinanceLogic(),
                              Exchange.KUCOIN: KucoinLogic(),
                              Exchange.BITFINEX: BitfinexLogic(),
                              Exchange.HITBTC: HitBTCLogic(),
                              Exchange.IDEX: IdexLogic(),
                              Exchange.OKEX: OkexLogic()
                            }
        
    def CheckAsset(self):
        
        print('%s  ----Start AssetMonitor.CheckAsset----' % (datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
        
        for key, value in self.exchangeClients.items():
            try:
                value.checkListedAssets()
            except Exception as e:
                print("%s.checkListedAssets error request. Exception %s" % (value.__class__.__name__, str(e)))       

        print('----End process AssetMonitor.CheckAsset----')
        