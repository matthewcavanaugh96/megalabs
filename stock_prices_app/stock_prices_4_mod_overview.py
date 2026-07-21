import streamlit as st


#st.set_page_config(page_title="Test Page", page_icon="📈", layout="centered")

st.title("Modeling Overview")
         
tab1, tab2, tab3, tab4 = st.tabs([
    "All my metrics",
    "My decision making process",
    "Feature Set 1",
    "General findings"
])





with tab1:
    st.header("All my metrics")
    st.write(""" 
    Here, I break down every metric, calculated or otherwise, whether it was used in modeling or not.
    """)

    st.subheader("Included directly from API")
    st.write("""
    These are columns I was able to download directly from the API.
    
    timestamp, ticker, open, high, low, close, volume, vwap, transaction, name, market_cap, exchange, country
    """)

    st.subheader("Simple moving averages")
    st.write("""
    Rolling averages of closing prices over a set number of days.
    SMA10, SMA20, SMA50, SMA100
    """)

    st.subheader("Percentage changes")
    st.write("""
    pct_change_from_prev, next_close_pct_change (this is my target), close_pct_of_day1
    """)

    st.subheader("Intra-day comparisons")
    st.write("""
    pct_change_from_prev, next_close_pct_change (this is my target), close_pct_of_day1
    """)

    st.subheader("Daily vs trend comparisons")
    st.write("""
    'close_vs_SMA10', 'close_vs_SMA20', 'close_vs_SMA50', 'close_vs_SMA100', 'rolling_std_5',
    'rolling_std_10', 'rolling_std_20', 'rolling_std_50', 'rolling_std_100', 'volume_vs_avg_5',
    'volume_vs_avg_10', 'volume_vs_avg_20', 'volume_vs_avg_50', 'volume_vs_avg_100'
     """)

    st.subheader("Daily returns vs previous days")
    st.write("""
    '5_day_return', '10_day_return', '20_day_return'
     """)

    st.subheader("Bollinger Bands and etc")
    st.write("""
    RSI14', 'EMA12', 'EMA26', 'MACD', 'MACD_signal', 'MACD_hist',
    'MACD_pct', 'MACD_signal_pct', 'MACD_hist_pct', 'BB_middle', 'BB_std',
    'BB_upper', 'BB_lower', 'BB_position', 'BB_width']
    """)
    
    
    st.subheader("FULL LIST, UPDATE AS NEEDED THEN ENSURE ABOVE CATEGORIES MATCH")
    st.write("""

    ['timestamp', 'ticker', 'open', 'high', 'low', 'close', 'volume', 'vwap',
       'transactions', 'name', 'market_cap', 'exchange', 'country', 'SMA10',
       'SMA20', 'SMA50', 'SMA100', 'pct_change_from_prev',
       'next_close_pct_change', 'close_pct_of_day1', 'close_vs_SMA10',
       'close_vs_SMA20', 'close_vs_SMA50', 'close_vs_SMA100', 'close_vs_open',
       'high_vs_low', 'high_vs_close', 'low_vs_close', 'positive_streak',
       'negative_streak', 'rolling_std_5', 'rolling_std_10', 'rolling_std_20',
       'rolling_std_50', 'rolling_std_100', 'volume_vs_avg_5',
       'volume_vs_avg_10', 'volume_vs_avg_20', 'volume_vs_avg_50',
       'volume_vs_avg_100', '5_day_return', '10_day_return', '20_day_return',
       'RSI14', 'EMA12', 'EMA26', 'MACD', 'MACD_signal', 'MACD_hist',
       'MACD_pct', 'MACD_signal_pct', 'MACD_hist_pct', 'BB_middle', 'BB_std',
       'BB_upper', 'BB_lower', 'BB_position', 'BB_width'],
      dtype='object')
    """)




with tab2:
    st.header("My decision making process")
    st.write("""
    The target column, 'next_close_pct_change' obviously had to be excluded. Same for 'pct_change_from_prev' which is the exact same number, just shifted forward one day.

    Beyond this, my decision became a little trickier.

    One idea is to drop all columns containing raw price data, and use only percentage-based metrics.
    """)


with tab3:
    st.header("Feature Set 1")
    st.write("""
    Placeholder
    """)

with tab4:
    st.header("General findings")
    st.write("""
    Placeholder
    """)