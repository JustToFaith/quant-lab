import pandas as pd
import yfinance as yf
from strategies.simple_ma import SimpleMAStrategy

# 下载历史数据
symbol = 'AAPL'
data = yf.download(symbol, start='2022-01-01', end='2023-01-01')

# 初始化策略
strategy = SimpleMAStrategy(short_window=20, long_window=50)
signals = strategy.generate_signals(data)

# 简单回测逻辑
initial_cash = 100000
position = 0
cash = initial_cash
for i in range(1, len(signals)):
    if signals['signal'].iloc[i] == 1 and position == 0:
        position = cash / data['Close'].iloc[i]
        cash = 0
        print(f"买入: {data.index[i].date()} 价格: {data['Close'].iloc[i]:.2f}")
    elif signals['signal'].iloc[i] == -1 and position > 0:
        cash = position * data['Close'].iloc[i]
        position = 0
        print(f"卖出: {data.index[i].date()} 价格: {data['Close'].iloc[i]:.2f}")

final_value = cash if position == 0 else position * data['Close'].iloc[-1]
print(f"初始资金: {initial_cash}, 最终资金: {final_value:.2f}") 