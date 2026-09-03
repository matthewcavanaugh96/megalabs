import streamlit as st
from pathlib import Path
from PIL import Image



st.title("""
Taking the model's advice
""")

# Removed from next section
# For scaling purposes, all of my predictions were made as percentages relative to the previous day for the same stock. However, I wondered what it would look like if I took these values to get implied absolute prices.


st.write("""
Below, I simulate possible investment outcomes based on several scenarios.

While I work on feature selection, I'll be using my Round 1 aggregate results. For this phase I may also add in a CNN/RNN and other models that were not usable in Round 1 for my feature selection method. However, depending on what I do for feature selection, those may wait to be combined with my optimized models.

""")



# Model advice
st.header("""
What if you took the model's advice every day?
""")

st.write("""
I simulated a scenario in which an investor took the models' advice every day in 2025. This hypothetical investor knows nothing other than the models' aggregate directional prediction for the day, and will act accordingly at open. They will enter day one of the simulation holding a single share of a stock at the previous day's actual closing value. For this and all subsequent days, their decision to buy, hold, or sell will be determined by the ensemble model's directional guess. If the ensemble predicts a positive movement, they will either hold their share if they have one or buy one if they don't have. If theensemble predicts a negative movement, they will sell their share if they have one or do nothing if they don't.

I ran this simulation previously, but have also created an alternative version with two killswitches which will result in the trader permanent ceasing to trade the stock: 
1. The stock drops 30% below its day-one value
2. The stock experiences 10 consecutive days of negative growth where the market overall is positive
""")


st.write("""
The results surprised me. We observed earlier than the ensemble model's directional accuracy was only 49%. Despite this, I found that for about 69% of stocks (1918 out of 2784), following the ensemble's advice would produce a stronger return than simply holding a share throughout the year.)
""")


st.write("""
If a trader simply held a single stock throughout the entire year, their closing portfolio value would be $980249.

Following the blind advice model, their closing value would be $1602655.

Following advice but with killswitches, the closing vlaue would be $2056783.

The total cost of incorrect killswitches - that is, stocks that finished above the value at which they were killed - was $1956.

The total benefit of correct killswitches - stocks that never recovered above their killed value - was $1185698.

This disparity is in spite of the absolute numbers of correct and incorrect killswitches being close to equal.
""")


st.write("""
OUTDATED VISUALIZATIONS Below, see which stocks would have done the best and worst for an investor following the model's advice.
""")


st.image("visualizations/ensemble_sim_top_10_pct.png", caption="These ten stocks had the largest potential return, by percentage, for an investor who always followed the ensemble model's advice.")

st.image("visualizations/ensemble_sim_bottom_10_pct.png", caption="These ten stocks had the largest potential loss, by percentage, for an investor who always followed the ensemble model's advice.")




# Correct every day
st.header("""
What if you could be right every day?
""")

st.write("""
For fun, I also simulated an investor who had a crystal ball and could perfectly predict directional accuracy - correctly holding, buying, or selling in anticipation of the coming day. If movement was positive, they'll be rewarded by the gain. If it was negative, they'll take no loss since they sold at opening.
""")

st.image("visualizations/always_right_top_10_pct.png", caption="These ten stocks hold the largest potential return by percentage for an investor who made the correct decision every day.")


# Wrong every day
st.header("""
What if you made the wrong decision every day?
""")

st.write("""
What about the other extreme - an investor who makes the WRONG decision every day?
""")

st.image("media/cramer.jpg", caption="Picture unrelated", width=200)

st.image("visualizations/always_wrong_top_10_pct.png", caption="These ten stocks hold the largest potential loss by percentage for an investor who made the wrong decision every day.")

