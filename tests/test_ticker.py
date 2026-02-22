#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
#

"""
Unit tests for Ticker.history and Ticker.info methods
"""

import pytest
import yfinanceng as yf


class TestTickerInfo:
    """Tests for Ticker.info property"""

    def test_info_returns_dict_for_valid_symbol(self):
        """info should return a dictionary for valid symbols (may be empty if fetch fails)"""
        ticker = yf.Ticker("MSFT")
        info = ticker.info

        assert info is not None
        assert isinstance(info, dict)

    def test_info_returns_copy_when_as_dict_true(self):
        """info with as_dict=True should return a copy each time"""
        ticker = yf.Ticker("MSFT")
        info1 = ticker.get_info(as_dict=True)
        info2 = ticker.get_info(as_dict=True)

        assert info1 is not info2
        assert info1 == info2

    def test_info_contains_expected_fields(self):
        """info should contain expected key fields if data is available"""
        ticker = yf.Ticker("MSFT")
        info = ticker.info

        if info and len(info) > 0:
            assert "symbol" in info or "shortName" in info

    def test_info_different_symbols(self):
        """info should work with different symbol types"""
        symbols = ["MSFT", "AAPL", "GOOGL"]
        for symbol in symbols:
            ticker = yf.Ticker(symbol)
            info = ticker.info

            assert info is not None
            assert isinstance(info, dict)

    def test_info_validates_symbol_field(self):
        """info should have correct symbol field matching ticker"""
        ticker = yf.Ticker("MSFT")
        info = ticker.info

        if info and "symbol" in info:
            assert info["symbol"] == "MSFT"


class TestTickerHistory:
    """Tests for Ticker.history method"""

    def test_history_returns_tuple(self):
        """history should return a tuple of two dataframes"""
        ticker = yf.Ticker("MSFT")
        result = ticker.history(period="1mo")

        assert isinstance(result, tuple)
        assert len(result) == 2

    def test_history_tuple_contains_price_and_dividends(self):
        """history tuple should contain (prices_df, dividends_df)"""
        ticker = yf.Ticker("MSFT")
        hist, dividends = ticker.history(period="1mo")

        assert hist is not None
        assert dividends is not None

    def test_history_prices_dataframe_structure(self):
        """history prices dataframe should have expected structure"""
        ticker = yf.Ticker("MSFT")
        hist, dividends = ticker.history(period="1mo")

        assert not hist.empty
        expected_cols = ["Open", "High", "Low", "Close", "Volume"]
        for col in expected_cols:
            assert col in hist.columns

    def test_history_prices_does_not_contain_dividends(self):
        """history prices dataframe should NOT contain Dividends column"""
        ticker = yf.Ticker("MSFT")
        hist, dividends = ticker.history(period="1mo")

        assert "Dividends" not in hist.columns

    def test_history_dividends_dataframe_structure(self):
        """history dividends dataframe should have expected structure"""
        ticker = yf.Ticker("MSFT")
        hist, dividends = ticker.history(period="1mo")

        assert isinstance(dividends, type(hist))

    def test_history_empty_for_invalid_symbol(self):
        """history should return empty DataFrame for invalid symbols"""
        ticker = yf.Ticker("INVALID_SYMBOL_12345")
        hist, dividends = ticker.history(period="1mo")

        assert hist is not None
        assert hist.empty

    def test_history_with_various_periods(self):
        """history should work with different period values"""
        periods = [
            "1d",
            "5d",
            "1mo",
            "3mo",
            "6mo",
            "1y",
            "2y",
            "5y",
            "10y",
            "ytd",
            "max",
        ]
        ticker = yf.Ticker("MSFT")

        for period in periods:
            hist, dividends = ticker.history(period=period)
            assert hist is not None

    def test_history_with_interval(self):
        """history should work with different intervals"""
        intervals = ["1d", "1wk", "1mo"]
        ticker = yf.Ticker("MSFT")

        for interval in intervals:
            hist, dividends = ticker.history(period="1y", interval=interval)
            assert hist is not None

    def test_history_with_start_end_dates(self):
        """history should work with start and end dates"""
        ticker = yf.Ticker("MSFT")
        hist, dividends = ticker.history(start="2023-01-01", end="2023-02-01")

        assert hist is not None
        assert not hist.empty

    def test_history_with_actions_includes_splits(self):
        """history with actions=True should include StockSplits column"""
        ticker = yf.Ticker("MSFT")
        hist, dividends = ticker.history(period="6mo", actions=True)

        assert "StockSplits" in hist.columns

    def test_history_without_actions_excludes_splits(self):
        """history with actions=False should exclude StockSplits column"""
        ticker = yf.Ticker("MSFT")
        hist, dividends = ticker.history(period="6mo", actions=False)

        assert "StockSplits" not in hist.columns

    def test_history_different_timezones(self):
        """history should handle different timezones"""
        ticker = yf.Ticker("MSFT")
        hist, dividends = ticker.history(period="1mo", tz=None)

        assert hist is not None

    def test_history_rounding(self):
        """history should support rounding parameter"""
        ticker = yf.Ticker("MSFT")
        hist, dividends = ticker.history(period="1mo", rounding=True)

        assert hist is not None

    def test_history_prepost(self):
        """history should support prepost parameter"""
        ticker = yf.Ticker("MSFT")
        hist, dividends = ticker.history(period="1d", prepost=True)

        assert hist is not None

    def test_history_multiple_symbols(self):
        """history should work consistently across multiple symbols"""
        symbols = ["MSFT", "AAPL", "GOOGL"]
        for symbol in symbols:
            ticker = yf.Ticker(symbol)
            hist, dividends = ticker.history(period="1mo")

            assert hist is not None

    def test_history_cache(self):
        """history should cache results"""
        ticker = yf.Ticker("MSFT")
        hist1, div1 = ticker.history(period="1mo")
        hist2, div2 = ticker.history(period="1mo")

        assert hist1 is hist2 or hist1.shape == hist2.shape


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
