import streamlit as st



st.title("""
Modeling Results 🖥️ 🧠 🧮
""")


tab1, tab2, tab3, tab4 = st.tabs([
    "ARIMA",
    "Random Forest",
    "Linear Regression",
    "XGBoost"
])

with tab1:
    st.header("ARIMA")
    st.write(""" 
    I tried an ARIMA time series model.

    The first piece of news was good - every stock passed the Augmented Dickey-Fuller (ADF) test, meaning no difference was required, so I could set d=0 and move on.
            
    Then, I performed a grid search to find the best combination of autoregressive (p) and moving-average (q) values for each stock, using Akaike Information Criterion (AIC) as my measuring stick. 
            
    Roughly a quarter of all stocks selected ARIMA(0,0,0), indicating a negligible difference from white noise.
        
    Rather than choosing a single ARIMA specification, a grid search was performed across multiple combinations of autoregressive (p) and moving-average (q) orders. For each stock, the model with the lowest Akaike Information Criterion (AIC) was selected.
            
    However, even the best-performing models had directional accuracy barely better than a coin flip. I'll nonetheless find a way to incorporate these results for comparison and benchmark purposes. 
    """)


with tab2:
    st.header("Random Forest")


with tab3:
    st.header("Linear Regression")

with tab4:
    st.header("XGBoost")

