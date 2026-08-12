import streamlit as st

st.title("Future ideas")

with st.expander("Hourly data"):
    st.write("""
    I downloaded daily data as well but I forgot how far back it goes. Could the hourly data somehow be incorporated with the daily data? to what extent? Another challenge is that (I believe) I got the hourly data from a different API which measures prices differently - the highest hourly price from the Hourly doesn't line up with the high price on the Daily set.
    """)



with st.expander("Expander test"):
    st.write("""
    test
    """)