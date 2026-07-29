import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("TWELVE_DATA_API_KEY")

BASE_URL = "https://api.twelvedata.com/time_series"


def get_candles(symbol="EUR/USD", interval="1min"):

    params = {
        "symbol": symbol,
        "interval": interval,
        "outputsize": 200,
        "apikey": API_KEY,
    }

    response = requests.get(BASE_URL, params=params, timeout=15)

    if response.status_code != 200:
        return None

    return response.json()
