import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt

start_date = '2023-01-01'
end_date = '2024-01-01'

stock_data = yf.download('GOOGL', start=start_date, end=end_date)

plt.figure(figsize=(10, 6))
plt.plot(stock_data['Close'], label='Alphabet Inc. (GOOGL)')

plt.title('Alphabet Inc. (GOOGL) Stock Prices - Historical Data')
plt.xlabel('Date')
plt.ylabel('Stock Price (USD)')
plt.legend()
plt.grid(True)
plt.show()
