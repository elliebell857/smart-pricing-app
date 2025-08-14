mport streamlit as st
import pandas as pd
from io import StringIO
from datetime import datetime, date
import os

# =========================
# PAGE SETUP & INLINE APPEARANCE
# =========================
st.set_page_config(page_title="Occasion Pricing Advisor", page_icon="💃", layout="centered")

# Inline CSS + Google Fonts (no external file needed)
st.markdown("""
<link href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;600;700&family=Playfair+Display:wght@600;700&display=swap" rel="stylesheet">
<style>
/* Fonts */
html, body, [class*="css"] { font-family: 'Poppins', sans-serif; }
h1, h2, h3 { font-family: 'Playfair Display', serif; color:#7A2E8E; font-weight:700; }

/* Background gradient */
.stApp { background: linear-gradient(135deg, #ffe6f0, #fff5e6); }

/* Sidebar */
[data-testid="stSidebar"] {
  background:#fff0f5; border-right:1px solid rgba(122,46,142,0.08);
}

/* Card sections (use with st.markdown wrappers if desired) */
.card {
  background: rgba(255,255,255,0.92);
  border-radius: 14px;
  padding: 16px;
  box-shadow: 0 10px 24px rgba(0,0,0,0.06);
  border: 1px solid rgba(122,46,142,0.08);
  margin: 10px 0 14px;
}
.divider {
  height:1px;
  background:linear-gradient(90deg, rgba(122,46,142,0.25), rgba(255,255,255,0));
  margin:10px 0 6px;
}

/* Buttons */
.stButton>button{
  background:#FF85A2; color:#fff; border:none; border-radius:12px;
  padding:.6em 1.1em; font-size:1rem; box-shadow:0 6px 16px rgba(255,133,162,.35);
  transition:all .2s ease;
}
.stButton>button:hover{ background:#E75480; transform:translateY(-1px) scale(1.02); }

/* Inputs */
.stTextInput>div>div>input, .stNumberInput input, .stSelectbox div[data-baseweb="select"]>div{
  background:#fff; border-radius:10px; border:1px solid #e5e5e5;
}

/* File uploader */
[data-testid="stFileUploader"]{
  background:rgba(255,255,255,.95); border-radius:12px; padding:12px; border:1px dashed #e3b9c6;
}

/* Table */
.stDataFrame { background:rgba(255,255,255,.95) !important; border-radius:12px; padding:6px; }
</style>
""", unsafe_allow_html=True)

# =========================
# TITLE
# =========================
st.title("💃 Occasion Pricing Advisor")
st.caption("Upload an item, enter its original price, and get suggested rental prices by season/occasion.")

# =========================
# DATA: LOAD CALENDAR (CSV or fallback defaults)
# =========================
@st.cache_data
def load_calendar() -> pd.DataFrame:
    """
    Reads 'occasion_calendar.csv' from repo root if present.
    Else uses defaults so the app still runs.
    Required columns: occasion,user_type,start_month,end_month,multiplier,notes
    """
    path = "occasion_calendar.csv"
    if os.path.exists(path):
        return pd.read_csv(path)

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
               "Add the CSV to your repo root to customize seasons/multipliers.")
    return pd.read_csv(StringIO(default_csv))

calendar = load_calendar()

# =========================
# SIDEBAR: PROFILE
# =========================
st.sidebar.header("Your Profile")
user_type = st.sidebar.radio("Are you in high school or college?", ["highschool", "college"])
region = st.sidebar.text_input("Region (optional)", value="Dallas, TX")
st.sidebar.markdown("---")
st.sidebar.caption("Tip: tweak season multipliers in `occasion_calendar.csv` (optional).")

# =========================
# ITEM FORM (original fields)
# =========================
st.subheader("1) Item details")
img = st.file_uploader("Upload a photo (JPG/PNG)", type=["jpg","jpeg","png"])  # kept for future, not shown in report
col1, col2 = st.columns(2)
with col1:
    original_price = st.number_input("Original retail price ($)", min_value=10.0, max_value=5000.0, value=250.0, step=5.0)
    condition = st.slider("Condition (1–5)", 1, 5, 5)
    material = st.selectbox("Material (optional)", ["Unknown","Silk","Satin","Cotton","Lace","Polyester","Sequin","Other"])
