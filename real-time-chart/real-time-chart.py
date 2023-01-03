import matplotlib.pyplot as plt
import matplotlib
import numpy as np
import yfinance as yf
from datetime import datetime, timezone, timedelta

#examples
#stock = "BTC-USD"
#stock = "JPY=X"
stock = input("Enter the stock name(CandleSticks may not be shown depending on the stock): ")
now = datetime.now(timezone.utc)
#get data from yfinance
data = yf.download(stock, start=now-timedelta(hours = 1), end=now, interval="1m")
x = data.index
y = data['Adj Close'].values.tolist()
up = data[data['Close'] >= data['Open']]
down = data[data['Close'] < data['Open']]
#plot setting
fig, ax = plt.subplots(1, 1, figsize=(16,9), dpi= 80)
plt.ion()
#setting for candle sticks
col1 = 'green'
col2 = 'red'
width = .0003
width2 = .00009

while True:
    #draw setting
    plt.xlabel("Time")
    plt.ylabel("Price")
    plt.xticks(x, x.strftime("%H:%M"), fontsize=10, horizontalalignment='center', rotation=45)
    plt.xticks(x, x.strftime("%H:%M"), fontsize=10, horizontalalignment='center', rotation=45)
    plt.yticks(np.arange(np.min(data['Low']), np.max(data['High']), (np.max(data['High'])-np.min(data['Low']))/10), fontsize=10)
    plt.xlim(x[0], x[-1])
    plt.ylim(np.min(data['Low']), np.max(data['High']))
    ax.set_title(stock, fontsize=18)
    ax.grid()
    ax.get_yaxis().set_major_formatter(matplotlib.ticker.FuncFormatter(lambda x, p: format(float(x), ',.4f')))
    #draw
    ax.fill_between(x, y1=y, y2=0, label="Close:"+str(format(y[-1], ',.4f')), alpha=0.2, color='tab:blue', linewidth=4)
    ax.legend(loc='best', fontsize=12)
    ax.bar(up.index, up.Close-up.Open, width, bottom=up.Open, color=col1)
    ax.bar(up.index, up.High-up.Close, width2, bottom=up.Close, color=col1)
    ax.bar(up.index, up.Low-up.Open, width2, bottom=up.Open, color=col1)
    ax.bar(down.index, down.Close-down.Open, width, bottom=down.Open, color=col2)
    ax.bar(down.index, down.High-down.Open, width2, bottom=down.Open, color=col2)
    ax.bar(down.index, down.Low-down.Close, width2, bottom=down.Close, color=col2)

    plt.pause(30)
    #new data
    now = datetime.now(timezone.utc)
    data = yf.download(stock, start=now-timedelta(hours = 1), end=now, interval="1m")
    x = data.index
    y = data['Adj Close'].values.tolist()
    up = data[data['Close'] >= data['Open']]
    down = data[data['Close'] < data['Open']]

    ax.cla()
