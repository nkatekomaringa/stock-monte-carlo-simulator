import yfinance as yf
import pandas as pd
import numpy as np

class MarketDataLoader:
    def __init__(self, ticker: str, period: str = "2y"):
        self.ticker = ticker
        self.period = period

    def fetch_data(self) -> pd.Series:
        """Fetches historical daily close prices for the specified ticker."""
        df = yf.download(self.ticker, period=self.period, progress=False)
        if df.empty:
            raise ValueError(f"No data returned for ticker: {self.ticker}")
        if isinstance(df.columns, pd.MultiIndex):
            close_prices = df['Close'][self.ticker]
        else:
            close_prices = df['Close']
        return close_prices.dropna()

    def get_log_returns(self, prices: pd.Series) -> pd.Series:
        """Calculates daily log returns."""
        return np.log(prices / prices.shift(1)).dropna()
