import yfinance as yf

def get_crypto_data(ticker, period_start):
    """
    Retrieves cryptocurrency data using the Yahoo Finance API.

    Parameters:
    ticker (str): The cryptocurrency ticker symbol (e.g., 'BTC-USD', 'ETH-USD').
    period_start (str): The start date for data collection in 'YYYY-MM-DD' format.

    Returns:
    pandas.DataFrame: A DataFrame containing historical cryptocurrency data.
    The DataFrame includes columns for 'Open', 'High', 'Low', 'Close', 'Volume', and 'Dividends'.
    """
    crypto = yf.Ticker(ticker)
    hist = crypto.history(start=period_start)
    return hist

