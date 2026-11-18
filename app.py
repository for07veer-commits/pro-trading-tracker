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

# 1. Pehla Mahamantra
with st.popover("🏹 १. वीतरागभयक्रोधः (Na Lalach, Na Darr, Na Gussa)", use_container_width=True):
    st.markdown("""
        ### **वीतरागभयक्रोधः** *(Adhyay 2, Shlok 56)*
        * **Sanskrit Arth:** Jo asakti, darr aur krodh se poori tarah mukt ho chuka hai.
        * **Trading Meaning:** Lalach, Darr aur Gussa trading ke sabse bade dushman hain. Inse mukt hokar apne pre-marked zones par strict discipline ke sath trade execute karein.
    """)

# 2. Doosra Mahamantra
with st.popover("⚖️ २. कर्मण्येवाधिकारस्ते (Mera kaam sirf Rule follow karna hai...)", use_container_width=True):
    st.markdown("""
        ### **कर्मण्येवाधिकारस्ते** *(Adhyay 2, Shlok 47)*
        * **Sanskrit Arth:** Tumhara adhikar sirf karm karne par hai, uske phalon par kabhi nahi.
        * **Trading Meaning:** Aapka control sirf rules follow karne aur risk management par hai. Profit market ka prasad hai, aap sirf apne process par dhyan dein.
    """)

# 3. Teesra Mahamantra
with st.popover("⚔️ ३. युद्धाय कृतनिश्चयः (Ek Yoddha ki tarah bina emotions ke...)", use_container_width=True):
    st.markdown("""
        ### **युद्धाय कृतनिश्चयः** *(Adhyay 2, Shlok 38)*
        * **Sanskrit Arth:** Sukh-dukh aur labh-hani ko saman samajh kar yuddh ke liye taiyar ho jao.
        * **Trading Meaning:** Market ek jang ka maidan hai. Profit aur loss dono ko barabar accept karte hue bina kisi emotional baggage ke apne setup ka wait karein.
    """)

st.markdown("""
<div style="background: linear-gradient(90deg, #E8F5E9, #C8E6C9); padding: 16px 20px; border-radius: 12px; border: 2px solid #2E7D32; margin: 15px 0; text-align: center;">
    <p style="color: #1B5E20; font-size: 20px; font-weight: 800; margin:
