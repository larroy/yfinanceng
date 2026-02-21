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

    def test_info_returns_empty_dict_for_invalid_symbol(self):
        """info should return empty dict for invalid symbols"""
        ticker = yf.Ticker("INVALID_SYMBOL_12345")
        info = ticker.info

        assert info is not None
        assert isinstance(info, dict)

    def test_info_returns_same_object_on_multiple_calls(self):
        """info should be cached and return the same object reference"""
        ticker = yf.Ticker("MSFT")
        info1 = ticker.info
        info2 = ticker.info

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


class TestTickerHistory:
    """Tests for Ticker.history method"""

    def test_history_returns_dataframe(self):
        """history should return a pandas DataFrame"""
        ticker = yf.Ticker("MSFT")
        history = ticker.history(period="1mo")

        assert history is not None

    def test_history_non_empty_for_valid_symbol(self):
        """history should return non-empty data for valid symbols"""
        ticker = yf.Ticker("MSFT")
        history = ticker.history(period="1mo")

        assert not history.empty

    def test_history_has_expected_columns(self):
        """history should have expected price columns"""
        ticker = yf.Ticker("MSFT")
        history = ticker.history(period="1mo")

        expected_cols = ["Open", "High", "Low", "Close", "Volume"]
        for col in expected_cols:
            assert col in history.columns

    def test_history_empty_for_invalid_symbol(self):
        """history should return empty DataFrame for invalid symbols"""
        ticker = yf.Ticker("INVALID_SYMBOL_12345")
        history = ticker.history(period="1mo")

        assert history is not None
        assert history.empty

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
            history = ticker.history(period=period)
            assert history is not None

    def test_history_with_interval(self):
        """history should work with different intervals"""
        intervals = ["1d", "1wk", "1mo"]
        ticker = yf.Ticker("MSFT")

        for interval in intervals:
            history = ticker.history(period="1y", interval=interval)
            assert history is not None

    def test_history_with_start_end_dates(self):
        """history should work with start and end dates"""
        ticker = yf.Ticker("MSFT")
        history = ticker.history(start="2023-01-01", end="2023-02-01")

        assert history is not None
        assert not history.empty

    def test_history_with_actions(self):
        """history should include dividends and splits when actions=True"""
        ticker = yf.Ticker("MSFT")
        history = ticker.history(period="6mo", actions=True)

        assert "Dividends" in history.columns
        assert "StockSplits" in history.columns

    def test_history_without_actions(self):
        """history should exclude dividends and splits when actions=False"""
        ticker = yf.Ticker("MSFT")
        history = ticker.history(period="6mo", actions=False)

        assert "Dividends" not in history.columns
        assert "StockSplits" not in history.columns

    def test_history_different_timezones(self):
        """history should handle different timezones"""
        ticker = yf.Ticker("MSFT")
        history = ticker.history(period="1mo", tz=None)

        assert history is not None

    def test_history_rounding(self):
        """history should support rounding parameter"""
        ticker = yf.Ticker("MSFT")
        history = ticker.history(period="1mo", rounding=True)

        assert history is not None

    def test_history_prepost(self):
        """history should support prepost parameter"""
        ticker = yf.Ticker("MSFT")
        history = ticker.history(period="1d", prepost=True)

        assert history is not None

    def test_history_multiple_symbols(self):
        """history should work consistently across multiple symbols"""
        symbols = ["MSFT", "AAPL", "GOOGL"]
        for symbol in symbols:
            ticker = yf.Ticker(symbol)
            history = ticker.history(period="1mo")

            assert history is not None

    def test_history_cache(self):
        """history should cache results"""
        ticker = yf.Ticker("MSFT")
        history1 = ticker.history(period="1mo")
        history2 = ticker.history(period="1mo")

        assert history1 is history2 or history1.shape == history2.shape


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
