import streamlit as st
import pandas as pd
from io import StringIO
from datetime import datetime, date
import os

# =========================
# THEME & STYLES
# =========================
st.set_page_config(page_title="Occasion Pricing Advisor", page_icon="💃", layout="centered")

st.markdown("""
    <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;600;700&family=Playfair+Display:wght@500;700&display=swap" rel="stylesheet">
    <style>
    html, body, [class*="css"] { font-family: 'Poppins', sans-serif; }
    h1, h2, h3 { font-family: 'Playfair Display', serif; color: #7A2E8E; font-weight: 700; }

    /* App background gradient */
    .stApp { background: linear-gradient(135deg, #ffe6f0, #fff5e6); }

    /* Sidebar */
    [data-testid="stSidebar"] { background-color: #fff0f5; }

    /* Section cards */
    .card {
        background: rgba(255,255,255,0.85);
        border-radius: 16px;
        padding: 18px 18px;
        box-shadow: 0 8px 24px rgba(0,0,0,0.06);
        border: 1px solid rgba(122,46,142,0.08);
        margin-bottom: 16px;
    }
    .divider {
        height: 1px;
        background: linear-gradient(to right, rgba(122,46,142,0.25), rgba(255,255,255,0));
        margin: 12px 0 8px;
    }

    /* Buttons */
    .stButton>button {
        background-color: #FF85A2;
        color: #fff;
        border-radius: 12px;
        border: none;
        padding: 0.65em 1.2em;
        font-size: 1rem;
        transition: all 0.25s ease;
        box-shadow: 0 6px 16px rgba(255,133,162,0.35);
    }
    .stButton>button:hover { background-color: #E75480; transform: translateY(-1px) scale(1.02); }

    /* Inputs */
    .stTextInput>div>div>input, .stNumberInput input, .stSelectbox div[data-baseweb="select"] > div {
        background-color: #fff;
        border-radius: 10px;
        border: 1px solid #ddd;
    }
    [data-testid="stFileUploader"] {
        background: rgba(255,255,255,0.9);
        border-radius: 12px; padding: 14px; border: 1px dashed #e3b9c6;
    }

    /* Dataframe tweaks */
    .stDataFrame { background: rgba(255,255,255,0.9) !important; border-radius: 12px; padding: 6px; }
    </style>
""", unsafe_allow_html=True)

st.title("💃 Occasion Pricing Advisor")
st.caption("Upload an item, enter retail price + any notes, and get suggested rental prices by season/occasion.")


# =========================
# DATA: LOAD CALENDAR (CSV or fallback defaults)
# =========================
@st.cache_data
def load_calendar():
    path = "occasion_calendar.csv"
    if os.path.exists(path):
        return pd.read_csv(path)

    # Fallback table if CSV isn't present
    default_csv = """occasion,user_type,start_month,end_month,multiplier,notes
homecoming,highschool,9,10,1.25,Sept-Oct peak for short and midi dresses
prom,highschool,3,5,1.35,Mar-May very high demand for gowns and sparkly minis
winter_formal,highschool,12,1,1.15,Dec-Jan school formals/holiday parties
football_season,college,9,11,1.15,Game days and tailgates (school colors popular)
date_parties,college,10,4,1.10,Themed mixers and semi-formals
formals,college,11,4,1.25,Greek life and club formals
rush,college,8,8,1.20,Panhellenic recruitment (neutrals/white)
"""
    st.warning("`occasion_calendar.csv` not found — using built‑in defaults. "
               "Add the CSV to your repo root to customize.")
    return pd.read_csv(StringIO(default_csv))

calendar = load_calendar()


# =========================
# SIDEBAR: PROFILE
# =========================
with st.sidebar:
    st.header("Your Profile")
    user_type = st.radio("Are you in high school or college?", ["highschool", "college"], horizontal=False)
    region = st.text_input("Region (optional)", value="Dallas, TX")
    st.markdown("<div class='divider'></div>", unsafe_allow_html=True)
    st.caption("Tip: tweak season multipliers in `occasion_calendar.csv`.")


# =========================
# HELPERS
# =========================
def material_adjust(material):
    return {
        "Silk": 1.10, "Satin": 1.07, "Lace": 1.05, "Sequin": 1.12,
        "Cotton": 1.00, "Polyester": 0.98, "Other": 1.00, "Unknown": 1.00,
    }.get(material, 1.00)

def condition_adjust(score: int):
    # 1..5 -> 0.75 .. 1.05
    return {1:0.75, 2:0.85, 3:0.93, 4:1.00, 5:1.05}[int(score)]

def silhouette_adjust(sil):
    return {"mini":1.00, "midi":1.05, "gown":1.15, "set":1.02, "jumpsuit":0.95, "Unknown":1.00}.get(sil,1.00)

