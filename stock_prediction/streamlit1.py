import streamlit as st


st.set_page_config(page_title="Stock Trends", page_icon="📈", layout="centered")

st.title("Stock Data")
st.write("""
I downloaded five years of stock data (2021-05-24 to 2026-05-21). The dataset features 2784 NASADQ and NYSE stocks with 1255 trading days for each. 
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


# =========================================================
# =========================================================
# =========================================================
# =========================================================



st.title("Our first example")
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
Now we will add SMAs (simple moving averages). You may notice that the SMA lines do not start immediately. This is due to there being insufficient days to calculate them. For example, SMA100 does not exist on day 79 because 100 days have not yet passed. As each SMA begins, you can still see how the previous days are influencing it. The longer the SMA, the smoother the line.
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



# =========================================================
# =========================================================
# =========================================================
# =========================================================



st.title("Seven Tech Stocks")
st.write("""
We will run comparisons with seven major technology stocks: AAPL, AMZN, GOOGL, META, MSFT, NFLX, and NVDA.
""")



st.write("""
    1. Relative changes for seven tech stocks over a 5 year span. Each stock is measured by its own value relative to the first day of the dataset; therefore, each stock starts in the same place.
""")


# Five year span - Relative price comparison
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


# =========================================================
# =========================================================
# =========================================================
# =========================================================



# Positive change probability after threshold change
st.write("""
2. What is the probability that each of these stocks will see a positive move after a previous positive change over a given threshold?
""")

ticker_list = ['AAPL', 'NVDA', 'NFLX', 'AMZN', 'GOOGL', 'META', 'MSFT']

thresholds = 2, 3, 4, 5, 6, 10, 20

master_df = df_daily_5_yr

results = []

for ticker in ticker_list:
    ticker_df = master_df[master_df['ticker'] == ticker]

    for threshold in thresholds:
        prev_change_condition = ticker_df['pct_change_from_prev'] >= threshold
        next_change_condition = ticker_df['next_close_pct_change'] >= 0

        full_condition = prev_change_condition & next_change_condition

        days_w_both_conditions = full_condition.sum()
        days_with_growth_threshold = prev_change_condition.sum()

        if days_with_growth_threshold > 0:
            pos_change_prob = (
                days_w_both_conditions / days_with_growth_threshold
            ) * 100
        else:
            pos_change_prob = None

        results.append({
            'ticker': ticker,
            'increase_threshold': threshold,
            'pos_change_prob': pos_change_prob,
            'days_with_growth_threshold': days_with_growth_threshold,
            'days_w_both_conditions': days_w_both_conditions
        })

change_threshold_df = pd.DataFrame(results)

st.dataframe(change_threshold_df)


# =========================================================
# =========================================================
# =========================================================
# =========================================================




# Create new dataset in preparation
super_safe_df = df_daily_5_yr.copy()

pos_mask = super_safe_df['pct_change_from_prev'] >= 0
streak_id = (pos_mask != pos_mask.shift()).cumsum()
super_safe_df['positive_day_streak'] = super_safe_df.groupby(streak_id).cumcount() + 1
super_safe_df.loc[~pos_mask, 'positive_day_streak'] = 0

neg_mask = super_safe_df['pct_change_from_prev'] < 0
streak_id = (neg_mask != neg_mask.shift()).cumsum()
super_safe_df['negative_day_streak'] = super_safe_df.groupby(streak_id).cumcount() + 1
super_safe_df.loc[~neg_mask, 'negative_day_streak'] = 0

super_safe_df.head(10)




# Positive change probability after consecutive positive days
st.write("""
3. What is the probability that each stock will see a positive move after a given number of consecutive positive days?
""")

ticker_list = ['AAPL', 'NVDA', 'NFLX', 'AMZN', 'GOOGL', 'META', 'MSFT']

thresholds = 2, 3, 4, 5, 6, 10, 20

master_df = super_safe_df

results = []

for ticker in ticker_list:
    ticker_df = master_df[master_df['ticker'] == ticker]

    for threshold in thresholds:
        prev_change_condition = ticker_df['pct_change_from_prev'] >= threshold
        next_change_condition = ticker_df['next_close_pct_change'] >= 0

        full_condition = prev_change_condition & next_change_condition

        days_w_both_conditions = full_condition.sum()
        days_with_consec_threshold = prev_change_condition.sum()

        if days_with_consec_threshold > 0:
            pos_change_prob = (
                days_w_both_conditions / days_with_consec_threshold
            ) * 100
        else:
            pos_change_prob = None

        results.append({
            'ticker': ticker,
            'consec_days_threshold': threshold,
            'pos_change_prob': pos_change_prob,
            'days_with_consec_threshold': days_with_consec_threshold,
            'days_w_both_conditions': days_w_both_conditions
        })

consec_threshold_df = pd.DataFrame(results)

st.dataframe(consec_threshold_df)



# =========================================================
# =========================================================
# =========================================================
# =========================================================



# Calculate aggregates from the entire dataset

df_daily_five_yr_agg = df_daily_5_yr.copy()

df_daily_five_yr_agg = df_daily_5_yr.sort_values(['ticker', 'timestamp']).copy()

df_daily_five_yr_agg['avg_daily_return'] = df_daily_five_yr_agg.groupby('ticker')['pct_change_from_prev'].transform('mean')

df_daily_five_yr_agg['avg_volume'] = df_daily_five_yr_agg.groupby('ticker')['volume'].transform('mean')

df_daily_five_yr_agg['avg_abs_daily_pct_change'] = (
    df_daily_five_yr_agg['pct_change_from_prev']
    .abs()
    .groupby(df_daily_five_yr_agg['ticker'])
    .transform('mean')
)

df_daily_five_yr_agg['change_begin_to_end'] = (
    df_daily_five_yr_agg.groupby('ticker')['close']
    .transform(lambda x: (x.iloc[-1] - x.iloc[0]) / x.iloc[0] * 100)
)

# df_daily_five_yr_agg['CBTE_vs_market_avg'] = df_daily_five_yr_agg['change_begin_to_end'] - ((df_daily_five_yr_agg['change_begin_to_end']).mean())

market_avg_cbte = (
    df_daily_five_yr_agg[['ticker', 'change_begin_to_end']]
    .drop_duplicates()
    ['change_begin_to_end']
    .mean()
)

df_daily_five_yr_agg['CBTE_vs_market_avg'] = (
    df_daily_five_yr_agg['change_begin_to_end'] - market_avg_cbte
)

df_daily_five_yr_agg['std_dev_daily_return'] = df_daily_five_yr_agg.groupby('ticker')['pct_change_from_prev'].transform('std')

# df_daily_five_yr_agg['wheel_spinner_score'] = df_daily_five_yr_agg['avg_abs_daily_pct_change'] / df_daily_five_yr_agg['change_begin_to_end']

# df_daily_five_yr_agg['wheel_spinner_score'] = (
#     df_daily_five_yr_agg['avg_abs_daily_pct_change'] 
#     / df_daily_five_yr_agg['change_begin_to_end'].abs()
# )

df_daily_five_yr_agg['pct_days_positive'] = (
    df_daily_five_yr_agg.groupby('ticker')['pct_change_from_prev']
    .transform(lambda x: (x > 0).mean() * 100)
)

df_daily_five_yr_agg['wheel_spinner_score'] = df_daily_five_yr_agg['avg_abs_daily_pct_change'] / (abs(df_daily_five_yr_agg['change_begin_to_end']) ** 1.5) 

# df_daily_five_yr_agg['daily_return_vs_market_avg'] = df_daily_five_yr_agg.groupby('ticker')['NCPC_vs_market_avg'].transform('mean')

df_daily_five_yr_agg = (
    df_daily_five_yr_agg[
        [
            'ticker',
            'name',
            'avg_daily_return',
            'avg_volume',
            'avg_abs_daily_pct_change',
            'change_begin_to_end',
            'CBTE_vs_market_avg',
            #'daily_return_vs_market_avg',
            'std_dev_daily_return',
            'wheel_spinner_score',
            'pct_days_positive'
        ]
    ]
    .drop_duplicates()
    .reset_index(drop=True)
)


# Reduce the aggregates to seven tech stocks
tech_stocks = ['AMZN', 'AAPL', 'GOOGL', 'META', 'MSFT', 'NFLX', 'NVDA']
tech_stock_agg = df_daily_five_yr_agg[df_daily_five_yr_agg['ticker'].isin(tech_stocks)]
#tech_stock_agg


# Collinearity

st.write("""
4. To what extent are our tech stocks collinear with each other, and how does this differ from the dataset as a whole? 
""")

import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st

corr_df = tech_stock_agg.corr(numeric_only=True)

mask = np.zeros_like(corr_df, dtype=bool)
mask[np.triu_indices_from(mask)] = True

fig, ax = plt.subplots(figsize=(18, 18))

sns.heatmap(
    corr_df,
    mask=mask,
    cmap="coolwarm",
    vmax=1,
    center=0,
    square=True,
    linewidths=0.5,
    cbar_kws={"shrink": 0.5},
    annot=True,
    ax=ax
)

ax.set_title(
    "Correlation heatmap for seven tech stocks",
    fontsize=24,
    fontweight="bold",
    pad=20
)

st.pyplot(fig)





import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st

corr_df = df_daily_five_yr_agg.corr(numeric_only=True)

mask = np.zeros_like(corr_df, dtype=bool)
mask[np.triu_indices_from(mask)] = True

fig, ax = plt.subplots(figsize=(18, 18))

sns.heatmap(
    corr_df,
    mask=mask,
    cmap="coolwarm",
    vmax=1,
    center=0,
    square=True,
    linewidths=0.5,
    cbar_kws={"shrink": 0.5},
    annot=True,
    ax=ax
)

ax.set_title(
    "Correlation heatmap for all stocks",
    fontsize=24,
    fontweight="bold",
    pad=20
)

st.pyplot(fig)










# import numpy as np
# import seaborn as sns

# #sns.set(style="whitegrid")

# # Generate a mask for the upper triangle
# mask = np.zeros_like(df_daily_five_yr_agg.corr(numeric_only = True), dtype=bool)
# mask[np.triu_indices_from(mask)] = True

# # Set up the matplotlib figure
# f, ax = plt.subplots(figsize=(18, 18))

# # Draw the heatmap with the mask and correct aspect ratio
# sns.heatmap(df_daily_five_yr_agg.corr(numeric_only = True), mask=mask, cmap='coolwarm', vmax=1, center=0,
#             square=True, linewidths=.5, cbar_kws={"shrink": .5}, annot=True)

# plt.title("Correlation heatmap for all stocks", fontsize=25, fontweight='bold')
# #plt.savefig("name.png")
# plt.show()






# =========================================================
# =========================================================
# =========================================================
# =========================================================


st.title("""Build your own!""")
st.write("""
Search for stocks and build your own plot to see their price changes!
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
if st.button('🎲 Random 5 Stocks'):
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

# =====

# ====

# SAFE VERSION WORKED (no randomizer)

# st.title("""Build your own!""")
# st.write("""
# Search for stocks and build your own plot to see their price changes!
# """)

# import streamlit as st
# import pandas as pd
# import matplotlib.pyplot as plt
# import matplotlib.dates as mdates

# df_daily_5_yr['timestamp'] = pd.to_datetime(df_daily_5_yr['timestamp'])

# # Create ticker/name lookup table
# stock_lookup = (
#     df_daily_5_yr[['ticker', 'name']]
#     .drop_duplicates()
#     .sort_values('ticker')
# )

# stock_lookup['display_name'] = (
#     stock_lookup['ticker'] + ' (' + stock_lookup['name'].fillna('Unknown') + ')'
# )

# display_to_ticker = dict(zip(stock_lookup['display_name'], stock_lookup['ticker']))


# default_selection = []

# if 'AAPL' in stock_lookup['ticker'].values:
#     default_selection = stock_lookup.loc[
#         stock_lookup['ticker'] == 'AAPL',
#         'display_name'
#     ].tolist()

# selected_display_names = st.multiselect(
#     'Search for one or more stocks',
#     options=stock_lookup['display_name'].tolist(),
#     default=default_selection
# )

# selected_tickers = [display_to_ticker[x] for x in selected_display_names]

# if len(selected_tickers) == 0:
#     st.info('Choose at least one stock to generate the plot.')
#     st.stop()

# plot_df = df_daily_5_yr[df_daily_5_yr['ticker'].isin(selected_tickers)]

# fig, ax = plt.subplots(figsize=(12, 8))

# for ticker in selected_tickers:
#     stock_df = plot_df[plot_df['ticker'] == ticker].sort_values('timestamp')

#     display_label = stock_lookup.loc[
#         stock_lookup['ticker'] == ticker,
#         'display_name'
#     ].iloc[0]

#     ax.plot(stock_df['timestamp'], stock_df['close'], label=display_label)

# ax.set_xlabel('Date')
# ax.set_ylabel('Closing Price')
# ax.set_title('Stock prices over five years')
# ax.xaxis.set_major_locator(mdates.MonthLocator(interval=3))
# ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m'))

# plt.xticks(rotation=45)
# ax.grid()
# ax.legend()

# st.pyplot(fig)
