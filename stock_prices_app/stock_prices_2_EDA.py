import streamlit as st

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


# =========================================================
# =========================================================
# =========================================================
# =========================================================

# 1 - Apple raw prices
st.title("Our first example")
st.write("""
Let's see AAPL's stock price over five years. 
""")


from pathlib import Path
from PIL import Image

img1 = Image.open('visualizations/v01_aapl_price.png')
st.image(img1)


# 2 - Apple prices plus SMAs
st.write("""
Now we will add SMAs (simple moving averages). You may notice that the SMA lines do not start immediately. This is due to there being insufficient days to calculate them. For example, SMA100 does not exist on day 79 because 100 days have not yet passed. As each SMA begins, you can still see how the previous days are influencing it. The longer the SMA, the smoother the line.
""")

img2 = Image.open('visualizations/v02_appl_with_smas.png')
st.image(img2)


# 3 - Tech stocks raw prices
st.title("Seven Tech Stocks")
st.write("""
We will run comparisons with seven major technology stocks: AAPL, AMZN, GOOGL, META, MSFT, NFLX, and NVDA.
""")


st.write("""
    1. Relative changes for seven tech stocks over one-year and five-year spans. Each stock is measured by its own value relative to the first day of the dataset; therefore, each stock starts in the same place.
""")

img3 = Image.open('visualizations/v03_tech_absolute.png')
st.image(img3)

img4 = Image.open('visualizations/v04_tech_relative_1yr.png')
st.image(img4)

img5 = Image.open('visualizations/v05_tech_relative_5yr.png')
st.image(img5)

img6 = Image.open('visualizations/v06_pos_prob_after_pct_pos.png')
st.image(img6)

img7 = Image.open('visualizations/v07_neg_prob_after_pct_neg.png')
st.image(img7)

st.write("""
Skipping 8 and 9 for time for now
""")


img10 = Image.open('visualizations/v10_correlation_all.png')
st.image(img10)


img11 = Image.open('visualizations/v11_correlation_tech.png')
st.image(img11)

st.write("""
I'll get back to 12 and 13 later
""")


img14 = Image.open('visualizations/v14_overall_improvement_top10.png')
st.image(img14)

img15 = Image.open('visualizations/v15_overall_improvement_top10_marcap.png')
st.image(img15)