def rush_weekend_multiplier(days, weekend, rush_pct, weekend_pct):
    m = 1.0
    if days is not None and days <= 4:
        m *= (1 + rush_pct/100.0)
    if weekend:
        m *= (1 + weekend_pct/100.0)
    return m


# =========================
# LAYOUT: CARDS
# =========================
st.markdown("<div class='card'>", unsafe_allow_html=True)
st.subheader("1) Item details")
img = st.file_uploader("Upload a photo (JPG/PNG)", type=["jpg","jpeg","png"])
c1, c2 = st.columns(2)
with c1:
    original_price = st.number_input("Original retail price ($)", min_value=10.0, max_value=5000.0, value=250.0, step=5.0)
    condition = st.slider("Condition (1 = poor • 5 = excellent)", 1, 5, 5)
    material = st.selectbox("Material (optional)", ["Unknown","Silk","Satin","Cotton","Lace","Polyester","Sequin","Other"])
with c2:
    silhouette = st.selectbox("Silhouette (optional)", ["Unknown","mini","midi","gown","set","jumpsuit"])
    color = st.selectbox("Color (optional)", ["Unknown","black","white","pink","blue","red","green","gold","silver","other"])
    notes = st.text_area("Notes (damage, fit, brand, etc.)", placeholder="Small snag on hem; runs short; LSF Pera Pink…")
st.markdown("</div>", unsafe_allow_html=True)

st.markdown("<div class='card'>", unsafe_allow_html=True)
st.subheader("2) Pricing knobs (optional)")
base_pct = st.slider("Base rental % of retail", 5, 50, 30, help="Starting point before season/condition adjustments")
rush_markup = st.slider("Rush markup % (≤4 days to event)", 0, 50, 10)
weekend_markup = st.slider("Weekend event markup %", 0, 40, 5)
st.markdown("</div>", unsafe_allow_html=True)

st.markdown("<div class='card'>", unsafe_allow_html=True)
st.subheader("3) Event info (for rush/weekend)")
event_date = st.date_input("Next expected event date (optional)")
today = datetime.now().date()
days_to_event = (event_date - today).days if event_date else None
is_weekend = event_date.weekday() >= 5 if event_date else False
st.markdown("</div>", unsafe_allow_html=True)

st.markdown("<div class='card'>", unsafe_allow_html=True)
generate = st.button("Generate Pricing Report")
st.markdown("</div>", unsafe_allow_html=True)


# =========================
# COMPUTE & SHOW REPORT (TABLE ONLY)
# =========================
if generate:
    # Base rental before occasion
    base_price = original_price * (base_pct/100.0)
    base_price *= material_adjust(material)
    base_price *= condition_adjust(condition)
    base_price *= silhouette_adjust(silhouette)
    base_price *= rush_weekend_multiplier(days_to_event, is_weekend, rush_markup, weekend_markup)

    # Filter occasions by user type
    df = calendar[calendar["user_type"] == user_type].copy()

    # Are we currently in season?
    month = today.month
    df["in_season_now"] = (
        ((df["start_month"] <= df["end_month"]) & ( (month >= df["start_month"]) & (month <= df["end_month"]) )) |
        ((df["start_month"] > df["end_month"])  & ( (month >= df["start_month"]) | (month <= df["end_month"]) ))
    )

    # Suggested prices and bands
    df["suggested_price"] = (base_price * df["multiplier"]).round(0)
    df["low"] = (df["suggested_price"] * 0.9).round(0)
    df["high"] = (df["suggested_price"] * 1.1).round(0)

    # Simple confidence score (you can refine later)
    conf = 70
    if material in ["Silk","Sequin"] and condition >= 4: conf += 5
    if silhouette == "gown": conf += 5
    df["confidence_%"] = conf

    # OPTIONAL preview card for the uploaded image
    if img:
        st.image(img, caption="Uploaded item", use_column_width=True)

    # Headline number (no code blocks)
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.subheader(f"Base rental (pre-season): ${base_price:.0f}")
    st.markdown("<div class='divider'></div>", unsafe_allow_html=True)

    # Clean display table (no code formatting)
    display_cols = ["occasion","start_month","end_month","multiplier","suggested_price","low","high","in_season_now","confidence_%"]
    st.dataframe(df[display_cols], use_container_width=True, hide_index=True)

    # Optional: CSV download button
    st.download_button(
        "Download pricing table as CSV",
        data=df[display_cols].to_csv(index=False),
        file_name="pricing_report.csv",
        mime="text/csv"
    )

    # Tiny “how computed” note — plain text, not code
    st.markdown(
        "**How prices are computed:** Base = retail × base% × material × condition × silhouette × (rush/weekend) → "
        "then × occasion multiplier from your season table."
    )
    st.markdown("</div>", unsafe_allow_html=True)
