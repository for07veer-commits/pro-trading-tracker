import streamlit as st
import streamlit.components.v1 as components
import json
import os
import random
from datetime import datetime, timedelta, timezone

# App Settings
st.set_page_config(page_title="Pritika's Pro Trading Tracker", page_icon="📈", layout="centered")

# ==========================================
# GLOBAL HARA-BHARA & COLOURFUL CSS STYLING
# ==========================================
st.markdown("""
<style>
.stApp { background: linear-gradient(180deg, #F9FBF9 0%, #FFFDF7 100%); }
div[data-testid="stPopover"] > div > button {
    background: linear-gradient(90deg, #FFF8DC, #FFE4B5) !important;
    border: 2px solid #FF8C00 !important; border-radius: 12px !important;
    padding: 14px 20px !important; box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.12) !important;
}
div[data-testid="stPopover"] > div > button p {
    font-size: 21px !important; font-weight: 800 !important; color: #8B0000 !important;
}
div[data-testid="stPopover"] > div > button:hover {
    background: linear-gradient(90deg, #FFD700, #FFA500) !important; border-color: #8B0000 !important;
}
div[data-testid="stLinkButton"] > a {
    background: linear-gradient(90deg, #008080, #20B2AA) !important;
    color: #FFFFFF !important; border: 2px solid #004D40 !important;
    border-radius: 12px !important; padding: 12px 18px !important; font-weight: 800 !important;
}
div[data-testid="stLinkButton"] > a p { color: #FFFFFF !important; font-size: 18px !important; font-weight: bold !important; }
div.stButton > button, div[data-testid="stFormSubmitButton"] > button {
    background: linear-gradient(90deg, #1B5E20, #2E7D32, #43A047) !important;
    color: white !important; border: 2px solid #FFD700 !important;
    border-radius: 12px !important; padding: 12px 24px !important; width: 100% !important;
}
div.stButton > button p, div[data-testid="stFormSubmitButton"] > button p {
    font-size: 20px !important; font-weight: 800 !important; color: #FFFFFF !important;
}
div[data-testid="stCheckbox"] {
    background: linear-gradient(90deg, #E8F5E9, #F1F8E9);
    padding: 12px 16px; border-radius: 10px; border-left: 6px solid #2E7D32;
    border-right: 1px solid #C8E6C9; margin-bottom: 10px;
}
div[data-testid="stCheckbox"] label p { font-size: 18px !important; font-weight: 700 !important; color: #1B5E20 !important; }
div[data-testid="stExpander"] {
    border: 2px solid #2E7D32 !important; border-radius: 14px !important; background-color: #FAFFFA !important;
}
div[data-testid="stMetric"] {
    background: linear-gradient(135deg, #E8F5E9, #C8E6C9);
    border: 2px solid #2E7D32; border-radius: 12px; padding: 15px; text-align: center;
}
div[data-testid="stForm"] {
    background: linear-gradient(135deg, #F3E5F5, #E8EAF6);
    border: 2px solid #6A1B9A; border-radius: 14px; padding: 18px;
}
</style>
""", unsafe_allow_html=True)

# ==============================================================================
# 🔒 SMART 4-DIGIT PASSWORD, VALIDITY & STAGE-LIMIT ADMIN SYSTEM
# ==============================================================================
DEFAULT_ADMIN_PASS = "7777"
DB_FILE = "tracker_access_db.json"
IST = timezone(timedelta(hours=5, minutes=30))

@st.cache_resource
def get_memory_db():
    if os.path.exists(DB_FILE):
        try:
            with open(DB_FILE, "r") as f:
                return json.load(f)
        except Exception:
            pass
    return {"admin_pass": DEFAULT_ADMIN_PASS, "pins": {}}

def save_db(db):
    try:
        with open(DB_FILE, "w") as f:
            json.dump(db, f)
    except Exception:
        pass

db = get_memory_db()

