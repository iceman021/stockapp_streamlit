import yfinance as yf
import streamlit as st
import pandas as pd

st.write("""
# Simple stock price

Show the Apple stock closing price and volume

""")

# define ticker symbol
tickerSymbol = 'AAPL'
# get data on this ticker
tickerData = yf.Ticker(tickerSymbol)
# get historical prices for this ticker
tickerDf = tickerData.history(period='1d', start='2012-8-10', end='2020-8-10')
# Open High    Low Close    Volume   Dividends   Stock Splits

st.line_chart(tickerDf.Close)
st.line_chart(tickerDf.Volume)
