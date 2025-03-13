import yfinance as yf

def get_crypto_data(ticker,period_start):
    crypto = yf.Ticker(ticker)
    hist = crypto.history(start=period_start)  
    return hist


