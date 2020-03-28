#!/usr/bin/env python3

import os

import numpy as np
import pandas as pd
import datetime as dt
import matplotlib.pyplot as plt

from pandas.plotting import table

import plotly.express as px

# Loading dataset
df = pd.read_csv('data/TSLA.csv',
                 sep=',',
                 header=0, parse_dates=True)

# Creating directory name plot to store the images under folder TSLA-Stocks_Analysis
os.makedirs('plots/TSLA-Stocks_Analysis', exist_ok=True)


# Analyse Volume based on Year
df['Date'] = pd.to_datetime(df['Date'])
df.describe(include="all")
Column_List = ['Open', 'High', 'Low', 'Close', 'Adj Close', 'Volume']

# Decompose the time series year-wise and month-wise to analyse further
df['Year'] = df['Date'].dt.year
df['Month'] = df['Date'].dt.month
df['WeekDay'] = df['Date'].dt.weekday

for i, col_list in enumerate(Column_List):
    var = df.groupby('Year')[col_list].sum()

# Convert the variable into a pandas dataframe
var = pd.DataFrame(var)

# Plot to understand the trend
plt.figure(figsize=(16, 7))
ax1 = plt.subplot(121)
var.plot(kind="pie", y="Volume", legend=False, fontsize=12, sharex=False,
         title="Time Series Influence on Total Volume Trade by Year", ax=ax1)

# Plot the table to identify numbers
ax2 = plt.subplot(122)
plt.axis('off')  # Since we are plotting the table
tbl = table(ax2, var, loc='center')
tbl.auto_set_font_size(False)
tbl.set_fontsize(12)
plt.savefig('plots/TSLA-Stocks_Analysis/TSLA_total_volume.png')

# #using plotly
fig = px.line(df, x='Date', y='Close')
fig.show()
# fig.write_image('plots/TSLA-Stocks_Analysis/TSLA_plotly.png')


# plot multiple plots on the same axes, to get some perspective on their comparisons
fig, axes = plt.subplots(1, 1, figsize=(5, 5))
axes.scatter(df['Date'], df['Close'], alpha=0.2, label='Close', s= 0.4, color='red')
axes.scatter(df['Date'], df['High'], alpha=0.2, label='High', s= 0.4, color='blue')
axes.scatter(df['Date'], df['Low'], alpha=0.2, label='Low', s= 0.4, color='green')

axes.set_xlabel('Date')
axes.set_ylabel('Stock Rate')
axes.set_title(f'Stocks comparisons')
axes.legend()
plt.savefig(f'plots/TSLA-Stocks_Analysis/Stocks_comparision.png', dpi=300)

plt.close()