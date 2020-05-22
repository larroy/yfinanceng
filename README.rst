Yahoo! Finance-ng python3 / pandas market data downloader
=========================================================

.. image:: https://img.shields.io/badge/python-3.6+-blue.svg?style=flat
    :target: https://pypi.python.org/pypi/yfinanceng
    :alt: Python version

.. image:: https://img.shields.io/pypi/v/yfinanceng.svg?maxAge=60
    :target: https://pypi.python.org/pypi/yfinanceng
    :alt: PyPi version

.. image:: https://img.shields.io/pypi/status/yfinanceng.svg?maxAge=60
    :target: https://pypi.python.org/pypi/yfinanceng
    :alt: PyPi status

.. image:: https://img.shields.io/pypi/dm/yfinanceng.svg?maxAge=2592000&label=installs&color=%2327B1FF
    :target: https://pypi.python.org/pypi/yfinanceng
    :alt: PyPi downloads

.. image:: https://img.shields.io/travis/larroy/yfinanceng/master.svg?maxAge=1
    :target: https://travis-ci.com/larroy/yfinanceng
    :alt: Travis-CI build status

.. image:: https://www.codefactor.io/repository/github/larroy/yfinanceng/badge
    :target: https://www.codefactor.io/repository/github/larroy/yfinanceng
    :alt: CodeFactor

.. image:: https://img.shields.io/github/stars/larroy/yfinanceng.svg?style=social&label=Star&maxAge=60
    :target: https://github.com/larroy/yfinanceng
    :alt: Star this repo

.. image:: https://img.shields.io/twitter/follow/larroy.svg?style=social&label=Follow&maxAge=60
    :target: https://twitter.com/larroy
    :alt: Follow me on twitter

\

Ever since `Yahoo! finance <https://finance.yahoo.com>`_ decommissioned
their historical data API, many programs that relied on it to stop working.

**yfinanceng** aimes to solve this problem by offering a reliable, threaded,
and Pythonic way to download historical market data from Yahoo! finance.


NOTE
~~~~

The library was originally named ``yfinance``, but
I've since renamed it to ``yfinanceng`` as I no longer consider it a mere "fix", and the author is
not promptly maintaining it or merging PRs.

`Changelog » <./CHANGELOG.rst>`__


-----

Quick Start
===========

The Ticker module
~~~~~~~~~~~~~~~~~

The ``Ticker`` module, which allows you to access
ticker data in amore Pythonic way:

.. code:: python

    import yfinanceng as yf

    msft = yf.Ticker("MSFT")

    # get stock info
    msft.info

    # get historical market data
    hist = msft.history(period="max")

    # show actions (dividends, splits)
    msft.actions

    # show dividends
    msft.dividends

    # show splits
    msft.splits

    # show financials
    msft.financials
    msft.quarterly_financials

    # show major holders
    msft.major_holders

    # show institutional holders
    msft.institutional_holders

    # show balance heet
    msft.balance_sheet
    msft.quarterly_balance_sheet

    # show cashflow
    msft.cashflow
    msft.quarterly_cashflow

    # show earnings
    msft.earnings
    msft.quarterly_earnings

    # show sustainability
    msft.sustainability

    # show analysts recommendations
    msft.recommendations

    # show next event (earnings, etc)
    msft.calendar

    # show ISIN code - *experimental*
    # ISIN = International Securities Identification Number
    msft.isin

    # show options expirations
    msft.options

    # get option chain for specific expiration
    opt = msft.option_chain('YYYY-MM-DD')
    # data available via: opt.calls, opt.puts

If you want to use a proxy server for downloading data, use:

.. code:: python

    import yfinanceng as yf

    msft = yf.Ticker("MSFT")

    msft.history(..., proxy="PROXY_SERVER")
    msft.get_actions(proxy="PROXY_SERVER")
    msft.get_dividends(proxy="PROXY_SERVER")
    msft.get_splits(proxy="PROXY_SERVER")
    msft.get_balance_sheet(proxy="PROXY_SERVER")
    msft.get_cashflow(proxy="PROXY_SERVER")
    msgt.option_chain(..., proxy="PROXY_SERVER")
    ...

To initialize multiple ``Ticker`` objects, use

.. code:: python

    import yfinanceng as yf

    tickers = yf.Tickers('msft aapl goog')
    # ^ returns a named tuple of Ticker objects

    # access each ticker using (example)
    tickers.msft.info
    tickers.aapl.history(period="1mo")
    tickers.goog.actions


Fetching data for multiple tickers
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code:: python

    import yfinanceng as yf
    data = yf.download("SPY AAPL", start="2017-01-01", end="2017-04-30")


I've also added some options to make life easier :)

.. code:: python

    data = yf.download(  # or pdr.get_data_yahoo(...
            # tickers list or string as well
            tickers = "SPY AAPL MSFT",

            # use "period" instead of start/end
            # valid periods: 1d,5d,1mo,3mo,6mo,1y,2y,5y,10y,ytd,max
            # (optional, default is '1mo')
            period = "ytd",

            # fetch data by interval (including intraday if period < 60 days)
            # valid intervals: 1m,2m,5m,15m,30m,60m,90m,1h,1d,5d,1wk,1mo,3mo
            # (optional, default is '1d')
            interval = "1m",

            # group by ticker (to access via data['SPY'])
            # (optional, default is 'column')
            group_by = 'ticker',

            # adjust all OHLC automatically
            # (optional, default is False)
            auto_adjust = True,

            # download pre/post regular market hours data
            # (optional, default is False)
            prepost = True,

            # use threads for mass downloading? (True/False/Integer)
            # (optional, default is True)
            threads = True,

            # proxy URL scheme use use when downloading?
            # (optional, default is None)
            proxy = None
        )


``pandas_datareader`` override
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If your code uses ``pandas_datareader`` and you want to download data faster,
you can "hijack" ``pandas_datareader.data.get_data_yahoo()`` method to use
**yfinanceng** while making sure the returned data is in the same format as
**pandas_datareader**'s ``get_data_yahoo()``.

.. code:: python

    from pandas_datareader import data as pdr

    import yfinanceng as yf
    yf.pdr_override() # <== that's all it takes :-)

    # download dataframe
    data = pdr.get_data_yahoo("SPY", start="2017-01-01", end="2017-04-30")


Installation
------------

Install ``yfinanceng`` using ``pip``:

.. code:: bash

    $ pip install yfinanceng --upgrade --no-cache-dir


Install ``yfinanceng`` using ``conda``:

.. code:: bash

    $ conda install -c larroy yfinanceng


Requirements
------------

* `Python <https://www.python.org>`_ >= 3.6+
* `Pandas <https://github.com/pydata/pandas>`_ (tested to work with >=0.23.1)
* `Numpy <http://www.numpy.org>`_ >= 1.11.1
* `requests <http://docs.python-requests.org/en/master/>`_ >= 2.14.2


Optional (if you want to use ``pandas_datareader``)
---------------------------------------------------

* `pandas_datareader <https://github.com/pydata/pandas-datareader>`_ >= 0.4.0

Legal Stuff
------------

**yfinanceng** is distributed under the **Apache Software License**. See the `LICENSE.txt <./LICENSE.txt>`_ file in the release for details.


Based on **yfinance** from **Ran Aroussi**.
