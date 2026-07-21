import streamlit as st

st.set_page_config(
    page_title="Stock prediction project", 
    page_icon = "📈", 
    layout="centered"
)

# Define pages
home = st.Page("stock_prices_1_home.py", title="Home", icon="🏠")
eda = st.Page("stock_prices_2_EDA.py", title="Exploring past data", icon="🗓️")
interactive = st.Page("stock_prices_3_interactive.py", title="Make your own plot!", icon="🫵")
mod_overview = st.Page("stock_prices_4_mod_overview.py", title="Modeling Overview", icon="🤔")
mod_results = st.Page("stock_prices_5_mod_results.py", title="Modeling Results", icon="🧠")
test_page = st.Page("stock_prices_6_test.py", title="Future ideas and experiments", icon="🧪")


# Set up navigation
nav = st.navigation([home, eda, interactive, mod_overview, mod_results, test_page])
nav.run()