with col2:
    silhouette = st.selectbox("Silhouette (optional)", ["Unknown","mini","midi","gown","set","jumpsuit"])
    color = st.selectbox("Color (optional)", ["Unknown","black","white","pink","blue","red","green","gold","silver","other"])
    notes = st.text_area("Notes (damage, material details, brand, etc.)")

st.subheader("2) Pricing knobs (optional)")
base_pct = st.slider("Base rental % of retail", 5, 50, 30, help="Starting point before season/condition adjustments")
rush_markup = st.slider("Rush (<4 days to event) markup %", 0, 50, 10)
weekend_markup = st.slider("Weekend event markup %", 0, 40, 5)

st.subheader("3) Event info (for rush/weekend logic)")
event_date = st.date_input("Next expected event date (optional)")
today = datetime.now().date()
days_to_event = (event_date - today).days if event_date else None
is_weekend = event_date.weekday() >= 5 if event_date else False

# =========================
# PRICING ADJUSTMENTS (same logic as original)
# =========================
def material_adjust(material_name: str) -> float:
    return {
        "Silk": 1.10, "Satin": 1.07, "Lace": 1.05, "Sequin": 1.12,
        "Cotton": 1.00, "Polyester": 0.98, "Other": 1.00, "Unknown": 1.00,
    }.get(material_name, 1.00)

def condition_adjust(score: int) -> float:
    return {1:0.75, 2:0.85, 3:0.93, 4:1.00, 5:1.05}[int(score)]

def silhouette_adjust(sil: str) -> float:
    return {"mini":1.00, "midi":1.05, "gown":1.15, "set":1.02, "jumpsuit":0.95, "Unknown":1.00}.get(sil, 1.00)

def rush_weekend_multiplier(days, weekend: bool, rush_pct: int, weekend_pct: int) -> float:
    m = 1.0
    if days is not None and days <= 4:
        m *= (1 + rush_pct/100.0)
    if weekend:
        m *= (1 + weekend_pct/100.0)
    return m

# =========================
# GENERATE REPORT (TABLE ONLY)
# =========================
if st.button("Generate Pricing Report"):
    # Base rental before occasion multipliers
    base_price = original_price * (base_pct / 100.0)
    base_price *= material_adjust(material)
    base_price *= condition_adjust(condition)
    base_price *= silhouette_adjust(silhouette)
    base_price *= rush_weekend_multiplier(days_to_event, is_weekend, rush_markup, weekend_markup)

    # Filter occasions by user type
    df = calendar[calendar["user_type"] == user_type].copy()

    # In-season flag based on current month
    month = today.month
    df["in_season_now"] = (
        ((df["start_month"] <= df["end_month"]) & ((month >= df["start_month"]) & (month <= df["end_month"]))) |
        ((df["start_month"] > df["end_month"])  & ((month >= df["start_month"]) | (month <= df["end_month"])))
    )

    # Suggested prices & bands
    df["suggested_price"] = (base_price * df["multiplier"]).round(0)
    df["low"] = (df["suggested_price"] * 0.9).round(0)
    df["high"] = (df["suggested_price"] * 1.1).round(0)

    # Simple confidence
    conf = 70
    if material in ["Silk","Sequin"] and condition >= 4: conf += 5
    if silhouette == "gown": conf += 5
    df["confidence_%"] = conf

    # TABLE ONLY (no image, no headline number, no charts, no download)
    display_cols = [
        "occasion", "start_month", "end_month", "multiplier",
        "suggested_price", "low", "high", "in_season_now", "confidence_%"
    ]
    st.dataframe(df[display_cols], use_container_width=True, hide_index=True)st.sidebar.markdown("---")
st.sidebar.caption("Tip: tweak season multipliers in `occasion_calendar.csv` (if present).")

