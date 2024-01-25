import inline as inline
import matplotlib
import pandas as pd
import mplfinance as mpf
file = 'FB.csv'
data = pd.read_csv(file)
data.Date = pd.to_datetime(data.Date)

data = data.set_index('Date')
#print(data)
#print(mpf.plot(data))
print(mpf.plot(data, type='line', volume=True))
