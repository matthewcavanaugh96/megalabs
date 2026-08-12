import streamlit as st



st.title("""
Modeling Results 🖥️ 🧠 🧮
""")


tab1, tab2 = st.tabs([
    "Ensemble Round 1",
    "Ensemble Round 2"
])

with tab1:
    st.header("Ensemble Round 1")
    st.write(""" 
    So far, this includes: Linear Regression, XGBoost, Random Forest, Extra Trees, Gradient Booster. These are the five models I initially ran for feature engineering purposes, though more may be added to this ensemble.
    """)

    #st.image("visualizations/Round_1_Model_Aggs.png", caption="Individual model aggregates", width=600)
    st.image("visualizations/models_and_ensemble.png", caption="Individual and ensemble scores. NOTE: Ensemble metrics are not a simple average of individual model metrics; they are calculated separately from the ensemble’s averaged predictions. This is why some metrics improve and others may decline.", width=800)



with tab2:
    st.header("Ensemble Round 2")
    st.write("""
    Coming soon
    """)