# ---------------------------------------------------
# Item form (original fields)
# ---------------------------------------------------
st.subheader("1) Item details")
img = st.file_uploader("Upload a photo (JPG/PNG)", type=["jpg","jpeg","png"])  # kept for future; not shown in report
col1, col2 = st.columns(2)
with col1:
    original_price = st.number_input("Original retail price ($)", min_value=10.0, max_value=5000.0, value=250.0, step=5.0)
    condition = st.slider("Condition (1–5)", 1, 5, 5)
    material = st.selectbox("Material (optional)", ["Unknown","Silk","Satin","Cotton","Lace","Polyester","Sequin","Other"])
with col2:
    silhouette = st.selectbox("Silhouette (optional)", ["Unknown","mini","midi","gown","set","jumpsuit"])
    color = st.selectbox("Color (optional)", ["Unknown","black","white","pink","blue","red","green","gold","silver","other"])
    notes = st.text_area("Notes (damage, material details, brand, etc.)")

st.subheader("2) Pricing knobs (optional)")
base_pct = st.slider("Base rental % of retail", 5, 50, 30, help="Starting point before season/condition adjustments")
rush_markup = st.slider("Rush (<4 days to event) markup %", 0, 50, 10)
weekend_markup = st.slider("Weekend event markup %", 0, 40, 5)

st.subheader("3) Event info (for rush/weekend logic)")
event_date = st.date_input("Next expected event date (optional)")
today = datetime.now().date()
days_to_event = (event_date - today).days if event_date else None
is_weekend = event_date.weekday() >= 5 if event_date else False

# ---------------------------------------------------
# Pricing adjustments (original logic)
# ---------------------------------------------------
def material_adjust(material_name: str) -> float:
    return {
        "Silk": 1.10, "Satin": 1.07, "Lace": 1.05, "Sequin": 1.12,
        "Cotton": 1.00, "Polyester": 0.98, "Other": 1.00, "Unknown": 1.00,
    }.get(material_name, 1.00)

def condition_adjust(score: int) -> float:
    return {1:0.75, 2:0.85, 3:0.93, 4:1.00, 5:1.05}[int(score)]

def silhouette_adjust(sil: str) -> float:
    return {"mini":1.00, "midi":1.05, "gown":1.15, "set":1.02, "jumpsuit":0.95, "Unknown":1.00}.get(sil, 1.00)

def rush_weekend_multiplier(days, weekend: bool, rush_pct: int, weekend_pct: int) -> float:
    m = 1.0
    if days is not None and days <= 4:
        m *= (1 + rush_pct/100.0)
    if weekend:
        m *= (1 + weekend_pct/100.0)
    return m

# ---------------------------------------------------
# Generate report (TABLE ONLY)
# ---------------------------------------------------
if st.button("Generate Pricing Report"):
    # Base rental before occasion multipliers
    base_price = original_price * (base_pct / 100.0)
    base_price *= material_adjust(material)
    base_price *= condition_adjust(condition)
    base_price *= silhouette_adjust(silhouette)
    base_price *= rush_weekend_multiplier(days_to_event, is_weekend, rush_markup, weekend_markup)

    # Filter seasons/occasions by user type
    df = calendar[calendar["user_type"] == user_type].copy()

    # In-season flag based on current month
    month = today.month
    df["in_season_now"] = (
        ((df["start_month"] <= df["end_month"]) & ((month >= df["start_month"]) & (month <= df["end_month"]))) |
        ((df["start_month"] > df["end_month"])  & ((month >= df["start_month"]) | (month <= df["end_month"])))
    )

    # Suggested prices & bands
    df["suggested_price"] = (base_price * df["multiplier"]).round(0)
    df["low"] = (df["suggested_price"] * 0.9).round(0)
    df["high"] = (df["suggested_price"] * 1.1).round(0)

    # Simple confidence
    conf = 70
    if material in ["Silk","Sequin"] and condition >= 4: conf += 5
    if silhouette == "gown": conf += 5
    df["confidence_%"] = conf

    # TABLE ONLY (no image, no headline number, no charts, no download)
    display_cols = [
        "occasion", "start_month", "end_month", "multiplier",
        "suggested_price", "low", "high", "in_season_now", "confidence_%"
    ]
    st.dataframe(df[display_cols], use_container_width=True, hide_index=True)
