import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt

start_date = '2023-01-01'
end_date = '2024-01-01'

stock_data = yf.download('GOOGL', start=start_date, end=end_date)

plt.figure(figsize=(10, 6))
stock_data['Volume'].plot(kind='bar', color='blue', alpha=0.7)

plt.title('Alphabet Inc. (GOOGL) Trading Volume - Historical Data')
plt.xlabel('Date')
plt.ylabel('Trading Volume')
plt.grid(axis='y')
plt.show()
