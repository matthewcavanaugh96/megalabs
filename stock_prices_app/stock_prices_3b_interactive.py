import random
from pathlib import Path

import matplotlib.dates as mdates
import matplotlib.pyplot as plt
import pandas as pd
import streamlit as st


# ---------------------------------------------------------
# File paths
# ---------------------------------------------------------

APP_DIR = Path(__file__).resolve().parent

PRICE_DATA_PATH = APP_DIR / "daily_cleaned_price_data_CLOSE.parquet"
METADATA_PATH = APP_DIR / "daily_cleaned_metadata.parquet"


# ---------------------------------------------------------
# Page heading
# ---------------------------------------------------------

st.title("Make your own plots!")

st.write("""
This version will contain all 2784 stocks for which I have data. Performance may be slower, though I am working on optimizations.
""")


# ---------------------------------------------------------
# Load small ticker/name metadata only
# ---------------------------------------------------------

@st.cache_data
def load_stock_lookup() -> pd.DataFrame:
    metadata_df = pd.read_parquet(METADATA_PATH)

    stock_lookup = (
        metadata_df[["ticker", "name"]]
        .drop_duplicates(subset="ticker")
        .sort_values("ticker")
        .reset_index(drop=True)
    )

    stock_lookup["display_name"] = (
        stock_lookup["ticker"]
        + " ("
        + stock_lookup["name"].fillna("Unknown")
        + ")"
    )

    return stock_lookup


stock_lookup = load_stock_lookup()

display_names = stock_lookup["display_name"].tolist()

display_to_ticker = dict(
    zip(stock_lookup["display_name"], stock_lookup["ticker"])
)

ticker_to_display = dict(
    zip(stock_lookup["ticker"], stock_lookup["display_name"])
)


# ---------------------------------------------------------
# Load only selected tickers from the large Parquet file
# ---------------------------------------------------------

@st.cache_data(max_entries=1, show_spinner="Loading selected stock data...")
def load_selected_stock_data(
    tickers: tuple[str, ...],
    value_column: str
) -> pd.DataFrame:

    if not tickers:
        return pd.DataFrame()

    selected_df = pd.read_parquet(
        PRICE_DATA_PATH,
        engine="pyarrow",
        columns=[
            "timestamp",
            "ticker",
            value_column
        ],
        filters=[
            ("ticker", "in", list(tickers))
        ]
    )

    selected_df["timestamp"] = pd.to_datetime(
        selected_df["timestamp"]
    )

    return selected_df


# ---------------------------------------------------------
# Default selection
# ---------------------------------------------------------

if "AAPL" in ticker_to_display:
    default_selection = [ticker_to_display["AAPL"]]
else:
    default_selection = []


# =========================================================
# First plot — raw prices
# =========================================================

if "raw_stock_selector" not in st.session_state:
    st.session_state.raw_stock_selector = default_selection

if "raw_plot_tickers" not in st.session_state:
    st.session_state.raw_plot_tickers = []


def choose_random_stocks():
    st.session_state.raw_stock_selector = random.sample(
        display_names,
        min(5, len(display_names))
    )


def clear_stock_selection():
    st.session_state.raw_stock_selector = []


st.subheader("Raw prices")

st.write(
    """
    Search for stocks and build your own plot to compare their closing prices.
    Select the stocks first, then click **Generate plot**.
    """
)

button_col1, button_col2 = st.columns(2)

with button_col1:
    st.button(
        "🎲 Choose 5 random stocks",
        on_click=choose_random_stocks,
        use_container_width=True
    )

with button_col2:
    st.button(
        "Clear selection",
        on_click=clear_stock_selection,
        use_container_width=True
    )


with st.form("raw_stock_form"):

    selected_display_names = st.multiselect(
        "Search for one or more stocks",
        options=display_names,
        key="raw_stock_selector",
        max_selections=10
    )

    generate_raw = st.form_submit_button(
        "Generate raw-price plot",
        type="primary",
        use_container_width=True
    )


if generate_raw:

    selected_tickers = tuple(
        display_to_ticker[display_name]
        for display_name in selected_display_names
    )

    if selected_tickers:
        st.session_state.raw_plot_tickers = selected_tickers
    else:
        st.warning(
            "Choose at least one stock before generating the plot."
        )


plotted_tickers = tuple(st.session_state.raw_plot_tickers)

if not plotted_tickers:
    st.info("Choose at least one stock and click **Generate raw-price plot**.")