def verify_pin(user_input):
    pin = str(user_input).strip()
    if not pin:
        return False, "", False, []
    
    if pin == db.get("admin_pass", DEFAULT_ADMIN_PASS):
        return True, "👑 Admin Mode Active (All Stages Unlocked)", True, ["1", "2", "3", "4", "5"]
    
    pins_data = db.get("pins", {})
    if pin in pins_data:
        info = pins_data[pin]
        exp_time = datetime.strptime(info["expiry"], "%Y-%m-%d %H:%M")
        now_ist = datetime.now(IST).replace(tzinfo=None)
        if now_ist > exp_time:
            return False, "⏳ Aapka 4-Digit PIN Expire ho chuka hai! Renew karne ke liye Pritika ji se sampark karein.", False, []
        allowed = info["stages"]
        stages_text = ", ".join([f"Stage {s}" for s in allowed])
        return True, f"✅ Active ({stages_text}) | Valid Till: {exp_time.strftime('%d %b %Y, %I:%M %p')}", False, allowed
    
    return False, "❌ Galat 4-Digit PIN! Kripya sahi password dalein.", False, []

if "saved_pass" not in st.session_state:
    st.session_state.saved_pass = ""

is_valid, status_msg, is_admin, allowed_stages = verify_pin(st.session_state.saved_pass)

# --- LOGIN SCREEN ---
if not is_valid:
    st.markdown("""
    <div style="text-align: center; background: linear-gradient(90deg, #004D40, #1B5E20, #2E7D32); padding: 18px; border-radius: 15px; border: 3px solid #FFD700; margin-bottom: 18px;">
        <h1 style="color: #FFD700; font-size: 34px; font-weight: 900; margin: 0;">🔒 Pritika's Pro Trading Tracker</h1>
    </div>
    """, unsafe_allow_html=True)
    st.info("🔑 App kholne ke liye apna **4-Digit Password** dalein (Admin Default: **7777**).")
    input_pass = st.text_input("Enter 4-Digit Password:", type="password", max_chars=20, placeholder="Example: 7777")
    if st.button("🔓 Unlock App"):
        ok, msg, adm, stg = verify_pin(input_pass)
        if ok:
            st.session_state.saved_pass = input_pass.strip()
            st.rerun()
        else:
            st.error(msg)
    st.stop()

# --- TOP ADMIN BAR ---
if is_admin:
    col_status, col_admin, col_logout = st.columns([5.5, 2.5, 2])
    with col_status:
        st.success(status_msg)
    with col_admin:
        admin_box = st.popover("👑 Admin", use_container_width=True) if hasattr(st, "popover") else st.expander("👑 Admin")
        with admin_box:
            st.markdown("### ⚡ 4-Digit Password Banayein")
            plan = st.radio("1. Plan Validity:", ["1 Day (24 Hours)", "1 Month (30 Days)", "1 Year (365 Days)"])
            st.markdown("**2. Stages Select Karein:**")
            st_s1 = st.checkbox("Stage 1: Pre-Market", value=True, key="adm_s1")
            st_s2 = st.checkbox("Stage 2: Live Market Rules", value=True, key="adm_s2")
            st_s3 = st.checkbox("Stage 3: Target Calculator", value=True, key="adm_s3")
            st_s4 = st.checkbox("Stage 4: Trade Diary", value=True, key="adm_s4")
            st_s5 = st.checkbox("Stage 5: Screen Recorder", value=True, key="adm_s5")
            custom_pin = st.text_input("3. Custom 4-Digit PIN (Optional):", max_chars=4, placeholder="Ex: 4582")
            selected_stages = [s for s, val in [("1", st_s1), ("2", st_s2), ("3", st_s3), ("4", st_s4), ("5", st_s5)] if val]
            
            if st.button("🔑 Create 4-Digit Password"):
                if not selected_stages:
                    st.warning("Kam se kam 1 Stage select karein!")
                elif custom_pin and (len(custom_pin) != 4 or not custom_pin.isdigit()):
                    st.warning("Sirf 4 digits ka number dalein!")
                else:
                    new_pin = custom_pin if custom_pin else str(random.randint(1000, 9999))
                    days_map = {"1 Day (24 Hours)": 1, "1 Month (30 Days)": 30, "1 Year (365 Days)": 365}
                    exp_dt = datetime.now(IST).replace(tzinfo=None) + timedelta(days=days_map[plan])
                    db["pins"][new_pin] = {"expiry": exp_dt.strftime("%Y-%m-%d %H:%M"), "stages": selected_stages, "plan": plan}
                    save_db(db)
                    stg_names = ", ".join([f"Stage {x}" for x in selected_stages])
                    st.success(f"✅ Naya PIN: **{new_pin}**")
                    st.code(f"🔗 App Link: https://pro-trading-tracker-ukcmgab2wnnufj9qzbse9s.streamlit.app/\n🔑 Password: {new_pin}\n🔓 Access: {stg_names}\n⏳ Valid till {exp_dt.strftime('%d %b %Y, %I:%M %p')}", language="markdown")
            
            if db.get("pins"):
                st.markdown("---")
                if st.button("🗑️ Clear All User Passwords"):
                    db["pins"] = {}
                    save_db(db)
                    st.rerun()

            st.markdown("---")
            st.markdown("### ⚙️ Apna Admin Password Badlein")
            new_admin_p = st.text_input("Naya Admin Password dalein:", placeholder="Ex: 9999")
            if st.button("💾 Save New Admin Password"):
                if new_admin_p.strip():
                    db["admin_pass"] = new_admin_p.strip()
                    save_db(db)
                    st.session_state.saved_pass = new_admin_p.strip()
                    st.success(f"✅ Saved!")
    with col_logout:
        if st.button("🚪 Logout"):
            st.session_state.saved_pass = ""
            st.rerun()
