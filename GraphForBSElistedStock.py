import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd
import pandas_datareader.data as web
import os

scrip_code=input('Enter the Scrip code for the stock (its a 6 digit code)')
start_date=input('Enter the Start Date in DDMMYYYY format')
end_date=input('Enter the End date in DDMMYYYY format')
api='owbvGjkTGXoxsxyhMp2m'

start=dt.datetime(int(start_date[4:]),int(start_date[2:4]),int(start_date[0:2]))
end=dt.datetime(int(end_date[4:]),int(end_date[2:4]),int(end_date[0:2]))
df=web.DataReader('BSE/BOM'+scrip_code,'quandl',start,end,api_key=api)

df.plot()
plt.show()
