import streamlit as st


# OPTIONS
# Split into separate dataframes
# Or
# Call from database as needed




#st.set_page_config(page_title="Stock Trends", page_icon="📈", layout="centered")

st.title("Stock Data")
st.write("""
I downloaded five years of daily stock data (2021-05-24 to 2026-05-21) from the Massive.com (formerly Polygon.io) API. After deleting any stocks with nulls or missing days, the dataset stands at 2784 NASADQ and NYSE stocks with 1255 trading days for each. 
""")

st.title("Why do some analyses not go back as far?")
st.write("""
Some rows had nulls for certain metrics. This is the result of certain time-series metrics having insufficient days to calculate them. For example, SMA100 (a moving average of the previous 100 closing prices per stock) does not exist on day 99. I handled this by creating two versions of the dataset - one which retains these nulls, and one which drops them.

For shorter versions of the dataset, such as the one-year and two-year segments, the column 'close_pct_of_day1' had to be calculated as the tables were created.

""")




import pandas as pd

from pathlib import Path

# Directory containing this Python file
APP_DIR = Path(__file__).resolve().parent

# Load the command script
with open(APP_DIR / "COMMAND_load_merge_transform.txt", "r") as file:
    command = file.read()

# Execute the command script
exec(command)



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

# 1 - Apple raw pric es
st.title("Our first example")
st.write("""
Let's see AAPL's stock price over five years. 
""")


from pathlib import Path
from PIL import Image

img1 = Image.open('v01_aapl_price.png')
st.image(img1)


# 2 - Apple prices plus SMAs
st.write("""
Now we will add SMAs (simple moving averages). You may notice that the SMA lines do not start immediately. This is due to there being insufficient days to calculate them. For example, SMA100 does not exist on day 79 because 100 days have not yet passed. As each SMA begins, you can still see how the previous days are influencing it. The longer the SMA, the smoother the line.
""")

img2 = Image.open('v02_appl_with_smas.png')
st.image(img2)


# 3 - Tech stocks raw prices
st.title("Seven Tech Stocks")
st.write("""
We will run comparisons with seven major technology stocks: AAPL, AMZN, GOOGL, META, MSFT, NFLX, and NVDA.
""")


st.write("""
    1. Relative changes for seven tech stocks over one-year and five-year spans. Each stock is measured by its own value relative to the first day of the dataset; therefore, each stock starts in the same place.
""")

img3 = Image.open('v03_tech_absolute.png')
st.image(img3)

img4 = Image.open('v04_tech_relative_1yr.png')
st.image(img4)

img5 = Image.open('v05_tech_relative_5yr.png')
st.image(img5)

img6 = Image.open('v06_pos_prob_after_pct_pos.png')
st.image(img6)

img7 = Image.open('v07_neg_prob_after_pct_neg.png')
st.image(img7)

st.write("""
Skipping 8 and 9 for time for now
""")


img10 = Image.open('v10_correlation_all.png')
st.image(img10)


img11 = Image.open('v11_correlation_tech.png')
st.image(img11)

st.write("""
I'll get back to 12 and 13 later
""")


img14 = Image.open('v14_overall_improvement_top10.png')
st.image(img14)

img15 = Image.open('v15_overall_improvement_top10_marcap.png')
st.image(img15)


st.title("=================")
st.title("ALL SAFE BELOW HERE")
st.title("=================")

# =========================================================
# =========================================================
# =========================================================
# =========================================================
# =========================================================
# =========================================================
# =========================================================
# =========================================================
# =========================================================
# =========================================================
# =========================================================
# =========================================================
# =========================================================
# =========================================================
# =========================================================
# =========================================================

# st.title("=================")
# st.title("ALL SAFE BELOW HERE")
# st.title("=================")
# st.title("Our first example")
# st.write("""
# Let's see AAPL's stock price over five years. 
# """)

# # AAPL with SMAs

# import streamlit as st
# import matplotlib.pyplot as plt
# import matplotlib.dates as mdates

# aapl_df = df_daily_5_yr[df_daily_5_yr['ticker'] == 'AAPL']

# # -------------------------
# # FIRST CHART
# # -------------------------

# fig1, ax1 = plt.subplots(figsize=(12, 8))

# aapl_df.set_index('timestamp')['close'].plot(ax=ax1)

# ax1.set_xlabel('Date')
# ax1.set_title('AAPL stock price over five years')

# ax1.xaxis.set_major_locator(mdates.MonthLocator(interval=3))
# ax1.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m'))

# plt.setp(ax1.get_xticklabels(), rotation=45)

# ax1.grid()

# st.pyplot(fig1)

# # -------------------------
# # SECOND CHART (SMAs)
# # -------------------------