else:
    col_status, col_logout = st.columns([8, 2])
    with col_status:
        st.info(status_msg)
    with col_logout:
        if st.button("🚪 Logout"):
            st.session_state.saved_pass = ""
            st.rerun()

# ==========================================
# MAIN APP TITLE & GEETA MAHAMANTRAS
# ==========================================
st.markdown("""
<div style="text-align: center; background: linear-gradient(90deg, #004D40, #1B5E20, #2E7D32); padding: 18px; border-radius: 15px; border: 3px solid #FFD700; margin-bottom: 18px;">
    <h1 style="color: #FFD700; font-size: 38px; font-weight: 900; margin: 0;">📊 Pritika's Pro Trading Tracker</h1>
</div>
<div style="text-align: center; background: linear-gradient(90deg, #FFD700, #FF8C00); padding: 18px; border-radius: 15px; border: 3px solid #8B0000; margin-bottom: 20px;">
    <h1 style="color: #800000; font-size: 40px; font-weight: 900; margin: 0;">🕉️ गीता के ३ महामंत्र 🕉️</h1>
    <p style="color: #1a1a1a; font-size: 20px; font-weight: bold; margin: 5px 0 0 0;">(Trader's Mindset)</p>
</div>
""", unsafe_allow_html=True)

with st.popover("🏹 १. वीतरागभयक्रोधः (Na Lalach, Na Darr, Na Gussa)", use_container_width=True):
    st.markdown("**🎯 Trading Meaning:** Lalach, Darr aur Gussa trading ke sabse bade dushman hain. Inse mukt hokar apne pre-marked zones par strict discipline ke sath trade execute karein.")
with st.popover("⚖️ २. कर्मण्येवाधिकारस्ते (Mera kaam sirf Rule follow karna hai...)", use_container_width=True):
    st.markdown("**🎯 Trading Meaning:** Aapka control sirf rules follow karne aur risk management par hai. Profit market ka prasad hai, aap sirf apne process par dhyan dein.")
with st.popover("⚔️ ३. युद्धाय कृतनिश्चयः (Ek Yoddha ki tarah bina emotions ke...)", use_container_width=True):
    st.markdown("**🎯 Trading Meaning:** Market ek jang ka maidan hai. Profit aur loss dono ko barabar accept karte hue bina kisi emotional baggage ke apne setup ka wait karein.")

