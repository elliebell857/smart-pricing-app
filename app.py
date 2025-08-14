import streamlit as st
import pandas as pd
from io import StringIO
from datetime import datetime, date
import os

# -----------------------------
# APP CONFIG (no custom theme)
# -----------------------------
st.set_page_config(page_title="Occasion Pricing Advisor", layout="centered")
st.title("Occasion Pricing Advisor")
st.caption("Upload an item, enter its original price, and get suggested rental prices by season/occasion.")

# -----------------------------
# DATA LOADING
# -----------------------------
REQUIRED_COLS = ["occasion", "user_type", "start_month", "end_month", "multiplier"]
OPTIONAL_COLS = ["notes"]

@st.cache_data
def load_calendar():
    """Load occasion_calendar.csv if present; otherwise use a sensible default table."""
    path = "occasion_calendar.csv"
    if os.path.exists(path):
        return pd.read_csv(path), True

    default_csv = """occasion,user_type,start_month,end_month,multiplier,notes
homecoming,highschool,9,10,1.25,Sept–Oct peak for short and midi dresses
prom,highschool,3,5,1.35,Mar–May very high demand for gowns and sparkly minis
winter_formal,highschool,12,1,1.15,Dec–Jan school formals/holiday parties
football_season,college,9,11,1.15,Game days and tailgates (school colors popular)
date_parties,college,10,4,1.10,Themed mixers and semi-formals
formals,college,11,4,1.25,Greek life and club formals
rush,college,8,8,1.20,Panhellenic recruitment (neutrals/white)
"""
    return pd.read_csv(StringIO(default_csv)), False

calendar_df, from_csv = load_calendar()

def validate_calendar(df: pd.DataFrame):
    missing = [c for c in REQUIRED_COLS if c not in df.columns]
    if missing:
        st.error(f"Your calendar is missing required columns: {missing}. "
                 f"Expected: {REQUIRED_COLS + OPTIONAL_COLS}")
        st.stop()

validate_calendar(calendar_df)

# Normalize numeric types
for c in ["start_month", "end_month"]:
    calendar_df[c] = pd.to_numeric(calendar_df[c], errors="coerce").astype("Int64")
calendar_df["multiplier"] = pd.to_numeric(calendar_df["multiplier"], errors="coerce")

# -----------------------------
# HELPERS (pricing math)
# -----------------------------
def material_adjust(material):
    return {
        "Silk": 1.10, "Satin": 1.07, "Lace": 1.05, "Sequin": 1.12,
        "Cotton": 1.00, "Polyester": 0.98, "Other": 1.00, "Unknown": 1.00,
    }.get(material, 1.00)

def condition_adjust(score: int):
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

def in_season(month, start_m, end_m):
    if pd.isna(start_m) or pd.isna(end_m):
        return False
    start_m, end_m = int(start_m), int(end_m)
    if start_m <= end_m:
        return start_m <= month <= end_m
    # wraps year end (e.g., Dec–Jan)
    return month >= start_m or month <= end_m

# -----------------------------
# SIDEBAR: PROFILE
# -----------------------------
with st.sidebar:
    st.header("Your Profile")
    user_type = st.radio("Are you in high school or college?", ["highschool", "college"])
    region = st.text_input("Region (optional)", value="Dallas, TX")
    st.caption("Tip: you can tweak occasion multipliers in occasion_calendar.csv.")
    if not from_csv:
        st.info("Using built-in defaults. Add occasion_calendar.csv next to app.py to customize.")

# -----------------------------
# MAIN: STEP 1 / 2 / 3 LAYOUT
# -----------------------------
st.subheader("1) Item details")
img = st.file_uploader("Upload an item image (optional)", type=["jpg","jpeg","png"])
c1, c2 = st.columns(2)
with c1:
    original_price = st.number_input("Enter original purchase price ($):", min_value=1.0, max_value=10000.0, value=250.0, step=1.0)
    condition = st.slider("Condition (1-poor to 5-excellent)", 1, 5, 5)
    material = st.selectbox("Material (optional)", ["Unknown","Silk","Satin","Cotton","Lace","Polyester","Sequin","Other"])
with c2:
    silhouette = st.selectbox("Silhouette (optional)", ["Unknown","mini","midi","gown","set","jumpsuit"])
    color = st.selectbox("Color (optional)", ["Unknown","black","white","pink","blue","red","green","gold","silver","other"])
    notes = st.text_area("Notes (damage, fit, brand, etc.)", placeholder="")