# st.write("""
# Now we will add SMAs (simple moving averages). You may notice that the SMA lines do not start immediately. This is due to there being insufficient days to calculate them. For example, SMA100 does not exist on day 79 because 100 days have not yet passed. As each SMA begins, you can still see how the previous days are influencing it. The longer the SMA, the smoother the line.
# """)


# features_to_plot = ['close', 'SMA20', 'SMA50', 'SMA100']

# fig2, ax2 = plt.subplots(figsize=(12, 8))

# for feature in features_to_plot:
#     aapl_df.set_index('timestamp')[feature].plot(
#         ax=ax2,
#         label=feature
#     )

# ax2.set_xlabel('Date')
# ax2.set_title('AAPL stock price with Simple Moving Averages')

# ax2.xaxis.set_major_locator(mdates.MonthLocator(interval=3))
# ax2.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m'))

# plt.setp(ax2.get_xticklabels(), rotation=45)

# ax2.legend()
# ax2.grid()

# st.pyplot(fig2)



# # =========================================================
# # =========================================================
# # =========================================================
# # =========================================================



# st.title("Seven Tech Stocks")
# st.write("""
# We will run comparisons with seven major technology stocks: AAPL, AMZN, GOOGL, META, MSFT, NFLX, and NVDA.
# """)



# st.write("""
#     1. Relative changes for seven tech stocks over one-year and five-year spans. Each stock is measured by its own value relative to the first day of the dataset; therefore, each stock starts in the same place.
# """)


# # One year span - Relative price comparison
# import matplotlib.pyplot as plt
# import matplotlib.dates as mdates

# tech_stocks = ['AMZN', 'AAPL', 'GOOGL', 'META', 'MSFT', 'NFLX', 'NVDA']

# master_df = df_daily_1_yr

# #plt.figure(figsize=(14, 7))
# fig, ax = plt.subplots(figsize=(14, 7))


# # for stock in tech_stocks:
# #     stock_df = master_df[master_df['ticker'] == stock]
# #     plt.plot(stock_df['timestamp'], stock_df['close_pct_of_day1'], label=stock)
# #     ax.set_xlabel('Date')
# #     ax.set_ylabel('Closing Price')
# #     ax.set_title(
# #     f'Relative price changes for seven stocks over a one year span\n'
# #     f'{(master_df['timestamp'].min()):%Y/%m/%d} = 100')
# #     plt.legend()


# for stock in tech_stocks:
#     stock_df = master_df[master_df['ticker'] == stock]
#     plt.plot(stock_df['timestamp'], stock_df['close_pct_of_day1'], label=stock)
#     ax.set_xlabel('Date')
#     ax.set_ylabel('Closing Price')
#     ax.set_title(
#         f'Relative price changes for seven stocks over a one year span\n'
#         f"{master_df['timestamp'].min():%Y/%m/%d} = 100"
# )
# plt.legend()



# # plt.gca().xaxis.set_major_locator(mdates.MonthLocator(interval=3))
# # plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m'))
# ax.xaxis.set_major_locator(mdates.MonthLocator(interval=3))
# ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m'))


# plt.xticks(rotation=45)
# ax.grid()
# st.pyplot(fig)




# # Five year span - Relative price comparison
# import matplotlib.pyplot as plt
# import matplotlib.dates as mdates

# tech_stocks = ['AMZN', 'AAPL', 'GOOGL', 'META', 'MSFT', 'NFLX', 'NVDA']

# master_df = df_daily_5_yr

# #plt.figure(figsize=(14, 7))
# fig, ax = plt.subplots(figsize=(14, 7))


# # this version failed
# # for stock in tech_stocks:
# #     stock_df = master_df[master_df['ticker'] == stock]
# #     plt.plot(stock_df['timestamp'], stock_df['close_pct_of_day1'], label=stock)
# #     ax.set_xlabel('Date')
# #     ax.set_ylabel('Closing Price')
# #     ax.set_title(
# #     f'Relative price changes for seven stocks over a five year span\n'
# #     f'{(master_df['timestamp'].min()):%Y/%m/%d} = 100')
# #     plt.legend()


# # trying same fix that worked before
# for stock in tech_stocks:
#     stock_df = master_df[master_df['ticker'] == stock]
#     plt.plot(stock_df['timestamp'], stock_df['close_pct_of_day1'], label=stock)
#     ax.set_xlabel('Date')
#     ax.set_ylabel('Closing Price')
#     ax.set_title(
#         f'Relative price changes for seven stocks over a five year span\n'
#         f"{master_df['timestamp'].min():%Y/%m/%d} = 100"
# )
#     ax.legend()
# # plt.gca().xaxis.set_major_locator(mdates.MonthLocator(interval=3))
# # plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m'))
# ax.xaxis.set_major_locator(mdates.MonthLocator(interval=3))
# ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m'))