st.markdown("""
<div style="background: linear-gradient(90deg, #E8F5E9, #C8E6C9); padding: 16px 20px; border-radius: 12px; border: 2px solid #2E7D32; margin: 15px 0; text-align: center;">
    <p style="color: #1B5E20; font-size: 20px; font-weight: 800; margin: 0;">✨ "Main Pritika Veer, apne in trading rules ka 100% palan karungi. Capital ko bachana mera pehla dharam hai, aur profit banana doosra."</p>
</div>
""", unsafe_allow_html=True)

# QUICK LINKS
col1, col2 = st.columns(2)
with col1:
    st.link_button("📰 Open Veer Market News", "https://veer-market-news.streamlit.app", use_container_width=True)
with col2:
    st.link_button("🔎 Open Veer Master Scanner", "https://trading-scanner--veer-crty7rxlsxven92q2buuiy.streamlit.app/", use_container_width=True)

pm1 = pm2 = pm3 = pm4 = False
lm1 = lm2 = lm3 = lm4 = False

# ==========================================
# STAGE 1: PRE-MARKET & POWER NOTE
# ==========================================
if "1" in allowed_stages:
    st.write("")
    st.markdown("""
    <div style="background: linear-gradient(90deg, #1565C0, #1E88E5); padding: 14px 20px; border-radius: 12px; border-left: 8px solid #FFD700; margin-bottom: 15px;">
        <h3 style="color: #FFFFFF; font-size: 26px; font-weight: 800; margin: 0;">🌙 STAGE 1: Pre-Market & Data Analysis</h3>
    </div>
    """, unsafe_allow_html=True)
    pm1 = st.checkbox("1. FII/DII Data & Option Chain: Maine Veer News App mein aaj ka data analyze kar liya hai.")
    pm2 = st.checkbox("2. Zone Marking: 'Smart Structure & Liquidity' se zones mark kar liye hain.")
    pm3 = st.checkbox("3. Global Cues & Pre-Open: Gift Nifty aur 9:08 AM ka settlement dekh liya hai.")
    pm4 = st.checkbox("4. Tech Ready: Veer Master Scanner aur Dhan Power Scalper login karke ready hain.")

    with st.expander("⚡ Generate Today's Trading Power Note", expanded=True):
        s1, s2, s3 = st.columns(3)
        with s1: fii_data = st.selectbox("1. Veer News", ["Select...", "Bullish (Dono Buy)", "Bearish (Dono Sell)", "Mixed (Takkar)"])
        with s2: scanner_data = st.selectbox("2. Master Scanner", ["Select...", "CE (Long Setup)", "PE (Short Setup)", "No Clear Setup"])
        with s3: breath_data = st.selectbox("3. Market Breath", ["Select...", "Positive (+)", "Negative (-)", "Neutral"])
        
        if st.button("🔥 Generate Power Note"):
            if fii_data == "Bullish (Dono Buy)" and scanner_data == "CE (Long Setup)" and breath_data == "Positive (+)":
                st.success("🚀 **POWER NOTE:** Teeno tools BULLISH hain! Zone par NORMAL quantity mein Call (CE) dekhein.")
            elif fii_data == "Bearish (Dono Sell)" and scanner_data == "PE (Short Setup)" and breath_data == "Negative (-)":
                st.error("📉 **POWER NOTE:** Teeno tools BEARISH hain! Zone se NORMAL quantity mein Put (PE) dekhein.")
            else:
                st.warning("⚠️ **POWER NOTE (CAUTION):** Data mixed hai! Aaj ya toh TRADE NA LEIN, ya sirf HALF Quantity mein trade karein.")