st.subheader("2) Pricing knobs (optional)")
base_pct = st.slider("Base rental % of retail", 5, 60, 30)
rush_markup = st.slider("Rush (< 4 days to event) markup %", 0, 60, 10)
weekend_markup = st.slider("Weekend event markup %", 0, 60, 5)

st.subheader("3) Event info (for rush/weekend)")
event_date = st.date_input("Next expected event date (optional)", value=None)
today = datetime.now().date()
days_to_event = (event_date - today).days if isinstance(event_date, date) else None
is_weekend = (event_date.weekday() >= 5) if isinstance(event_date, date) else False

# -----------------------------
# REPORT
# -----------------------------
if st.button("Generate Pricing Report"):
    # Filter calendar for user_type
    cal = calendar_df[calendar_df["user_type"] == user_type].copy()
    if cal.empty:
        st.warning(f"No rows for user_type = '{user_type}' in your calendar.")
        st.stop()

    # Base rental before occasion multiplier
    base_price = original_price * (base_pct/100.0)
    base_price *= material_adjust(material)
    base_price *= condition_adjust(condition)
    base_price *= silhouette_adjust(silhouette)
    base_price *= rush_weekend_multiplier(days_to_event, is_weekend, rush_markup, weekend_markup)

    # Per-occasion pricing
    current_month = today.month
    cal["in_season_now"] = cal.apply(lambda r: in_season(current_month, r["start_month"], r["end_month"]), axis=1)
    cal["suggested_price"] = (base_price * cal["multiplier"]).round(0)
    cal["low"] = (cal["suggested_price"] * 0.90).round(0)
    cal["high"] = (cal["suggested_price"] * 1.10).round(0)

    # Confidence (simple)
    conf = 70
    if material in ["Silk","Sequin"] and condition >= 4: conf += 5
    if silhouette == "gown": conf += 5
    cal["confidence_%"] = conf

    # ----- KPIs -----
    st.subheader("Summary")
    k1, k2, k3 = st.columns(3)
    k1.metric("Base rental (pre-season)", f"${base_price:.0f}")
    k2.metric("Rush/weekend applied",
              "Yes" if (days_to_event is not None and days_to_event <= 4) or is_weekend else "No")
    k3.metric("Occasions in season now", f"{int(cal['in_season_now'].sum())} of {len(cal)}")

    # ----- Simple recommendations -----
    in_season_df = cal[cal["in_season_now"]] if cal["in_season_now"].any() else cal
    mid = int(in_season_df["suggested_price"].median())
    lo = int(max(1, round(mid * 0.90)))
    hi = int(round(mid * 1.10))
    st.markdown("**Recommended listing ranges**")
    st.write(f"- Standard: **${mid}**")
    st.write(f"- Conservative: **${lo}**")
    st.write(f"- Premium: **${hi}**")

    # Optional short caption (kept simple)
    caption_bits = []
    if color != "Unknown": caption_bits.append(color)
    if silhouette != "Unknown": caption_bits.append(silhouette)
    if material != "Unknown": caption_bits.append(material.lower())
    caption_main = " • ".join([b.capitalize() for b in caption_bits]) or "Dress"
    st.markdown("**Suggested caption (copy/paste):**")
    st.write(f"{caption_main} — rental **${mid}** (range ${lo}–${hi}). {notes or ''}")

    # ----- Detailed table -----
    st.subheader("Detailed occasion table")
    show_cols = ["occasion","start_month","end_month","multiplier",
                 "suggested_price","low","high","in_season_now","confidence_%"]
    nice = {
        "occasion":"Occasion",
        "start_month":"Season start (mo)",
        "end_month":"Season end (mo)",
        "multiplier":"Occasion multiplier",
        "suggested_price":"Suggested price ($)",
        "low":"Low ($)",
        "high":"High ($)",
        "in_season_now":"In season now?",
        "confidence_%":"Confidence (%)",
    }
    table = cal[show_cols].rename(columns=nice)
    st.dataframe(table, use_container_width=True, hide_index=True)

    st.download_button(
        label="Download pricing table (CSV)",
        data=table.to_csv(index=False),
        file_name="pricing_report.csv",
        mime="text/csv"
    )

# -----------------------------
# OPTIONAL: show raw calendar
# -----------------------------
with st.expander("View your occasion calendar data"):
    preview_cols = [c for c in REQUIRED_COLS + OPTIONAL_COLS if c in calendar_df.columns]
    st.dataframe(calendar_df[preview_cols].sort_values(["user_type","start_month","occasion"]),
                 use_container_width=True, hide_index=True)
