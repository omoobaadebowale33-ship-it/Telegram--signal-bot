import os
import requests
import time
import random
import pandas as pd
import numpy as np
import yfinance as yf

# ==============================
# TELEGRAM CONFIGURATION
# ==============================
BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

# ==============================
# MARKET SETTINGS
# ==============================
PAIRS = ["EURUSD=X", "BTC-USD", "XAUUSD=X", "AUDJPY=X", "EURJPY=X", "AUDCAD=X"]
INTERVAL_MINUTES = 15
SIGNAL_EXPIRY_MINUTES = 30

# ==============================
# STRATEGY CONFIG
# ==============================
def get_signal(pair):
    try:
        data = yf.download(pair, period="1d", interval="15m")
        if len(data) < 50:
            return None
        
        data["EMA20"] = data["Close"].ewm(span=20).mean()
        data["EMA50"] = data["Close"].
