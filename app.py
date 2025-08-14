import os
from io import StringIO
from datetime import datetime, date

import pandas as pd
import streamlit as st

# =========================
# PAGE SETUP + INLINE THEME (high-contrast pink theme)
# =========================
st.set_page_config(page_title="Occasion Pricing Advisor", page_icon=":dancer:", layout="centered")

st.markdown(
    """
    <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;600;700&family=Playfair+Display:wght@600;700&display=swap" rel="stylesheet">
    <style>
      /* Fonts & base text color for contrast */
      html, body, [class*="css"] { font-family: 'Poppins', sans-serif; color:#2E0B37; }
      h1, h2, h3 { font-family: 'Playfair Display', serif; color:#6C2A7A; font-weight:700; }

      /* Soft pink gradient background */
      .stApp { background: linear-gradient(135deg, #FFE6F0, #FFF5E6); }

      /* Sidebar */
      [data-testid="stSidebar"] { background:#FFF0F5; border-right:1px solid rgba(108,42,122,0.10); }

      /* Card helpers (use with wrappers below) */
      .card {
        background: rgba(255,255,255,0.94);
        border: 1px solid rgba(108,42,122,0.08);
        border-radius: 14px;
        padding: 16px;
        box-shadow: 0 10px 24px rgba(0,0,0,0.06);
        margin: 10px 0 16px;
      }
      .divider {
        height:1px; margin:10px 0 6px;
        background: linear-gradient(90deg, rgba(108,42,122,0.25), rgba(255,255,255,0));
      }

      /* Buttons */
      .stButton>button{
        background:#FF85A2; color:#ffffff; border:none; border-radius:12px;
        padding:.6em 1.15em; font-size:1rem;
        box-shadow: 0 6px 16px rgba(255,133,162,.35);
        transition: all .2s ease;
      }
      .stButton>button:hover { background:#E75480; transform: translateY(-1px) scale(1.02); }

      /* Inputs */
      .stTextInput>div>div>input, .stNumberInput input, .stSelectbox div[data-baseweb="select"]>div {
        background:#FFFFFF; border-radius:10px; border:1px solid #E3E3E3;
      }

      /* File uploader */
      [data-testid="stFileUploader"]{
        background: rgba(255,255,255,.96);
        border-radius: 12px; padding: 12px;
        border:1px dashed #E3B9C6;
      }

      /* Data table container */
      .stDataFrame { background:rgba(255,255,255,.96) !important; border-radius:12px; padding:6px; }
    </style>
    """,
    unsafe_allow_html=True,
)

st.title("Occasion Pricing Advisor")
st.caption("Upload an item, enter its original price, and get suggested rental prices by season/occasion.")

# =========================
# OCCASION CALENDAR LOADING (CSV or built-in defaults)
# Robust to different column names (Occasion vs occasion, etc.)
# =========================
@st.cache_data
def load_calendar() -> pd.DataFrame:
    path = "occasion_calendar.csv"
    if os.path.exists(path):
        df = pd.read_csv(path)
    else:
        default_csv = """occasion,user_type,start_month,end_month,multiplier,notes
homecoming,highschool,9,10,1.25,Sept-Oct peak for short and midi dresses
prom,highschool,3,5,1.35,Mar-May very high demand for gowns and sparkly minis
winter_formal,highschool,12,1,1.15,Dec-Jan school formals/holiday parties
football_season,college,9,11,1.15,Game days and tailgates (school colors popular)
date_parties,college,10,4,1.10,Themed mixers and semi-formals
formals,college,11,4,1.25,Greek life and club formals
rush,college,8,8,1.20,Panhellenic recruitment (neutrals/white)
"""
        st.warning(
            "`occasion_calendar.csv` not found — using built‑in defaults. "
            "Add a CSV in the repo root to customize seasons/multipliers."
        )
        df = pd.read_csv(StringIO(default_csv))

    # Normalize column names to lowercase and strip spaces
    df.columns = [c.strip().lower() for c in df.columns]

    # Map common alternatives to expected names
    rename_map = {}
    colset = set(df.columns)
    def pick(one, alts):
        for name in [one] + alts:
            if name in colset:
                return name
        return None

    occ = pick("occasion", ["occasions", "event", "season"])
    usr = pick("user_type", ["user type", "usertype", "school_level", "segment"])
    sm  = pick("start_month", ["start", "startmonth", "start_mon"])
    em  = pick("end_month", ["end", "endmonth", "end_mon"])
    mul = pick("multiplier", ["factor", "season_multiplier", "mult"])
    nts = pick("notes", ["note", "comment"])

    expected = {"occasion": occ, "user_type": usr, "start_month": sm, "end_month": em, "multiplier": mul, "notes": nts}
    for want, have in expected.items():
        if have and have != want:
            rename_map[have] = want
    if rename_map:
        df = df.rename(columns=rename_map)

    # Basic validation
    required = ["occasion", "start_month", "end_month", "multiplier"]
    for r in required:
        if r not in df.columns:
            raise ValueError(f"Calendar is missing required column: {r}")

    # Ensure numeric columns are numeric
    for c in ["start_month", "end_month", "multiplier"]:
        df[c] = pd.to_numeric(df[c], errors="coerce")

    # Drop rows with missing essentials
    df = df.dropna(subset=["occasion", "start_month", "end_month", "multiplier"]).reset_index(drop=True)
    return df

calendar = load_calendar()