# plt.xticks(rotation=45)
# ax.grid()
# st.pyplot(fig)


# # =========================================================
# # =========================================================
# # =========================================================
# # =========================================================



# # Positive change probability after threshold change
# st.write("""
# 2a. What is the probability that each of these stocks will see a positive move after a previous positive change over a given threshold?
# """)

# ticker_list = ['AAPL', 'NVDA', 'NFLX', 'AMZN', 'GOOGL', 'META', 'MSFT']

# thresholds = 2, 3, 4, 5, 6, 10, 20

# master_df = df_daily_5_yr

# results = []

# for ticker in ticker_list:
#     ticker_df = master_df[master_df['ticker'] == ticker]

#     for threshold in thresholds:
#         prev_change_condition = ticker_df['pct_change_from_prev'] >= threshold
#         next_change_condition = ticker_df['next_close_pct_change'] >= 0

#         full_condition = prev_change_condition & next_change_condition

#         days_w_both_conditions = full_condition.sum()
#         days_with_growth_threshold = prev_change_condition.sum()

#         if days_with_growth_threshold > 0:
#             pos_change_prob = (
#                 days_w_both_conditions / days_with_growth_threshold
#             ) * 100
#         else:
#             pos_change_prob = None

#         results.append({
#             'ticker': ticker,
#             'pct_increase_threshold': threshold,
#             'pos_change_prob': pos_change_prob,
#             'days_with_growth_threshold': days_with_growth_threshold,
#             'days_w_both_conditions': days_w_both_conditions
#         })

# change_threshold_df = pd.DataFrame(results)

# st.dataframe(change_threshold_df)


# # =========================================================
# # =========================================================
# # =========================================================
# # =========================================================


# # Negative change probability after threshold change
# st.write("""
# 2b. What is the probability that each of these stocks will see a negative move after a previous negative change over a given threshold?
# """)

# ticker_list = ['AAPL', 'NVDA', 'NFLX', 'AMZN', 'GOOGL', 'META', 'MSFT']

# thresholds = 2, 3, 4, 5, 6, 10, 20

# master_df = df_daily_5_yr

# results = []

# for ticker in ticker_list:
#     ticker_df = master_df[master_df['ticker'] == ticker]

#     for threshold in thresholds:
#         prev_change_condition = ticker_df['pct_change_from_prev'] <= threshold
#         next_change_condition = ticker_df['next_close_pct_change'] < 0

#         full_condition = prev_change_condition & next_change_condition

#         days_w_both_conditions = full_condition.sum()
#         days_with_growth_threshold = prev_change_condition.sum()

#         if days_with_growth_threshold > 0:
#             pos_change_prob = (
#                 days_w_both_conditions / days_with_growth_threshold
#             ) * 100
#         else:
#             pos_change_prob = None

#         results.append({
#             'ticker': ticker,
#             'pct_decrease_threshold': threshold,
#             'pos_change_prob': pos_change_prob,
#             'days_with_growth_threshold': days_with_growth_threshold,
#             'days_w_both_conditions': days_w_both_conditions
#         })

# change_threshold_df = pd.DataFrame(results)

# st.dataframe(change_threshold_df)




# # =========================================================
# # =========================================================
# # =========================================================
# # =========================================================




# # Create new dataset in preparation
# super_safe_df = df_daily_5_yr.copy()

# pos_mask = super_safe_df['pct_change_from_prev'] >= 0
# streak_id = (pos_mask != pos_mask.shift()).cumsum()
# super_safe_df['positive_day_streak'] = super_safe_df.groupby(streak_id).cumcount() + 1
# super_safe_df.loc[~pos_mask, 'positive_day_streak'] = 0

# neg_mask = super_safe_df['pct_change_from_prev'] < 0
# streak_id = (neg_mask != neg_mask.shift()).cumsum()
# super_safe_df['negative_day_streak'] = super_safe_df.groupby(streak_id).cumcount() + 1
# super_safe_df.loc[~neg_mask, 'negative_day_streak'] = 0

# super_safe_df.head(10)




# # Positive change probability after consecutive positive days
# st.write("""
# 3a. What is the probability that each stock will see a positive move after a given number of consecutive positive days?
# """)

# ticker_list = ['AAPL', 'NVDA', 'NFLX', 'AMZN', 'GOOGL', 'META', 'MSFT']

# thresholds = 2, 3, 4, 5, 6, 10, 20

# master_df = super_safe_df

# results = []

# for ticker in ticker_list:
#     ticker_df = master_df[master_df['ticker'] == ticker]

#     for threshold in thresholds:
#         prev_change_condition = ticker_df['pct_change_from_prev'] >= threshold
#         next_change_condition = ticker_df['next_close_pct_change'] >= 0

#         full_condition = prev_change_condition & next_change_condition

