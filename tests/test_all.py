#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
#

"""
Sanity check for most common library uses all working

- Stock: Microsoft
- ETF: Russell 2000 Growth
- Mutual fund: Vanguard 500 Index fund
- Index: S&P500
- Currency BTC-USD
"""

from __future__ import print_function
import yfinanceng as yf


def test_yfinanceng():
    for symbol in ["MSFT", "VFINX", "^GSPC", "BTC-USD"]:
        print(">>", symbol, end=" ... ")
        ticker = yf.Ticker(symbol)

        # always should have info and history for valid symbols
        assert ticker.info is not None and ticker.info != {}
        assert ticker.history(period="max").empty is False

        # following should always gracefully handled, no crashes
        ticker.cashflow
        ticker.balance_sheet
        ticker.financials
        ticker.sustainability
        ticker.major_holders
        ticker.institutional_holders

        print("OK")


def test_not_existing():
    t = yf.Ticker("ASD9867987ASD")
    nfo = t.info
    assert not nfo


if __name__ == "__main__":
    test_yfinanceng()