# ==========================================
# STAGE 2: LIVE MARKET ROUTINE & SCORE
# ==========================================
if "2" in allowed_stages:
    st.write("")
    st.markdown("""
    <div style="background: linear-gradient(90deg, #B71C1C, #D84315); padding: 14px 20px; border-radius: 12px; border-left: 8px solid #FFD700; margin-bottom: 15px;">
        <h3 style="color: #FFFFFF; font-size: 26px; font-weight: 800; margin: 0;">🎯 STAGE 2: Live Market Entry</h3>
    </div>
    """, unsafe_allow_html=True)
    lm1 = st.checkbox("Rule 1: Trade strictly mere pre-marked 'ZONE' ke andar aa gaya hai (No FOMO).")
    lm2 = st.checkbox("Rule 2: Entry lene se pehle maine fix Stop Loss (SL) aur Target soch liya hai.")
    lm3 = st.checkbox("Rule 3: Aaj ki Max 3 Trades ki limit abhi bachi hui hai.")
    lm4 = st.checkbox("Rule 4: Main bina kisi Revenge ke, bilkul shant dimaag se trade le rahi hoon.")

    tasks = [pm1, pm2, pm3, pm4, lm1, lm2, lm3, lm4] if "1" in allowed_stages else [lm1, lm2, lm3, lm4]
    percentage = int((sum(tasks) / len(tasks)) * 100)

    st.progress(percentage)
    if percentage == 100:
        st.success("🟢 100% APPROVED: Sab kuch perfect hai. Aap apna trade execute kar sakti hain!")
    else:
        st.error(f"🔴 DO NOT TRADE! Abhi rules check karna bache hain.")

# ==========================================
# STAGE 3: TARGET ENFORCER & TAX CALCULATOR
# ==========================================
if "3" in allowed_stages:
    st.write("")
    st.markdown("""
    <div style="background: linear-gradient(90deg, #004D40, #00796B); padding: 14px 20px; border-radius: 12px; border-left: 8px solid #FFD700; margin-bottom: 12px;">
        <h3 style="color: #FFFFFF; font-size: 26px; font-weight: 800; margin: 0;">🛡️ STAGE 3: Target Enforcer & Position Sizing</h3>
    </div>
    """, unsafe_allow_html=True)
    with st.expander("🧮 Calculate Safe Lots, Exact Taxes & Target", expanded=True):
        c1, c2 = st.columns(2)
        with c1:
            risk_amount = st.number_input("Max Loss (₹)", min_value=100, value=1000, step=100)
            sl_points = st.number_input("Stop Loss (Points)", min_value=1, value=20, step=1)
        with c2:
            lot_size = st.number_input("Current Lot Size", min_value=1, value=15, step=1)
            buy_price = st.number_input("Option Buy Price", min_value=1, value=300, step=1)
        if st.button("Calculate Exact Tax & Target"):
            ideal_qty = int(risk_amount / sl_points)
            safe_lots = ideal_qty // lot_size
            final_qty = safe_lots * lot_size
            if safe_lots > 0:
                target_points = sl_points * 2
                sell_price = buy_price + target_points
                total_turnover = (buy_price * final_qty) + (sell_price * final_qty)
                total_taxes = round(40 + (sell_price * final_qty * 0.001) + (total_turnover * 0.0003503) + ((40 + (total_turnover * 0.0003503)) * 0.18), 2)
                net_profit = round((target_points * final_qty) - total_taxes, 2)
                st.info(f"✅ Safe Limit: **{safe_lots} Lots** (**{final_qty} Qty**) | Max Loss: **₹{risk_amount}**")
                bc1, bc2, bc3 = st.columns(3)
                bc1.metric("Brokerage + Taxes", f"₹{total_taxes}")
                bc2.metric("Target (1:2)", f"₹{sell_price}")
                bc3.metric("Net Profit", f"₹{net_profit}")
            else:
                st.error("🚨 DO NOT TRADE! Stop Loss aapke Risk limit se bada hai.")

# ==========================================
# STAGE 4: MARKET MAUSAM & DIARY
# ==========================================
if "4" in allowed_stages:
    st.write("")
    st.markdown("""
    <div style="background: linear-gradient(90deg, #0277BD, #00ACC1); padding: 14px 20px; border-radius: 12px; border-left: 8px solid #FFD700; margin-bottom: 15px;">
        <h3 style="color: #FFFFFF; font-size: 26px; font-weight: 800; margin: 0;">🌤️ STAGE 4: Market Mausam & Emotion Tracker</h3>
    </div>
    """, unsafe_allow_html=True)
    col3, col4 = st.columns(2)
    with col3:
        weather = st.radio("Market Direction:", ["☀️ Clear (Strong Trend)", "🌫️ Foggy (Sideways)", "🌧️ Stormy (Volatile)"])
    with col4:
        with st.form("trade_journal"):
            trade_pnl = st.number_input("Trade ka PnL (₹)", value=0)
            reason = st.selectbox("Reason:", ["Rule Followed", "FOMO", "Revenge", "Boredom"])
            if st.form_submit_button("💾 Save Trade Record"):
                st.success(f"Saved! PnL: ₹{trade_pnl} ({reason})")

