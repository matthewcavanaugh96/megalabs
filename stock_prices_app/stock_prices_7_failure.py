import streamlit as st
from pathlib import Path
from PIL import Image



st.title("""
Taking the model's advice
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
I simulated a scenario in which an investor took the models' advice every day in 2025. This hypothetical investor knows nothing other than the models' aggregate directional prediction for the day, and will act accordingly at open. They will enter day one of the simulation holding a single share of a stock at the previous day's actual closing value. For this and all subsequent days, their decision to buy, hold, or sell will be determined by the ensemble model's directional guess. If the ensemble predicts a positive movement, they will either hold their share or buy one if they don't have one. If the ensemble predicts a negative movement, they will sell their share if they have one or do nothing if they don't.

The results surprised me. We observed earlier than the ensemble model's directional accuracy was just under 50%. Despite this, I found that for 69% of stocks (1920 out of 2784), following the ensemble's advice would produce a stronger return than simply holding a share throughout the year. 

This suggested to me that the average positive day probably produces a stronger growth than a negative day does a loss. But even this difference was surprisingly negligible: positive days had a mean growth of 2.026 and median of 1.238, while negative days had a mean loss of -1.927 and median of -1.232, and there were slightly more negative than positive stock days.
""")

# st.image("visualizations/v20_ensemble_direct_correct.png", caption="Picture unrelated", width=200)
# st.image("visualizations/v21_ensemble_better_than_holding.png", caption="Caption", width=200)


# Correct every day
# Wrong every day
st.header("""
Nostradamus?
""")

st.write("""
For fun, let's assume you have a crystal ball and can predict directional accuracy every day - perfectly holding, buying, or selling in anticipation of the coming day.

If movement was positive, you'll be rewarded by the gain.

If it was negative, you'll take no loss since you did not hold the stock.
""")


# Wrong every day
st.header("""
What if you made the wrong decision every day?
""")


st.write("""
What about the other extreme - an investor who makes the WRONG decision every day?
""")

st.image("media/cramer.jpg", caption="Picture unrelated", width=200)
