import streamlit as st
import pandas as pd
from io import StringIO
from datetime import datetime
import os

# =========================
# THEME & STYLES
# =========================
st.set_page_config(page_title="Occasion Pricing Advisor", layout="centered")

st.markdown("""
    <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;600;700&family=Playfair+Display:wght@500;700&display=swap" rel="stylesheet">
    <style>
    html, body, [class*="css"] { font-family: 'Poppins', sans-serif; color:#222; }
    h1, h2, h3 { font-family: 'Playfair Display', serif; color: #7A2E8E; font-weight: 700; }

    /* App background gradient */
    .stApp { background: linear-gradient(135deg, #ffe6f0, #fff5e6); }

    /* Sidebar */
    [data-testid="stSidebar"] { background-color: #fff0f5; }

    /* Section cards */
    .card {
        background: rgba(255,255,255,0.92);
        border-radius: 16px;
        padding: 18px 18px;
        box-shadow: 0 8px 24px rgba(0,0,0,0.06);
        border: 1px solid rgba(122,46,142,0.10);
        margin-bottom: 16px;
    }
    .divider {
        height: 1px;
        background: linear-gradient(to right, rgba(122,46,142,0.35), rgba(255,255,255,0));
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
        background: rgba(255,255,255,0.95);
        border-radius: 12px; padding: 14px; border: 1px dashed #e3b9c6;
    }

    /* Dataframe tweaks */
    .stDataFrame { background: rgba(255,255,255,0.95) !important; border-radius: 12px; padding: 6px; }
    </style>
""", unsafe_allow_html=True)

st.title("Occasion Pricing Advisor")
st.caption("Upload an item, enter retail price and notes, and get suggested rental prices by season/occasion. Clear summary + detailed table. No code output.")

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
    st.warning("`occasion_calendar.csv` not found — using built‑in defaults. Add the CSV to your repo root to customize.")
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
    if start_m <= end_m:
        return start_m <= month <= end_m
    # season wraps year end (e.g., Dec–Jan)
    return month >= start_m or month <= end_m

# =========================
# LAYOUT: INPUT CARDS
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
if img:
    st.image(img, caption="Uploaded item", use_column_width=True)
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
# REPORT: CLEAR KPIs + SUMMARY + TABLE (NO CODE BLOCKS)
# =========================
if generate:
    # 1) Base build
    base_price = original_price * (base_pct/100.0)
    base_price *= material_adjust(material)
    base_price *= condition_adjust(condition)
    base_price *= silhouette_adjust(silhouette)
    base_price *= rush_weekend_multiplier(days_to_event, is_weekend, rush_markup, weekend_markup)

    # 2) Occasion rows (filtered by user type)
    df = calendar[calendar["user_type"] == user_type].copy()

    # Season flag (now)
    current_month = today.month
    df["in_season_now"] = df.apply(
        lambda r: in_season(current_month, int(r["start_month"]), int(r["end_month"])), axis=1
    )

    # Suggested price per occasion
    df["suggested_price"] = (base_price * df["multiplier"]).round(0)
    df["low"] = (df["suggested_price"] * 0.90).round(0)
    df["high"] = (df["suggested_price"] * 1.10).round(0)

    # Simple confidence score that is easy to understand
    conf = 70
    if material in ["Silk","Sequin"] and condition >= 4: conf += 5
    if silhouette == "gown": conf += 5
    df["confidence_%"] = conf

    # 3) Quick KPIs (plain English)
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.subheader("Pricing Summary")
    k1, k2, k3 = st.columns(3)
    k1.metric("Base rental before season", f"${base_price:.0f}")
    k2.metric("Rush/weekend applied", "Yes" if (days_to_event is not None and days_to_event <= 4) or is_weekend else "No")
    k3.metric("In-season occasions now", f"{int(df['in_season_now'].sum())} of {len(df)}")
    st.markdown("<div class='divider'></div>", unsafe_allow_html=True)

    # 4) Simple recommendations anyone can follow
    #    Use medians of in-season suggestions, fall back to all if none in-season
    in_season_df = df[df["in_season_now"]] if df["in_season_now"].any() else df
    mid = int(in_season_df["suggested_price"].median())
    lo = int(max(1, round(mid * 0.9)))
    hi = int(round(mid * 1.1))

    st.markdown("**Recommended listing ranges**")
    st.write(
        f"- Standard: **${mid}** (most typical for similar items right now)\n"
        f"- Conservative: **${lo}** (to rent faster)\n"
        f"- Premium: **${hi}** (if demand looks high or item is special)"
    )

    # Optional short caption the user can copy
    st.markdown("<div class='divider'></div>", unsafe_allow_html=True)
    st.markdown("**Suggested listing caption (copy/paste):**")
    caption_bits = []
    if color != "Unknown": caption_bits.append(color)
    if silhouette != "Unknown": caption_bits.append(silhouette)
    if material != "Unknown": caption_bits.append(material.lower())
    caption_main = " • ".join([b.capitalize() for b in caption_bits]) or "Dress"
    st.write(
        f"{caption_main} — rental **${mid}** (range ${lo}–${hi}). "
        f"Great for {', '.join(df[df['in_season_now']]['occasion'].tolist()) or 'upcoming events'}. "
        f"{notes or ''}"
    )

    # 5) Full table with clear headers
    st.markdown("<div class='divider'></div>", unsafe_allow_html=True)
    st.subheader("Detailed occasion table")
    display_cols = [
        "occasion","start_month","end_month","multiplier",
        "suggested_price","low","high","in_season_now","confidence_%"
    ]
    # Rename columns for clarity
    rename_map = {
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
    display_df = df[display_cols].rename(columns=rename_map)
    st.dataframe(display_df, use_container_width=True, hide_index=True)

    st.download_button(
        "Download pricing table as CSV",
        data=display_df.to_csv(index=False),
        file_name="pricing_report.csv",
        mime="text/csv"
    )

    # 6) How it works — short, plain-English
    with st.expander("How these prices are calculated (plain English)"):
        st.write(
            "- Start from a percentage of retail price you chose under “Base rental % of retail”.\n"
            "- Adjust for material, condition, and silhouette.\n"
            "- If your event is within 4 days or on a weekend, a rush/weekend markup is applied.\n"
            "- Finally, multiply by each occasion’s seasonal multiplier (from your calendar file)."
        )
        st.info("You can change season multipliers by editing `occasion_calendar.csv`.")

    # 7) Quick tips
    with st.expander("Quick tips"):
        st.write(
            "- If similar listings in your area sit for more than a week, try the Conservative price.\n"
            "- If you’re getting lots of messages immediately, try the Premium price next time.\n"
            "- Condition 5 and premium materials (silk/sequin) can justify the higher end of the range."
        )
    st.markdown("</div>", unsafe_allow_html=True)