#         days_w_both_conditions = full_condition.sum()
#         days_with_consec_threshold = prev_change_condition.sum()

#         if days_with_consec_threshold > 0:
#             pos_change_prob = (
#                 days_w_both_conditions / days_with_consec_threshold
#             ) * 100
#         else:
#             pos_change_prob = None

#         results.append({
#             'ticker': ticker,
#             'consec_days_threshold': threshold,
#             'pos_change_prob': pos_change_prob,
#             'days_with_consec_threshold': days_with_consec_threshold,
#             'days_w_both_conditions': days_w_both_conditions
#         })

# consec_threshold_df = pd.DataFrame(results)

# st.dataframe(consec_threshold_df)



# # =========================================================
# # =========================================================
# # =========================================================
# # =========================================================


# st.write("""
# This table was as far as I got previously. 
# """)


# # Positive change probability after consecutive positive days
# st.write("""
# 3b. What is the probability that each stock will see a negative move after a given number of consecutive negative days?
# """)

# ticker_list = ['AAPL', 'NVDA', 'NFLX', 'AMZN', 'GOOGL', 'META', 'MSFT']

# thresholds = 2, 3, 4, 5, 6, 10, 20

# master_df = super_safe_df

# results = []

# for ticker in ticker_list:
#     ticker_df = master_df[master_df['ticker'] == ticker]

#     for threshold in thresholds:
#         prev_change_condition = ticker_df['pct_change_from_prev'] <= threshold
#         next_change_condition = ticker_df['next_close_pct_change'] < 0

#         full_condition = prev_change_condition & next_change_condition

#         days_w_both_conditions = full_condition.sum()
#         days_with_consec_threshold = prev_change_condition.sum()

#         if days_with_consec_threshold > 0:
#             pos_change_prob = (
#                 days_w_both_conditions / days_with_consec_threshold
#             ) * 100
#         else:
#             pos_change_prob = None

#         results.append({
#             'ticker': ticker,
#             'consec_days_threshold': threshold,
#             'pos_change_prob': pos_change_prob,
#             'days_with_consec_threshold': days_with_consec_threshold,
#             'days_w_both_conditions': days_w_both_conditions
#         })

# consec_threshold_df = pd.DataFrame(results)

# st.dataframe(consec_threshold_df)



# st.write("""
# Previous table was as far as i got on previous versions. 
# """)



# # =========================================================
# # =========================================================
# # =========================================================
# # =========================================================




# # =========================================================
# # =========================================================
# # =========================================================
# # =========================================================


# # # Calculate aggregates from the entire dataset

# # df_daily_five_yr_agg = df_daily_5_yr.copy()

# # df_daily_five_yr_agg = df_daily_5_yr.sort_values(['ticker', 'timestamp']).copy()

# # df_daily_five_yr_agg['avg_daily_return'] = df_daily_five_yr_agg.groupby('ticker')['pct_change_from_prev'].transform('mean')

# # df_daily_five_yr_agg['avg_volume'] = df_daily_five_yr_agg.groupby('ticker')['volume'].transform('mean')

# # df_daily_five_yr_agg['avg_abs_daily_pct_change'] = (
# #     df_daily_five_yr_agg['pct_change_from_prev']
# #     .abs()
# #     .groupby(df_daily_five_yr_agg['ticker'])
# #     .transform('mean')
# # )

# # df_daily_five_yr_agg['change_begin_to_end'] = (
# #     df_daily_five_yr_agg.groupby('ticker')['close']
# #     .transform(lambda x: (x.iloc[-1] - x.iloc[0]) / x.iloc[0] * 100)
# # )

# # # df_daily_five_yr_agg['CBTE_vs_market_avg'] = df_daily_five_yr_agg['change_begin_to_end'] - ((df_daily_five_yr_agg['change_begin_to_end']).mean())

# # market_avg_cbte = (
# #     df_daily_five_yr_agg[['ticker', 'change_begin_to_end']]
# #     .drop_duplicates()
# #     ['change_begin_to_end']
# #     .mean()
# # )

# # df_daily_five_yr_agg['CBTE_vs_market_avg'] = (
# #     df_daily_five_yr_agg['change_begin_to_end'] - market_avg_cbte
# # )

# # df_daily_five_yr_agg['std_dev_daily_return'] = df_daily_five_yr_agg.groupby('ticker')['pct_change_from_prev'].transform('std')

# # # df_daily_five_yr_agg['wheel_spinner_score'] = df_daily_five_yr_agg['avg_abs_daily_pct_change'] / df_daily_five_yr_agg['change_begin_to_end']

# # # df_daily_five_yr_agg['wheel_spinner_score'] = (
# # #     df_daily_five_yr_agg['avg_abs_daily_pct_change'] 
# # #     / df_daily_five_yr_agg['change_begin_to_end'].abs()
# # # )

