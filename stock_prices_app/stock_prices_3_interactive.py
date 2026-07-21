import streamlit as st
import pandas as pd

from pathlib import Path

CURRENT_DIR = Path(__file__).resolve().parent
COMMAND_FILE = CURRENT_DIR / "COMMAND_load_merge_transform.txt"

with open(COMMAND_FILE, "r") as file:
    command = file.read()

exec(command)




st.title("""Build your own!""")
st.write("""
Search for stocks and build your own plot to see their price changes! The graph may take a moment to load.
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


import random

# Initialize session state
if 'selected_stocks' not in st.session_state:
    st.session_state.selected_stocks = default_selection

# Randomize button
if st.button('🎲 Choose 5 random stocks'):
    st.session_state.selected_stocks = random.sample(
        stock_lookup['display_name'].tolist(),
        min(5, len(stock_lookup))
    )

selected_display_names = st.multiselect(
    'Search for one or more stocks',
    options=stock_lookup['display_name'].tolist(),
    default=st.session_state.selected_stocks,
    key='stock_selector'
)

st.session_state.selected_stocks = selected_display_names

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