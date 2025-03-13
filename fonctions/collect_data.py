import yfinance as yf

'''fonction de recuperation des donnes de monnaie avec l'API de yahoofinance
    parametre: ticker: la devise desire en type (chaine de caractere) , 
         period_start: date des debut devaluation en type (Date)  '''
def get_crypto_data(ticker,period_start):
    crypto = yf.Ticker(ticker)
    hist = crypto.history(start=period_start)  
    return hist


