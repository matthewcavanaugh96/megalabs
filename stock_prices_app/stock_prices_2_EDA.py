import streamlit as st

st.title("Stock Data")
st.write("""
I downloaded five years of daily stock data (2021-05-24 to 2026-05-21) from the Massive.com (formerly Polygon.io) API. After deleting any stocks with nulls or missing days, the dataset stands at 2784 NASADQ and NYSE stocks with 1255 trading days for each. 
""")

st.title("Why do some analyses not go back as far?")
st.write("""
Some rows had nulls for certain metrics. This is the result of certain time-series metrics having insufficient days to calculate them. For example, SMA100 (a moving average of the previous 100 closing prices per stock) does not exist on day 79. I handled this by creating two versions of the dataset - one which retains these nulls, and one which drops them.
""")




import pandas as pd


# =========================================================
# =========================================================
# =========================================================
# =========================================================

# 1 - Apple raw prices
st.write("""
For our first example, let's see AAPL's stock price over five years. 
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
We will run various comparisons with seven major technology stocks: AAPL, AMZN, GOOGL, META, MSFT, NFLX, and NVDA.
""")

st.write("""
Plotted below are absolute prices for the seven tech stocks over spans of one and five years.
""")

img3a = Image.open('visualizations/v03a_tech_absolute_1yr.png')
st.image(img3a)

img3b = Image.open('visualizations/v03b_tech_absolute_5y.png')
st.image(img3b)

st.write("""
Here, I instead plotted relative prices - each stock starts at 100 on the first day of the dataset and is subsequently measured relative to that benchmark.
""")

img4 = Image.open('visualizations/v04_tech_relative_1yr.png')
st.image(img4)

img5 = Image.open('visualizations/v05_tech_relative_5yr.png')
st.image(img5)

st.write("""
In the five-year graph, you can see NVDA's staggering relative growth relative to the others over time. However, by absolute price, it is still on the lower end within this group.
""")

st.write("""
I wanted to see what recent trends can tell us about the next few days. For each of the seven tech stocks, I measured the probability of a positive movement the day after several thresholds of gains, and then of negative movement after the same thresholds of negative movement. If no days met the gain or loss threshold for the stock, it will be marked N/A.
""")

img6 = Image.open('visualizations/v06_pos_prob_after_pct_pos.png')
st.image(img6)

img7 = Image.open('visualizations/v07_neg_prob_after_pct_neg.png')
st.image(img7)

st.write("""
Below, see a similar analysis, but with the thresholds instead measuring consecutive days of positive or negative movement.
""")

st.write("""
(Need to add 7 and 8)
""")

st.write("""
To what extent are our tech stocks collinear with each other, and how does this differ from the dataset as a whole? 
""")

img10 = Image.open('visualizations/v10_correlation_all.png')
st.image(img10)


img11 = Image.open('visualizations/v11_correlation_tech.png')
st.image(img11)

st.write("""
(Need to add 12 and 13)
""")

st.write("""
This visualization shows the ten stocks that improved the most in terms of actual price over the course of the entire dataset.
""")

img14 = Image.open('visualizations/v14_overall_improvement_top10.png')
st.image(img14)

img15 = Image.open('visualizations/v15_overall_improvement_top10_marcap.png')
st.image(img15)