# =========================
# SIDEBAR: USER PROFILE
# =========================
st.sidebar.header("Your Profile")
user_type = st.sidebar.radio("Are you in high school or college?", ["highschool", "college"])
region = st.sidebar.text_input("Region (optional)", value="Dallas, TX")
st.sidebar.markdown("---")
st.sidebar.caption("Tip: customize season multipliers in `occasion_calendar.csv`.")

# =========================
# INPUT CARDS
# =========================
st.markdown("<div class='card'>", unsafe_allow_html=True)
st.subheader("1) Item details")
st.file_uploader("Upload a photo (JPG/PNG) — optional", type=["jpg", "jpeg", "png"])  # not used yet; kept for future
c1, c2 = st.columns(2)
with c1:
    original_price = st.number_input("Original retail price ($)", min_value=10.0, max_value=5000.0, value=250.0, step=5.0)
    condition = st.slider("Condition (1–5)", 1, 5, 5)
    material = st.selectbox("Material (optional)", ["Unknown", "Silk", "Satin", "Cotton", "Lace", "Polyester", "Sequin", "Other"])
with c2:
    silhouette = st.selectbox("Silhouette (optional)", ["Unknown", "mini", "midi", "gown", "set", "jumpsuit"])
    st.selectbox("Color (optional)", ["Unknown", "black", "white", "pink", "blue", "red", "green", "gold", "silver", "other"])
    st.text_area("Notes (damage, material, brand, etc.)")
st.markdown("</div>", unsafe_allow_html=True)

st.markdown("<div class='card'>", unsafe_allow_html=True)
st.subheader("2) Pricing knobs (optional)")
base_pct = st.slider("Base rental % of retail", 5, 50, 30, help="Starting point before season/condition adjustments")
rush_markup = st.slider("Rush markup % (≤4 days to event)", 0, 50, 10)
weekend_markup = st.slider("Weekend event markup %", 0, 40, 5)
st.markdown("</div>", unsafe_allow_html=True)

st.markdown("<div class='card'>", unsafe_allow_html=True)
st.subheader("3) Event info (for rush/weekend logic)")
event_date = st.date_input("Next expected event date (optional)")
today = datetime.now().date()
days_to_event = (event_date - today).days if event_date else None
is_weekend = event_date.weekday() >= 5 if event_date else False
st.markdown("</div>", unsafe_allow_html=True)

# =========================
# PRICING ADJUSTMENT HELPERS
# =========================
def material_adjust(name: str) -> float:
    return {
        "Silk": 1.10, "Satin": 1.07, "Lace": 1.05, "Sequin": 1.12,
        "Cotton": 1.00, "Polyester": 0.98, "Other": 1.00, "Unknown": 1.00,
    }.get(name, 1.00)

def condition_adjust(score: int) -> float:
    return {1: 0.75, 2: 0.85, 3: 0.93, 4: 1.00, 5: 1.05}[int(score)]

def silhouette_adjust(sil: str) -> float:
    return {"mini": 1.00, "midi": 1.05, "gown": 1.15, "set": 1.02, "jumpsuit": 0.95, "Unknown": 1.00}.get(sil, 1.00)

def rush_weekend_multiplier(days, weekend: bool, rush_pct: int, weekend_pct: int) -> float:
    mult = 1.0
    if days is not None and days <= 4:
        mult *= (1 + rush_pct / 100.0)
    if weekend:
        mult *= (1 + weekend_pct / 100.0)
    return mult

# =========================
# GENERATE REPORT (TABLE ONLY)
# =========================
st.markdown("<div class='card'>", unsafe_allow_html=True)
generate = st.button("Generate Pricing Report")
st.markdown("</div>", unsafe_allow_html=True)

if generate:
    # Base rental before season multipliers
    base_price = original_price * (base_pct / 100.0)
    base_price *= material_adjust(material)
    base_price *= condition_adjust(condition)
    base_price *= silhouette_adjust(silhouette)
    base_price *= rush_weekend_multiplier(days_to_event, is_weekend, rush_markup, weekend_markup)

    # Filter by user type if the calendar has that column
    df = calendar.copy()
    if "user_type" in df.columns:
        mask = df["user_type"].astype(str).str.lower() == user_type
        if mask.any():
            df = df[mask].copy()

    # In-season flag (current month)
    month = today.month
    df["in_season_now"] = (
        ((df["start_month"] <= df["end_month"]) & ((month >= df["start_month"]) & (month <= df["end_month"]))) |
        ((df["start_month"] > df["end_month"])  & ((month >= df["start_month"]) | (month <= df["end_month"])))
    )

    # Suggested prices & bands
    df["suggested_price"] = (base_price * df["multiplier"]).round(0)
    df["low"] = (df["suggested_price"] * 0.90).round(0)
    df["high"] = (df["suggested_price"] * 1.10).round(0)

    # Simple confidence score
    conf = 70
    if material in ["Silk", "Sequin"] and condition >= 4:
        conf += 5
    if silhouette == "gown":
        conf += 5
    df["confidence_%"] = conf

    # Table-only output (readable, high contrast)
    display_cols = ["occasion", "start_month", "end_month", "multiplier",
                    "suggested_price", "low", "high", "in_season_now", "confidence_%"]
    # Keep only columns that exist (in case notes/user_type missing)
    display_cols = [c for c in display_cols if c in df.columns]
    st.dataframe(df[display_cols], use_container_width=True, hide_index=True)