else:
    plot_df = load_selected_stock_data(
        plotted_tickers,
        "close"
    )

    fig, ax = plt.subplots(figsize=(12, 8))

    for ticker, stock_df in plot_df.groupby(
        "ticker",
        sort=False
    ):
        stock_df = stock_df.sort_values("timestamp")

        ax.plot(
            stock_df["timestamp"],
            stock_df["close"],
            label=ticker_to_display.get(ticker, ticker)
        )

    ax.set_xlabel("Date")
    ax.set_ylabel("Closing price ($)")
    ax.set_title("Stock closing prices over five years")

    ax.xaxis.set_major_locator(
        mdates.MonthLocator(interval=3)
    )

    ax.xaxis.set_major_formatter(
        mdates.DateFormatter("%Y-%m")
    )

    ax.tick_params(axis="x", rotation=45)
    ax.grid(True, alpha=0.3)
    ax.legend()

    fig.tight_layout()

    st.pyplot(fig)

    plt.close(fig)

    del plot_df
    del fig


# =========================================================
# Second plot — relative price performance
# =========================================================

st.divider()

st.subheader("Relative price performance")

st.write(
    """
    Compare stocks on the same scale. Each stock begins at **100**, making it
    easier to compare percentage growth regardless of the stock's actual price.
    """
)


if "relative_stock_selector" not in st.session_state:
    st.session_state.relative_stock_selector = default_selection

if "relative_plot_tickers" not in st.session_state:
    st.session_state.relative_plot_tickers = []


def choose_random_relative_stocks():
    st.session_state.relative_stock_selector = random.sample(
        display_names,
        min(5, len(display_names))
    )


def clear_relative_stock_selection():
    st.session_state.relative_stock_selector = []


relative_button_col1, relative_button_col2 = st.columns(2)

with relative_button_col1:
    st.button(
        "🎲 Choose 5 random stocks",
        key="relative_random_button",
        on_click=choose_random_relative_stocks,
        use_container_width=True
    )

with relative_button_col2:
    st.button(
        "Clear selection",
        key="relative_clear_button",
        on_click=clear_relative_stock_selection,
        use_container_width=True
    )




# selected_relative_display_names = st.multiselect(
#     "Search for one or more stocks",
#     options=display_names,
#     key="relative_stock_selector",
#     max_selections=10
# )


# if st.button(
#     "Generate relative-performance plot",
#     key="generate_relative_plot",
#     type="primary",
#     use_container_width=True
# ):
#     selected_relative_tickers = tuple(
#         display_to_ticker[display_name]
#         for display_name in selected_relative_display_names
#     )

#     if selected_relative_tickers:
#         st.session_state.relative_plot_tickers = (
#             selected_relative_tickers
#         )
#     else:
#         st.warning(
#             "Choose at least one stock before generating the relative plot."
#         )

with st.form("relative_stock_form"):

    selected_display_names = st.multiselect(
        "Search for one or more stocks",
        options=display_names,
        key="relative_stock_selector",
        max_selections=10
    )

    generate_relative = st.form_submit_button(
        "Generate relative-price plot",
        type="primary",
        use_container_width=True
    )


if generate_relative:

    selected_tickers = tuple(
        display_to_ticker[display_name]
        for display_name in selected_display_names
    )

    if selected_tickers:
        st.session_state.relative_plot_tickers = selected_tickers
    else:
        st.warning(
            "Choose at least one stock before generating the plot."
        )






relative_plot_tickers = tuple(
    st.session_state.relative_plot_tickers
)

if not relative_plot_tickers:
    st.info(
        "Choose at least one stock and click "
        "**Generate relative-performance plot**."
    )

else:
    relative_plot_df = load_selected_stock_data(
        relative_plot_tickers,
        "close_pct_of_day1"
    )

    fig, ax = plt.subplots(figsize=(12, 8))

    for ticker, stock_df in relative_plot_df.groupby(
        "ticker",
        sort=False
    ):
        stock_df = stock_df.sort_values("timestamp")

        ax.plot(
            stock_df["timestamp"],
            stock_df["close_pct_of_day1"],
            label=ticker_to_display.get(ticker, ticker)
        )

    ax.axhline(
        y=100,
        linestyle="--",
        linewidth=1,
        alpha=0.7
    )

    ax.set_xlabel("Date")
    ax.set_ylabel("Relative closing price (day 1 = 100)")
    ax.set_title("Relative stock performance over five years")

    ax.xaxis.set_major_locator(
        mdates.MonthLocator(interval=3)
    )

    ax.xaxis.set_major_formatter(
        mdates.DateFormatter("%Y-%m")
    )

    ax.tick_params(axis="x", rotation=45)
    ax.grid(True, alpha=0.3)
    ax.legend()

    fig.tight_layout()

    st.pyplot(fig)

    plt.close(fig)

    del relative_plot_df
    del fig