# # df_daily_five_yr_agg['pct_days_positive'] = (
# #     df_daily_five_yr_agg.groupby('ticker')['pct_change_from_prev']
# #     .transform(lambda x: (x > 0).mean() * 100)
# # )

# # df_daily_five_yr_agg['wheel_spinner_score'] = df_daily_five_yr_agg['avg_abs_daily_pct_change'] / (abs(df_daily_five_yr_agg['change_begin_to_end']) ** 1.5) 

# # # df_daily_five_yr_agg['daily_return_vs_market_avg'] = df_daily_five_yr_agg.groupby('ticker')['NCPC_vs_market_avg'].transform('mean')

# # df_daily_five_yr_agg = (
# #     df_daily_five_yr_agg[
# #         [
# #             'ticker',
# #             'name',
# #             'avg_daily_return',
# #             'avg_volume',
# #             'avg_abs_daily_pct_change',
# #             'change_begin_to_end',
# #             'CBTE_vs_market_avg',
# #             #'daily_return_vs_market_avg',
# #             'std_dev_daily_return',
# #             'wheel_spinner_score',
# #             'pct_days_positive'
# #         ]
# #     ]
# #     .drop_duplicates()
# #     .reset_index(drop=True)
# # )


# # # Reduce the aggregates to seven tech stocks
# # tech_stocks = ['AMZN', 'AAPL', 'GOOGL', 'META', 'MSFT', 'NFLX', 'NVDA']
# # tech_stock_agg = df_daily_five_yr_agg[df_daily_five_yr_agg['ticker'].isin(tech_stocks)]
# # #tech_stock_agg


# # =========================================================
# # =========================================================
# # =========================================================
# # =========================================================





# # Collinearity

# st.write("""
# 4. COLLINEARITY 2 LOAD IMAGES DIRECTLY
# """)


# # LOAD IMAGES

# heatmap_path = APP_DIR / "Correlation heatmap for all stocks 2.png"

# # IMAGE LOADING (new)
# from pathlib import Path

# APP_DIR = Path(__file__).resolve().parent

# from PIL import Image

# img = Image.open(APP_DIR / "Correlation heatmap for all stocks 2.png")
# st.image(img)

# img = Image.open(APP_DIR / "Correlation heatmap for seven tech stocks 2.png")
# st.image(img)


# # # ==============
# # # OLD OLD OLD IMAGE LOADING
# # # ==============
# # from PIL import Image
# # img = Image.open('Correlation heatmap for all stocks 2.png')
# # st.image(img)


# # from PIL import Image
# # img = Image.open('Correlation heatmap for seven tech stocks 2.png')
# # st.image(img)



# # =========================================================
# # =========================================================
# # =========================================================
# # =========================================================


# # =========================================================
# # =========================================================
# # =========================================================
# # =========================================================


# # st.write("""
# # 4. To what extent are our tech stocks collinear with each other, and how does this differ from the dataset as a whole? 
# # """)

# # import numpy as np
# # import seaborn as sns
# # import matplotlib.pyplot as plt
# # import streamlit as st

# # corr_df = tech_stock_agg.corr(numeric_only=True)

# # mask = np.zeros_like(corr_df, dtype=bool)
# # mask[np.triu_indices_from(mask)] = True

# # fig, ax = plt.subplots(figsize=(18, 18))

# # sns.heatmap(
# #     corr_df,
# #     mask=mask,
# #     cmap="coolwarm",
# #     vmax=1,
# #     center=0,
# #     square=True,
# #     linewidths=0.5,
# #     cbar_kws={"shrink": 0.5},
# #     annot=True,
# #     ax=ax
# # )

# # ax.set_title(
# #     "Correlation heatmap for seven tech stocks",
# #     fontsize=24,
# #     fontweight="bold",
# #     pad=20
# # )

# # st.pyplot(fig)






# # import numpy as np
# # import seaborn as sns
# # import matplotlib.pyplot as plt
# # import streamlit as st

# # corr_df = df_daily_five_yr_agg.corr(numeric_only=True)

# # mask = np.zeros_like(corr_df, dtype=bool)
# # mask[np.triu_indices_from(mask)] = True

# # fig, ax = plt.subplots(figsize=(18, 18))

# # sns.heatmap(
# #     corr_df,
# #     mask=mask,
# #     cmap="coolwarm",
# #     vmax=1,
# #     center=0,
# #     square=True,
# #     linewidths=0.5,
# #     cbar_kws={"shrink": 0.5},
# #     annot=True,
# #     ax=ax
# # )

# # ax.set_title(
# #     "Correlation heatmap for all stocks",
# #     fontsize=24,
# #     fontweight="bold",
# #     pad=20
# # )

# # st.pyplot(fig)





# # =========================================================
# # =========================================================
# # =========================================================
# # =========================================================

# # =========================================================
# # =========================================================
# # =========================================================
# # =========================================================




# # import numpy as np
# # import seaborn as sns

# # #sns.set(style="whitegrid")

# # # Generate a mask for the upper triangle
# # mask = np.zeros_like(df_daily_five_yr_agg.corr(numeric_only = True), dtype=bool)
# # mask[np.triu_indices_from(mask)] = True

# # # Set up the matplotlib figure
# # f, ax = plt.subplots(figsize=(18, 18))

# # # Draw the heatmap with the mask and correct aspect ratio
# # sns.heatmap(df_daily_five_yr_agg.corr(numeric_only = True), mask=mask, cmap='coolwarm', vmax=1, center=0,
# #             square=True, linewidths=.5, cbar_kws={"shrink": .5}, annot=True)

# # plt.title("Correlation heatmap for all stocks", fontsize=25, fontweight='bold')
# # #plt.savefig("name.png")
# # plt.show()

# # =========================================================
# # =========================================================
# # =========================================================
# # =========================================================



# # # SAFE VERSION WORKED

# # st.title("""General statistics""")

# # st.write("""
# # What are the most trending stocks? Let's see which stocks increased the most over the entire dataset.
# # """)

# # st.write("""
# # SAFE VERSION WORKED
# # """)

# # import matplotlib.pyplot as plt
# # import matplotlib.dates as mdates

# # recent_day_df = df_daily_5_yr[df_daily_5_yr['timestamp'] == df_daily_5_yr['timestamp'].max()]
# # strongest_df = recent_day_df.nlargest(10, 'close_pct_of_day1')
# # plot_stocks = strongest_df['ticker'].unique().tolist()

# # master_df = df_daily_5_yr

# # plt.figure(figsize=(14, 7))

# # fig, ax = plt.subplots(figsize=(12, 8))

# # for stock in plot_stocks:
# #     stock_df = master_df[master_df['ticker'] == stock]
# #     plt.plot(stock_df['timestamp'], stock_df['close'], label=stock)
# #     plt.xlabel('Date')
# #     plt.ylabel('Closing Price')
# #     plt.title(
# #     f'Strongest trending stocks by percentage over a five-year span')
# #     #f'{(master_df['timestamp'].min()):%Y/%m/%d} = 100%')
# #     plt.legend()

# # # ax.gca().xaxis.set_major_locator(mdates.MonthLocator(interval=3))
# # # ax.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m'))

# # ax.xaxis.set_major_locator(mdates.MonthLocator(interval=3))
# # ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m'))


# # plt.xticks(rotation=45)
# # ax.grid()

# # st.pyplot(fig)

# # =========================================================
# # =========================================================
# # =========================================================
# # =========================================================

# # Legend test

# st.title("""General statistics""")




# # =========================================================
# # =========================================================
# # =========================================================
# # =========================================================

# st.write("""
# Let's see which stocks improved most on the last day of the dataset.
# """)

# recent_day_df = df_daily_5_yr[df_daily_5_yr['timestamp'] == df_daily_5_yr['timestamp'].max()]
# recent_day_df = recent_day_df[['timestamp', 'ticker', 'name', 'market_cap', 'close', 'pct_change_from_prev', 'close_pct_of_day1']]
# most_recent_impr = recent_day_df.nlargest(10, 'pct_change_from_prev')
# most_recent_impr.sort_values(by='pct_change_from_prev', ascending=False)
# most_recent_impr = most_recent_impr[['ticker', 'name', 'pct_change_from_prev', 'close']]
# st.dataframe(most_recent_impr)

# st.write("""
# Now we will repeat the same analysis, but with a minimum market capitalization of $5 billion.
# """)

# recent_day_df = df_daily_5_yr[df_daily_5_yr['timestamp'] == df_daily_5_yr['timestamp'].max()]
# recent_day_df = recent_day_df[['timestamp', 'ticker', 'name', 'market_cap', 'close', 'pct_change_from_prev', 'close_pct_of_day1']]

# marcap_df = recent_day_df[recent_day_df['market_cap'] >= 5000000000]
# most_recent_impr_marcap = marcap_df.nlargest(10, 'pct_change_from_prev')
# most_recent_impr_marcap.sort_values(by='pct_change_from_prev', ascending=False)
# most_recent_impr_marcap = most_recent_impr_marcap[['ticker', 'name', 'pct_change_from_prev', 'close']]
# st.dataframe(most_recent_impr_marcap)

# st.write("""
# The daily increases become much more subdued when applying the market cap filter. Absolute prices are also higher, which may be owed to these stocks being more established and thus less prone to wild daily swings.
# """)


# # =========================================================
# # =========================================================
# # =========================================================
# # =========================================================



# st.write("""
# Now let's see which stocks increased the most over the entire dataset. For this part, I rendered the data as visualizations.
# """)


# import matplotlib.pyplot as plt
# import matplotlib.dates as mdates

# recent_day_df = df_daily_5_yr[df_daily_5_yr['timestamp'] == df_daily_5_yr['timestamp'].max()]
# strongest_df = recent_day_df.nlargest(10, 'close_pct_of_day1')
# plot_stocks = strongest_df['ticker'].unique().tolist()

# master_df = df_daily_5_yr

# ticker_to_name = (
#     master_df[['ticker', 'name']]
#     .drop_duplicates()
#     .set_index('ticker')['name']
#     .to_dict()
# )

# plt.figure(figsize=(14, 7))

# fig, ax = plt.subplots(figsize=(12, 8))

# for stock in plot_stocks:
#     stock_df = master_df[master_df['ticker'] == stock]
    
#     plt.plot(
#         stock_df['timestamp'],
#         stock_df['close'],
#         label=f"{stock} ({ticker_to_name[stock]})"
#     )   
#     plt.xlabel('Date')
#     plt.ylabel('Closing Price')
#     plt.title(
#     f'Strongest trending stocks over a five-year span')
#     #f'{(master_df['timestamp'].min()):%Y/%m/%d} = 100%')
#     plt.legend()

# # ax.gca().xaxis.set_major_locator(mdates.MonthLocator(interval=3))
# # ax.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m'))

# ax.xaxis.set_major_locator(mdates.MonthLocator(interval=3))
# ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m'))


# plt.xticks(rotation=45)
# ax.grid()

# st.pyplot(fig)

# # =========================================================
# # =========================================================
# # =========================================================
# # =========================================================

# st.write("""
# Once again, let's apply the market cap filter.
# """)

# import matplotlib.pyplot as plt
# import matplotlib.dates as mdates

# recent_day_df = df_daily_5_yr[df_daily_5_yr['timestamp'] == df_daily_5_yr['timestamp'].max()]
# min_market_cap_df = recent_day_df[recent_day_df['market_cap'] >= 5000000000]
# strongest_df = min_market_cap_df.nlargest(10, 'close_pct_of_day1')
# plot_stocks = strongest_df['ticker'].unique().tolist()

# master_df = df_daily_5_yr

# ticker_to_name = (
#     master_df[['ticker', 'name']]
#     .drop_duplicates()
#     .set_index('ticker')['name']
#     .to_dict()
# )

# plt.figure(figsize=(14, 7))

# fig, ax = plt.subplots(figsize=(12, 8))

# for stock in plot_stocks:
#     stock_df = master_df[master_df['ticker'] == stock]
    
#     plt.plot(
#         stock_df['timestamp'],
#         stock_df['close'],
#         label=f"{stock} ({ticker_to_name[stock]})"
#     )   
#     plt.xlabel('Date')
#     plt.ylabel('Closing Price')
#     plt.title(
#     f'Strongest trending stocks over a five-year span\n(Minimum market cap $5 billion)')
#     #f'{(master_df['timestamp'].min()):%Y/%m/%d} = 100%')
#     plt.legend()

# # ax.gca().xaxis.set_major_locator(mdates.MonthLocator(interval=3))
# # ax.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m'))

# ax.xaxis.set_major_locator(mdates.MonthLocator(interval=3))
# ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m'))


# plt.xticks(rotation=45)
# ax.grid()

# st.pyplot(fig)





# # = most_recent_impr[most_recent_impr['market_cap'] >= 5000000000]
# # most_recent_impr_marcap.sort_values(by='pct_change_from_prev', ascending=False)
# # most_recent_impr_marcap = most_recent_impr_marcap[['ticker', 'name', 'pct_change_from_prev', 'close']]
# # st.dataframe(most_recent_impr_marcap)



# # =========================================================
# # =========================================================
# # =========================================================
# # =========================================================



# # st.title("""MADE SEPARATE PAGE FOR THIS, MAY DELETE FROM HERE""")


# # st.title("""Build your own!""")
# # st.write("""
# # Search for stocks and build your own plot to see their price changes! The graph may take a moment to load.
# # """)

# # import streamlit as st
# # import pandas as pd
# # import matplotlib.pyplot as plt
# # import matplotlib.dates as mdates

# # df_daily_5_yr['timestamp'] = pd.to_datetime(df_daily_5_yr['timestamp'])

# # # Create ticker/name lookup table
# # stock_lookup = (
# #     df_daily_5_yr[['ticker', 'name']]
# #     .drop_duplicates()
# #     .sort_values('ticker')
# # )

# # stock_lookup['display_name'] = (
# #     stock_lookup['ticker'] + ' (' + stock_lookup['name'].fillna('Unknown') + ')'
# # )

# # display_to_ticker = dict(zip(stock_lookup['display_name'], stock_lookup['ticker']))


# # default_selection = []

# # if 'AAPL' in stock_lookup['ticker'].values:
# #     default_selection = stock_lookup.loc[
# #         stock_lookup['ticker'] == 'AAPL',
# #         'display_name'
# #     ].tolist()


# # import random

# # # Initialize session state
# # if 'selected_stocks' not in st.session_state:
# #     st.session_state.selected_stocks = default_selection

# # # Randomize button
# # if st.button('🎲 Choose 5 random stocks'):
# #     st.session_state.selected_stocks = random.sample(
# #         stock_lookup['display_name'].tolist(),
# #         min(5, len(stock_lookup))
# #     )

# # selected_display_names = st.multiselect(
# #     'Search for one or more stocks',
# #     options=stock_lookup['display_name'].tolist(),
# #     default=st.session_state.selected_stocks,
# #     key='stock_selector'
# # )

# # st.session_state.selected_stocks = selected_display_names

# # selected_tickers = [display_to_ticker[x] for x in selected_display_names]

# # if len(selected_tickers) == 0:
# #     st.info('Choose at least one stock to generate the plot.')
# #     st.stop()

# # plot_df = df_daily_5_yr[df_daily_5_yr['ticker'].isin(selected_tickers)]

# # fig, ax = plt.subplots(figsize=(12, 8))

# # for ticker in selected_tickers:
# #     stock_df = plot_df[plot_df['ticker'] == ticker].sort_values('timestamp')

# #     display_label = stock_lookup.loc[
# #         stock_lookup['ticker'] == ticker,
# #         'display_name'
# #     ].iloc[0]

# #     ax.plot(stock_df['timestamp'], stock_df['close'], label=display_label)

# # ax.set_xlabel('Date')
# # ax.set_ylabel('Closing Price')
# # ax.set_title('Stock prices over five years')
# # ax.xaxis.set_major_locator(mdates.MonthLocator(interval=3))
# # ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m'))

# # plt.xticks(rotation=45)
# # ax.grid()
# # ax.legend()

# # st.pyplot(fig)










# # END END END
# # END END END
# # END END END
# # END END END
# # END END END
# # END END END
# # END END END
# # END END END
# # END END END
# # =====

# # ====

# # SAFE VERSION WORKED (no randomizer)

# # st.title("""Build your own!""")
# # st.write("""
# # Search for stocks and build your own plot to see their price changes!
# # """)

# # import streamlit as st
# # import pandas as pd
# # import matplotlib.pyplot as plt
# # import matplotlib.dates as mdates

# # df_daily_5_yr['timestamp'] = pd.to_datetime(df_daily_5_yr['timestamp'])

# # # Create ticker/name lookup table
# # stock_lookup = (
# #     df_daily_5_yr[['ticker', 'name']]
# #     .drop_duplicates()
# #     .sort_values('ticker')
# # )

# # stock_lookup['display_name'] = (
# #     stock_lookup['ticker'] + ' (' + stock_lookup['name'].fillna('Unknown') + ')'
# # )

# # display_to_ticker = dict(zip(stock_lookup['display_name'], stock_lookup['ticker']))


# # default_selection = []

# # if 'AAPL' in stock_lookup['ticker'].values:
# #     default_selection = stock_lookup.loc[
# #         stock_lookup['ticker'] == 'AAPL',
# #         'display_name'
# #     ].tolist()

# # selected_display_names = st.multiselect(
# #     'Search for one or more stocks',
# #     options=stock_lookup['display_name'].tolist(),
# #     default=default_selection
# # )

# # selected_tickers = [display_to_ticker[x] for x in selected_display_names]

# # if len(selected_tickers) == 0:
# #     st.info('Choose at least one stock to generate the plot.')
# #     st.stop()

# # plot_df = df_daily_5_yr[df_daily_5_yr['ticker'].isin(selected_tickers)]

# # fig, ax = plt.subplots(figsize=(12, 8))

# # for ticker in selected_tickers:
# #     stock_df = plot_df[plot_df['ticker'] == ticker].sort_values('timestamp')

# #     display_label = stock_lookup.loc[
# #         stock_lookup['ticker'] == ticker,
# #         'display_name'
# #     ].iloc[0]

# #     ax.plot(stock_df['timestamp'], stock_df['close'], label=display_label)

# # ax.set_xlabel('Date')
# # ax.set_ylabel('Closing Price')
# # ax.set_title('Stock prices over five years')
# # ax.xaxis.set_major_locator(mdates.MonthLocator(interval=3))
# # ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m'))

# # plt.xticks(rotation=45)
# # ax.grid()
# # ax.legend()

# # st.pyplot(fig)
