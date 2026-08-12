import streamlit as st

st.title("Bonus page")
st.write("""
This is where I will put one-off analyses that don't fit elsewhere, future ideas, and experiements.
""")


st.subheader("Daily accuracy")
st.write("""
What did the ensemble model look like on a daily basis?
""")

st.image("visualizations/round_1_ensemble_daily_abs_error.png", caption="Ensemble average daily absolute error for all trading days in 2025. All models failed to predict the massive spike seen on April 9.", width=800)



st.title("Future ideas")


with st.expander("Hourly data"):
    st.write("""
    I downloaded daily data as well but I forgot how far back it goes. Could the hourly data somehow be incorporated with the daily data? to what extent? Another challenge is that I got the hourly data from a different API which measures prices differently - the highest hourly price from the Hourly doesn't line up with the high price on the Daily set.
    """)



with st.expander("Categories"):
    st.write("""
    I am curious as to how stocks in similar categories (finance, travel etc) moved relative to each other. Howwever, categorization can be subjective, and the API data I downloaded did not provide any such labels. With nearly 3000 stocks, this would be too much to do manually, so this may be a task for AI agents.
    """)