import streamlit as st
from pathlib import Path
from PIL import Image



st.title("""
The implications of failure
""")

st.write("""
For scaling purposes, all of my predictions were made as percentages relative to the previous day for the same stock. However, I wondered what it would look like if I took these values to get implied absolute prices.

Below, I simulate possible investment outcomes based on several scenarios.

While I work on feature selection, I'll be using my Round 1 aggregate results. For this phase I may also add in a CNN/RNN and other models that were not usable in Round 1 for my feature selection method.

""")



# Model advice
st.header("""
What if you took the model's advice every day?
""")

st.write("""
I simulated a scenario in which an investor took the models' advice every day. This hypothetical investor knows nothing other than the models' aggregate directional prediction for the day, and will act accordingly at open.

If directionality is incorrect, I will measure how much they lost by selling or failing to buy.

Would you have been better off just holding through?
""")


# Correct every day
st.write("""
For fun, let's assume you have a crystal ball and can predict directional accuracy every day - perfectly holding, buying, or selling in anticipation of the coming day.

If movement was positive, you'll be rewarded by the gain.

If it was negative, you'll take no loss since you did not hold the stock.
""")


# Wrong every day
st.header("""
What if you made the wrong decision every day?
""")

st.image("media/cramer.jpg", caption="Picture unrelated", width=200)

st.write("""
What about the other extreme - an investor who makes the WRONG decision every day?
""")