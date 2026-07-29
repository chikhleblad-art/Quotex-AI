"""
Market data module
Version 1.0
"""

class MarketData:

    def __init__(self):
        self.symbol = ""
        self.price = 0.0
        self.trend = "UNKNOWN"

    def set_market(self, symbol, price, trend):
        self.symbol = symbol
        self.price = price
        self.trend = trend

    def info(self):
        return {
            "symbol": self.symbol,
            "price": self.price,
            "trend": self.trend
        }
