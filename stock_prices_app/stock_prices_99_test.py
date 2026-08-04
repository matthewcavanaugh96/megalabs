import streamlit as st

st.title("Future ideas")

with st.expander("Hourly data"):
    st.write("""
    I downloaded daily data as well but I forgot how far back it goes. Could the hourly data somehow be incorporated with the daily data? to what extent? Another challenge is that (I believe) I got the hourly data from a different API which measures prices differently - the highest hourly price from the Hourly doesn't line up with the high price on the Daily set.
    """)

with st.expander("The implications of failure"):
    st.write("""
    Even though my change predictions are percentage-based, I can still use these values to infer predicted absolute prices. This may in turn allow me to create metircs measuring the cost of error per stock - for example, how much could an investor have lost out on by failing to invest in a stock that skyrocketed overnight, or investing in one that tanked? I may also be able to compare this to market capitalization.
    """)

with st.expander("Test 3"):
    st.write("""
    test
    """)