# ==========================================
# STAGE 5: LIVE TRADE SCREEN & VOICE RECORDER (Aapka Original Bada Code)
# ==========================================
if "5" in allowed_stages:
    st.write("")
    st.markdown("""
    <div style="background: linear-gradient(90deg, #880E4F, #C2185B); padding: 14px 20px; border-radius: 12px; border-left: 8px solid #FFD700; margin-bottom: 12px; box-shadow: 0px 4px 10px rgba(0,0,0,0.15);">
        <h3 style="color: #FFFFFF; font-size: 26px; font-weight: 800; margin: 0;">
            🎥 STAGE 5: Live Trade Screen & Voice Recorder
        </h3>
        <p style="color: #FCE4EC; font-size: 16px; margin: 4px 0 0 0;">
            Apni pasand ka Audio Mode chunein (Sirf Mic, Sirf Computer, ya Dono Ek Sath) aur Live Trade record karein:
        </p>
    </div>
    """, unsafe_allow_html=True)

    components.html("""
    <div style="background: linear-gradient(135deg, #E8F5E9, #FFF8E1); border: 2px solid #2E7D32; border-radius: 14px; padding: 18px; text-align: center; font-family: sans-serif; box-shadow: 0px 4px 10px rgba(0,0,0,0.1);">
        
        <!-- Audio Mode Selector -->
        <div style="margin-bottom: 14px;">
            <div style="font-size: 17px; font-weight: 800; color: #1B5E20; margin-bottom: 8px;">
                🎧 Step 1: Aawaz (Audio) Ka Option Chunein:
            </div>
            <div style="display: grid; grid-template-columns: repeat(2, 1fr); gap: 8px; max-width: 620px; margin: 0 auto;">
                <label style="background: #FFFFFF; border: 2px solid #2E7D32; border-radius: 10px; padding: 10px; cursor: pointer; font-weight: bold; color: #1B5E20; font-size: 15px; display: flex; align-items: center; justify-content: center; gap: 6px;">
                    <input type="radio" name="audioMode" value="both" checked style="transform: scale(1.2);">
                    🎙️+💻 Dono Ek Sath (Mic + PC)
                </label>
                <label style="background: #FFFFFF; border: 2px solid #1565C0; border-radius: 10px; padding: 10px; cursor: pointer; font-weight: bold; color: #0D47A1; font-size: 15px; display: flex; align-items: center; justify-content: center; gap: 6px;">
                    <input type="radio" name="audioMode" value="mic" style="transform: scale(1.2);">
                    🎙️ Sirf Meri Aawaz (Mic Only)
                </label>
                <label style="background: #FFFFFF; border: 2px solid #6A1B9A; border-radius: 10px; padding: 10px; cursor: pointer; font-weight: bold; color: #4A148C; font-size: 15px; display: flex; align-items: center; justify-content: center; gap: 6px;">
                    <input type="radio" name="audioMode" value="system" style="transform: scale(1.2);">
                    💻 Sirf Computer Ki Aawaz
                </label>
                <label style="background: #FFFFFF; border: 2px solid #757575; border-radius: 10px; padding: 10px; cursor: pointer; font-weight: bold; color: #424242; font-size: 15px; display: flex; align-items: center; justify-content: center; gap: 6px;">
                    <input type="radio" name="audioMode" value="none" style="transform: scale(1.2);">
                    🔇 Bina Aawaz (Only Video)
                </label>
            </div>
        </div>

        <div id="status" style="font-size: 16px; font-weight: bold; color: #1B5E20; background: #C8E6C9; padding: 8px 12px; border-radius: 8px; margin-bottom: 14px;">
            🟢 Ready to Record (Upar Aawaz chunein aur Start Recording dabayein)
        </div>
        
        <!-- Action Buttons -->
        <div style="display: flex; gap: 12px; justify-content: center; flex-wrap: wrap; margin-bottom: 10px;">
            <button id="startBtn" onclick="startRecording()" style="background: linear-gradient(90deg, #1B5E20, #43A047); color: white; border: 2px solid #FFD700; border-radius: 10px; padding: 12px 22px; font-size: 17px; font-weight: bold; cursor: pointer; box-shadow: 0px 3px 6px rgba(0,0,0,0.2);">
                🔴 Start Recording
            </button>
            <button id="stopBtn" onclick="stopRecording()" style="background: linear-gradient(90deg, #B71C1C, #E53935); color: white; border: 2px solid #FFD700; border-radius: 10px; padding: 12px 22px; font-size: 17px; font-weight: bold; cursor: pointer; box-shadow: 0px 3px 6px rgba(0,0,0,0.2);">
                ⏹️ Stop Recording
            </button>
            <a id="downloadLink" style="display: none; background: linear-gradient(90deg, #0D47A1, #1976D2); color: white; border: 2px solid #FFD700; border-radius: 10px; padding: 12px 22px; font-size: 17px; font-weight: bold; text-decoration: none; box-shadow: 0px 3px 6px rgba(0,0,0,0.2);">
                💾 Download Trade Video
            </a>
        </div>

        <video id="preview" autoplay muted playsinline style="width: 100%; max-height: 200px; border-radius: 10px; border: 2px solid #1B5E20; display: none; background: #000; margin-top: 8px;"></video>
    </div>

    <script>
    const store = window.parent || window;

    function bindActiveRecording() {
        const statusEl = document.getElementById('status');
        const preview = document.getElementById('preview');
        
        if (store._pritikaRecorder) {
            store._pritikaRecorder.onstop = function() { finalizeRecording(); };
        }
        if (store._pritikaDisplayStream && store._pritikaDisplayStream.getVideoTracks().length > 0) {
            store._pritikaDisplayStream.getVideoTracks()[0].onended = function() { stopRecording(); };
        }
        if (store._pritikaRecorder && store._pritikaRecorder.state === 'recording') {
            statusEl.innerHTML = store._pritikaStatusText || '🔴 LIVE RECORDING CHALU HAI...';
            statusEl.style.color = '#B71C1C';
            statusEl.style.background = '#FFCDD2';
            if (store._pritikaDisplayStream) {
                preview.srcObject = store._pritikaDisplayStream;
                preview.style.display = 'block';
            }
        }
    }

    function finalizeRecording() {
        const statusEl = document.getElementById('status');
        const preview = document.getElementById('preview');
        const downloadLink = document.getElementById('downloadLink');
        
        if (store._pritikaChunks && store._pritikaChunks.length > 0) {
            const blob = new Blob(store._pritikaChunks, { type: 'video/webm' });
            const url = URL.createObjectURL(blob);
            const now = new Date().toISOString().slice(0,19).replace(/[:T]/g, "-");
            const filename = `Pritika_Trade_Recording_${now}.webm`;
            
            if (downloadLink) {
                downloadLink.href = url; downloadLink.download = filename;
                downloadLink.style.display = 'inline-block'; downloadLink.click();
            }
            if (statusEl) {
                statusEl.innerHTML = '✅ Recording Complete & Video Downloaded!';
                statusEl.style.color = '#0D47A1'; statusEl.style.background = '#BBDEFB';
            }
        } else if (statusEl) {
            statusEl.innerHTML = '⏹️ Recording Ruk Gayi Hai.';
            statusEl.style.color = '#1B5E20'; statusEl.style.background = '#C8E6C9';
        }
        if (preview) preview.style.display = 'none';
    }

    async function startRecording() {
        const statusEl = document.getElementById('status');
        const modeEl = document.querySelector('input[name="audioMode"]:checked');
        const mode = modeEl ? modeEl.value : 'both';

        try {
            if (store._pritikaRecorder && store._pritikaRecorder.state === 'recording') {
                stopRecording();
            }
            
            const mediaDevices = (store.navigator && store.navigator.mediaDevices) ? store.navigator.mediaDevices : navigator.mediaDevices;
            let micStream = null;
            let displayStream = null;

            if (mode === 'mic' || mode === 'both') {
                try {
                    micStream = await mediaDevices.getUserMedia({ audio: true, video: false });
                } catch (micErr) {
                    if (mode === 'mic') {
                        statusEl.innerHTML = '⚠️ Mic Permission Denied!';
                        return;
                    }
                }
            }

            const wantSystemAudio = (mode === 'system' || mode === 'both');
            displayStream = await mediaDevices.getDisplayMedia({ video: { cursor: "always" }, audio: wantSystemAudio });

            const hasMic = micStream && micStream.getAudioTracks().length > 0;
            const hasSys = displayStream && displayStream.getAudioTracks().length > 0;
            const tracks = [...displayStream.getVideoTracks()];

            if (hasMic && hasSys) {
                const AudioCtx = store.AudioContext || store.webkitAudioContext || window.AudioContext;
                const audioCtx = new AudioCtx();
                if (audioCtx.state === 'suspended') await audioCtx.resume();
                const dest = audioCtx.createMediaStreamDestination();
                audioCtx.createMediaStreamSource(displayStream).connect(dest);
                audioCtx.createMediaStreamSource(micStream).connect(dest);
                tracks.push(...dest.stream.getAudioTracks());
                store._pritikaAudioCtx = audioCtx;
                store._pritikaStatusText = '🔴 LIVE RECORDING: 🎙️ Meri Aawaz + 💻 Computer Aawaz DONO ON Hain!';
            } else if (hasMic) {
                tracks.push(...micStream.getAudioTracks());
                store._pritikaStatusText = '🔴 LIVE RECORDING: 🎙️ Meri Aawaz ON Hai';
            } else if (hasSys) {
                tracks.push(...displayStream.getAudioTracks());
                store._pritikaStatusText = '🔴 LIVE RECORDING: 💻 Sirf Computer Ki Aawaz Record Ho Rahi Hai!';
            } else {
                store._pritikaStatusText = '🔴 LIVE RECORDING: 🔇 Bina Aawaz (Only Video) Record Ho Raha Hai!';
            }

            const combinedStream = new MediaStream(tracks);
            store._pritikaDisplayStream = displayStream;
            store._pritikaMicStream = micStream;
            store._pritikaStream = combinedStream;
            store._pritikaChunks = [];

            let options = { mimeType: 'video/webm;codecs=vp8,opus' };
            if (!MediaRecorder.isTypeSupported(options.mimeType)) options = { mimeType: 'video/webm' };
            
            const recorder = new MediaRecorder(combinedStream, options);
            store._pritikaRecorder = recorder;
            recorder.ondataavailable = function(e) { if (e.data && e.data.size > 0) store._pritikaChunks.push(e.data); };
            
            bindActiveRecording();
            recorder.start(1000);
            document.getElementById('downloadLink').style.display = 'none';
            
        } catch (err) {
            statusEl.innerHTML = '⚠️ Screen select karke Share dabayein!';
            statusEl.style.color = '#E65100'; statusEl.style.background = '#FFE0B2';
        }
    }

    function stopRecording() {
        try {
            if (store._pritikaRecorder) {
                store._pritikaRecorder.onstop = function() { finalizeRecording(); };
                if (store._pritikaRecorder.state !== 'inactive') store._pritikaRecorder.stop();
                else finalizeRecording();
            } else finalizeRecording();
            
            if (store._pritikaStream) store._pritikaStream.getTracks().forEach(t => t.stop());
            if (store._pritikaDisplayStream) store._pritikaDisplayStream.getTracks().forEach(t => t.stop());
            if (store._pritikaMicStream) store._pritikaMicStream.getTracks().forEach(t => t.stop());
            if (store._pritikaAudioCtx && store._pritikaAudioCtx.state !== 'closed') store._pritikaAudioCtx.close();
        } catch (e) { finalizeRecording(); }
    }

    bindActiveRecording();
    </script>
    """, height=430)
