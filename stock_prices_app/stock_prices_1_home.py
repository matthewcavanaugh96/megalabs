import streamlit as st

st.title("""
Welcome!
""")


st.write("""
This is my stock project.

Use the sidebar on the left to navigate between sections.

""")

st.title("""
About
""")

st.write("""

My dataset contains five years of daily stock data, downloaded from the Massive.com (formerly Polygon.io) API.

After deleting stocks with nulls or missing days, the dataset stands at 2784 NASDAQ and NYSE stocks.

The dataset spans from 2025-05-24 to 2026-05-21, with 1255 trading days.
""")

st.write("""
First, I ran exploratory EDA about my dataset.

Then, I ran various machine learning and deep learning models, the results of which can be seen in its own section.
""")