"""
Market Data Module
Gets live market data from Twelve Data
"""

import os
import requests

API_KEY = os.getenv("TWELVE_DATA_API_KEY")

BASE_URL = "https://api.twelvedata.com/time_series"


def get_market_data(symbol="EUR/USD", interval="1min", outputsize=100):
    params = {
        "symbol": symbol,
        "interval": interval,
        "outputsize": outputsize,
        "apikey": API_KEY,
    }

    response = requests.get(BASE_URL, params=params, timeout=15)
    response.raise_for_status()
    return response.json()
