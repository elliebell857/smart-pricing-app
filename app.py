import streamlit as st
import pandas as pd

# Load the calendar CSV
@st.cache_data
def load_calendar():
    return pd.read_csv("occasion_calendar.csv")

calendar = load_calendar()

# Set page config (appearance changes)
st.set_page_config(
    page_title="Occasion Pricing Advisor",
    page_icon="💰",
    layout="centered",
    initial_sidebar_state="expanded"
)

# Inject custom CSS for background color and text styling
st.markdown(
    """
    <style>
    .stApp {
        background-color: #fff0f5; /* light pink background */
        color: #4b0082; /* dark purple text */
        font-family: Arial, sans-serif;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# App title
st.title("Occasion Pricing Advisor")

# Profile info
st.subheader("Your Profile")
school_level = st.radio("Are you in high school or college?", ["highschool", "college"])
region = st.text_input("Region (optional)", "Dallas, TX")

st.caption("Tip: you can tweak occasion multipliers in occasion_calendar.csv.")

# User inputs
uploaded_file = st.file_uploader("Upload an item image (optional)", type=["jpg", "jpeg", "png"])
original_price = st.number_input("Enter original purchase price ($):", min_value=0.0, step=1.0)

# Generate table of suggested prices
if original_price > 0:
    st.subheader("Suggested Rental Prices")
    results = []
    for _, row in calendar.iterrows():
        occasion = row["Occasion"]
        multiplier = row["Multiplier"]
        suggested_price = round(original_price * multiplier, 2)
        results.append({"Occasion": occasion, "Suggested Price ($)": suggested_price})

    results_df = pd.DataFrame(results)
    st.dataframe(results_df, use_container_width=True)
