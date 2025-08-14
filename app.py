
import streamlit as st
import pandas as pd
from datetime import datetime
import io

st.set_page_config(page_title="Occasion Pricing Advisor", page_icon="💃", layout="centered")

st.title("💃 Occasion Pricing Advisor")
st.caption("Upload an item, enter its original price, and get suggested rental prices by season/occasion.")

# ---- User Profile (stored in session for demo) ----
st.sidebar.header("Your Profile")
user_type = st.sidebar.radio("Are you in high school or college?", ["highschool", "college"])
region = st.sidebar.text_input("Region (optional)", value="Dallas, TX")
st.sidebar.markdown("---")
st.sidebar.caption("Tip: you can tweak occasion multipliers in `occasion_calendar.csv`.")

# ---- Occasion Calendar ----
@st.cache_data
def load_calendar():
    return pd.read_csv("occasion_calendar.csv")
calendar = load_calendar()

# ---- Item Upload Form ----
st.subheader("1) Item details")
img = st.file_uploader("Upload a photo (JPG/PNG)", type=["jpg","jpeg","png"])
col1, col2 = st.columns(2)
with col1:
    original_price = st.number_input("Original retail price ($)", min_value=10.0, max_value=5000.0, value=250.0, step=5.0)
    condition = st.slider("Condition (1-poor to 5-excellent)", min_value=1, max_value=5, value=5)
    material = st.selectbox("Material (optional)", ["Unknown","Silk","Satin","Cotton","Lace","Polyester","Sequin","Other"])
with col2:
    silhouette = st.selectbox("Silhouette (optional)", ["Unknown","mini","midi","gown","set","jumpsuit"])
    color = st.selectbox("Color (optional)", ["Unknown","black","white","pink","blue","red","green","gold","silver","other"])
    notes = st.text_area("Notes (damage, fit, brand, etc.)")

st.subheader("2) Pricing knobs (optional)")
base_pct = st.slider("Base rental % of retail", 5, 50, 30, help="Starting point before season/condition adjustments")
rush_markup = st.slider("Rush (<4 days to event) markup %", 0, 50, 10)
weekend_markup = st.slider("Weekend event markup %", 0, 40, 5)

st.subheader("3) Event info (for rush/weekend logic)")
event_date = st.date_input("Next expected event date (optional)")
today = datetime.now().date()
days_to_event = (event_date - today).days if event_date else None
is_weekend = event_date.weekday() >= 5 if event_date else False

def material_adjust(material):
    return {
        "Silk": 1.10, "Satin": 1.07, "Lace": 1.05, "Sequin": 1.12,
        "Cotton": 1.00, "Polyester": 0.98, "Other": 1.00, "Unknown": 1.00,
    }.get(material, 1.00)

def condition_adjust(score):
    # scale 1..5 -> 0.75 .. 1.05
    return {1:0.75,2:0.85,3:0.93,4:1.00,5:1.05}[int(score)]

def silhouette_adjust(sil):
    return {"mini":1.00,"midi":1.05,"gown":1.15,"set":1.02,"jumpsuit":0.95,"Unknown":1.00}.get(sil,1.00)

def rush_weekend_multiplier(days, weekend, rush_pct, weekend_pct):
    m = 1.0
    if days is not None and days <= 4:
        m *= (1 + rush_pct/100.0)
    if weekend:
        m *= (1 + weekend_pct/100.0)
    return m

if st.button("Generate Pricing Report"):
    # Base rental before occasion
    base_price = original_price * (base_pct/100.0)
    base_price *= material_adjust(material)
    base_price *= condition_adjust(condition)
    base_price *= silhouette_adjust(silhouette)
    base_price *= rush_weekend_multiplier(days_to_event, is_weekend, rush_markup, weekend_markup)

    # Build occasion table filtered by user_type
    df = calendar[calendar["user_type"]==user_type].copy()
    # Compute seasonality factor by today's month as a demo and also provide a general suggested price
    month = today.month
    df["in_season_now"] = ( (df["start_month"] <= df["end_month"]) & ( (month >= df["start_month"]) & (month <= df["end_month"]) ) ) | \
                          ( (df["start_month"] > df["end_month"]) & ( (month >= df["start_month"]) | (month <= df["end_month"]) ) )

    df["suggested_price"] = (base_price * df["multiplier"]).round(0)
    df["low"] = (df["suggested_price"] * 0.9).round(0)
    df["high"] = (df["suggested_price"] * 1.1).round(0)

    # Simple confidence score
    conf = 70
    if material in ["Silk","Sequin"] and condition >=4: conf += 5
    if silhouette=="gown": conf += 5
    df["confidence_%"] = conf

    st.image(img, caption="Uploaded item", use_column_width=True) if img else None
    st.markdown(f"**Base rental (pre-season):** ${base_price:.0f}")
    st.dataframe(df[["occasion","start_month","end_month","multiplier","suggested_price","low","high","in_season_now","confidence_%"]])

    # Downloadable CSV
    st.download_button("Download report CSV", data=df.to_csv(index=False), file_name="pricing_report.csv", mime="text/csv")

    st.markdown("""
    **How this was computed:**  
    Base = retail × base% × material × condition × silhouette × (rush/weekend) → then × occasion multiplier.
    You can edit multipliers in `occasion_calendar.csv`.
    """)
