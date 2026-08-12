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
I simulated a scenario in which an investor took the models' advice every day in 2025. This hypothetical investor knows nothing other than the models' aggregate directional prediction for the day, and will act accordingly at open. They will enter day one of the simulation holding a single share of a stock at the previous day's actual closing value. For this and all subsequent days, their decision to buy, hold, or sell will be determined by the ensemble model's directional guess. If the ensemble predicts a positive movement, they will either hold their share if they have one or buy one if they don't have. If the ensemble predicts a negative movement, they will sell their share if they have one or do nothing if they don't.
""")


st.markdown("The results surprised me. We observed earlier than the ensemble model's directional accuracy was only 49%. <u>Despite this, I found that for 69% of stocks (1920 out of 2784), following the ensemble's advice would produce a stronger return than simply holding a share throughout the year.</u>. (Need to triple check this math)", unsafe_allow_html=True)

st.write("""
This suggested to me that the average positive day probably produces a stronger growth than a negative day does a loss. But even this difference was surprisingly negligible: positive days had a mean growth of 2.026 and median of 1.238, while negative days had a mean loss of -1.927 and median of -1.232, and there were slightly more negative than positive stock days.
""")

st.write("""
Below, see which stocks would have done the best and worst for an investor following the model's advice.
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

