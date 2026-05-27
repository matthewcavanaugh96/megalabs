import streamlit as st


st.set_page_config(page_title="Stock Trends", page_icon="📈", layout="centered")

st.title("Test")
st.write("""
Test text. 
""")


import pandas as pd

with open("daily_data/COMMAND EVERYTHING.txt", "r") as file:
    code = file.read()
    exec(code)



# # AAPL default
# import streamlit as st
# import matplotlib.pyplot as plt
# import matplotlib.dates as mdates

# aapl_df = df_daily_5_yr[df_daily_5_yr['ticker'] == 'AAPL']
# fig, ax = plt.subplots(figsize=(12, 8))
# aapl_df.set_index('timestamp')['close'].plot(ax=ax)

# ax.set_xlabel('Date')
# plt.xticks(rotation=45)
# ax.xaxis.set_major_locator(mdates.MonthLocator(interval=3))
# ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m'))
# ax.grid()
# ax.set_title('AAPL stock price over five years')
# st.pyplot(fig)






st.write("""
Let's see AAPL's stock price over five years. 
""")

# AAPL with SMAs

import streamlit as st
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

aapl_df = df_daily_5_yr[df_daily_5_yr['ticker'] == 'AAPL']

# -------------------------
# FIRST CHART
# -------------------------

fig1, ax1 = plt.subplots(figsize=(12, 8))

aapl_df.set_index('timestamp')['close'].plot(ax=ax1)

ax1.set_xlabel('Date')
ax1.set_title('AAPL stock price over five years')

ax1.xaxis.set_major_locator(mdates.MonthLocator(interval=3))
ax1.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m'))

plt.setp(ax1.get_xticklabels(), rotation=45)

ax1.grid()

st.pyplot(fig1)

# -------------------------
# SECOND CHART (SMAs)
# -------------------------

st.write("""
Now we will add SMAs (simple moving averages). You may notice that the SMA lines do not start immediately. This is due to there being insufficient days to calculate them. As each SMA begins, you can still see how the previous days are influencing it. The longer the SMA, the smoother the line.
""")


features_to_plot = ['close', 'SMA20', 'SMA50', 'SMA100']

fig2, ax2 = plt.subplots(figsize=(12, 8))

for feature in features_to_plot:
    aapl_df.set_index('timestamp')[feature].plot(
        ax=ax2,
        label=feature
    )

ax2.set_xlabel('Date')
ax2.set_title('AAPL stock price with Simple Moving Averages')

ax2.xaxis.set_major_locator(mdates.MonthLocator(interval=3))
ax2.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m'))

plt.setp(ax2.get_xticklabels(), rotation=45)

ax2.legend()
ax2.grid()

st.pyplot(fig2)






st.write("""
Search for stocks and build your own plot to compare them!
""")

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

df_daily_5_yr['timestamp'] = pd.to_datetime(df_daily_5_yr['timestamp'])

# Create ticker/name lookup table
stock_lookup = (
    df_daily_5_yr[['ticker', 'name']]
    .drop_duplicates()
    .sort_values('ticker')
)

stock_lookup['display_name'] = (
    stock_lookup['ticker'] + ' (' + stock_lookup['name'].fillna('Unknown') + ')'
)

display_to_ticker = dict(zip(stock_lookup['display_name'], stock_lookup['ticker']))


default_selection = []

if 'AAPL' in stock_lookup['ticker'].values:
    default_selection = stock_lookup.loc[
        stock_lookup['ticker'] == 'AAPL',
        'display_name'
    ].tolist()

selected_display_names = st.multiselect(
    'Search for one or more stocks',
    options=stock_lookup['display_name'].tolist(),
    default=default_selection
)

selected_tickers = [display_to_ticker[x] for x in selected_display_names]

if len(selected_tickers) == 0:
    st.info('Choose at least one stock to generate the plot.')
    st.stop()

plot_df = df_daily_5_yr[df_daily_5_yr['ticker'].isin(selected_tickers)]

fig, ax = plt.subplots(figsize=(12, 8))

for ticker in selected_tickers:
    stock_df = plot_df[plot_df['ticker'] == ticker].sort_values('timestamp')

    display_label = stock_lookup.loc[
        stock_lookup['ticker'] == ticker,
        'display_name'
    ].iloc[0]

    ax.plot(stock_df['timestamp'], stock_df['close'], label=display_label)

ax.set_xlabel('Date')
ax.set_ylabel('Closing Price')
ax.set_title('Stock prices over five years')
ax.xaxis.set_major_locator(mdates.MonthLocator(interval=3))
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m'))

plt.xticks(rotation=45)
ax.grid()
ax.legend()

st.pyplot(fig)







st.title("Seven Tech Stocks")
st.write("""
We will run comparisons with seven major technology stocks: AAPL, AMZN, GOOGL, META, MSFT, NFLX, and NVDA.
""")



st.write("""
    1. Relative changes for seven tech stocks over a 5 year span. Each stock is measured by its own value relative to the first day of the dataset.
""")





# Five year span
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

tech_stocks = ['AMZN', 'AAPL', 'GOOGL', 'META', 'MSFT', 'NFLX', 'NVDA']

master_df = df_daily_5_yr

#plt.figure(figsize=(14, 7))
fig, ax = plt.subplots(figsize=(14, 7))


for stock in tech_stocks:
    stock_df = master_df[master_df['ticker'] == stock]
    plt.plot(stock_df['timestamp'], stock_df['close_pct_of_day1'], label=stock)
    ax.set_xlabel('Date')
    ax.set_ylabel('Closing Price')
    ax.set_title(
    f'Relative price changes for seven stocks over a five year span\n'
    f'{(master_df['timestamp'].min()):%Y/%m/%d} = 100%')
    plt.legend()

# plt.gca().xaxis.set_major_locator(mdates.MonthLocator(interval=3))
# plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m'))
ax.xaxis.set_major_locator(mdates.MonthLocator(interval=3))
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m'))


plt.xticks(rotation=45)
ax.grid()
st.pyplot(fig)
