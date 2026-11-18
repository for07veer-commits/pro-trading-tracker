import streamlit as st

# App Settings
st.set_page_config(page_title="Pritika's Pro Trading Tracker", page_icon="📈", layout="centered")

# ==========================================
# GLOBAL HARA-BHARA & COLOURFUL CSS STYLING
# ==========================================
st.markdown("""
<style>
/* App Background */
.stApp {
    background: linear-gradient(180deg, #F9FBF9 0%, #FFFDF7 100%);
}

/* Geeta Mantra Popover Buttons */
div[data-testid="stPopover"] > div > button {
    background: linear-gradient(90deg, #FFF8DC, #FFE4B5) !important;
    border: 2px solid #FF8C00 !important;
    border-radius: 12px !important;
    padding: 14px 20px !important;
    box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.12) !important;
}
div[data-testid="stPopover"] > div > button p {
    font-size: 21px !important;
    font-weight: 800 !important;
    color: #8B0000 !important;
}
div[data-testid="stPopover"] > div > button:hover {
    background: linear-gradient(90deg, #FFD700, #FFA500) !important;
    border-color: #8B0000 !important;
}

/* Master Tool Link Buttons */
div[data-testid="stLinkButton"] > a {
    background: linear-gradient(90deg, #008080, #20B2AA) !important;
    color: #FFFFFF !important;
    border: 2px solid #004D40 !important;
    border-radius: 12px !important;
    padding: 12px 18px !important;
    font-weight: 800 !important;
    box-shadow: 0px 4px 8px rgba(0,0,0,0.15) !important;
}
div[data-testid="stLinkButton"] > a p {
    color: #FFFFFF !important;
    font-size: 18px !important;
    font-weight: bold !important;
}
div[data-testid="stLinkButton"] > a:hover {
    background: linear-gradient(90deg, #004D40, #008080) !important;
    border-color: #FFD700 !important;
}

/* Action Buttons (Generate Power Note, Calculate Tax, Save Diary) */
div.stButton > button, div[data-testid="stFormSubmitButton"] > button {
    background: linear-gradient(90deg, #1B5E20, #2E7D32, #43A047) !important;
    color: white !important;
    border: 2px solid #FFD700 !important;
    border-radius: 12px !important;
    padding: 12px 24px !important;
    width: 100% !important;
    box-shadow: 0px 4px 10px rgba(0,0,0,0.2) !important;
}
div.stButton > button p, div[data-testid="stFormSubmitButton"] > button p {
    font-size: 20px !important;
    font-weight: 800 !important;
    color: #FFFFFF !important;
}
div.stButton > button:hover, div[data-testid="stFormSubmitButton"] > button:hover {
    background: linear-gradient(90deg, #FF6F00, #F57C00) !important;
    border-color: #8B0000 !important;
}

/* Checkboxes (Rules) - Hara Bhara Card Look */
div[data-testid="stCheckbox"] {
    background: linear-gradient(90deg, #E8F5E9, #F1F8E9);
    padding: 12px 16px;
    border-radius: 10px;
    border-left: 6px solid #2E7D32;
    border-right: 1px solid #C8E6C9;
    margin-bottom: 10px;
    box-shadow: 0px 2px 5px rgba(0,0,0,0.06);
}
div[data-testid="stCheckbox"] label p {
    font-size: 18px !important;
    font-weight: 700 !important;
    color: #1B5E20 !important;
}

/* Expanders (Power Note & Tax Calculator) */
div[data-testid="stExpander"] {
    border: 2px solid #2E7D32 !important;
    border-radius: 14px !important;
    background-color: #FAFFFA !important;
    box-shadow: 0px 4px 10px rgba(0,0,0,0.08) !important;
}
div[data-testid="stExpander"] summary {
    background: linear-gradient(90deg, #C8E6C9, #DCEDC8) !important;
    border-radius: 12px 12px 0 0 !important;
    padding: 12px 16px !important;
}
div[data-testid="stExpander"] summary p {
    font-size: 20px !important;
    font-weight: 800 !important;
    color: #1B5E20 !important;
}

/* Metric Cards (Tax, Target, Net Profit) */
div[data-testid="stMetric"] {
    background: linear-gradient(135deg, #E8F5E9, #C8E6C9);
    border: 2px solid #2E7D32;
    border-radius: 12px;
    padding: 15px;
    text-align: center;
    box-shadow: 0px 4px 8px rgba(0,0,0,0.1);
}
div[data-testid="stMetricLabel"] p {
    font-size: 16px !important;
    font-weight: bold !important;
    color: #1B5E20 !important;
}
div[data-testid="stMetricValue"] {
    font-size: 26px !important;
    font-weight: 900 !important;
    color: #004D40 !important;
}

/* Digital Trade Diary Form */
div[data-testid="stForm"] {
    background: linear-gradient(135deg, #F3E5F5, #E8EAF6);
    border: 2px solid #6A1B9A;
    border-radius: 14px;
    padding: 18px;
    box-shadow: 0px 4px 10px rgba(0,0,0,0.1);
}
</style>
""", unsafe_allow_html=True)

# ==========================================
# MAIN APP TITLE & GEETA MAHAMANTRAS
# ==========================================
st.markdown("""
<div style="text-align: center; background: linear-gradient(90deg, #004D40, #1B5E20, #2E7D32); padding: 18px; border-radius: 15px; border: 3px solid #FFD700; margin-bottom: 18px; box-shadow: 0px 5px 15px rgba(0,0,0,0.25);">
    <h1 style="color: #FFD700; font-size: 38px; font-weight: 900; text-shadow: 2px 2px 4px #000000; margin: 0;">
        📊 Pritika's Pro Trading Tracker
    </h1>
</div>

<div style="text-align: center; background: linear-gradient(90deg, #FFD700, #FF8C00); padding: 18px; border-radius: 15px; border: 3px solid #8B0000; margin-bottom: 20px; box-shadow: 0px 4px 12px rgba(0,0,0,0.2);">
    <h1 style="color: #800000; font-size: 42px; font-weight: 900; text-shadow: 2px 2px 4px #ffffff; margin: 0;">
        🕉️ गीता के ३ महामंत्र 🕉️
    </h1>
    <p style="color: #1a1a1a; font-size: 22px; font-weight: bold; margin: 5px 0 0 0;">
        (Trader's Mindset)
    </p>
</div>
""", unsafe_allow_html=True)

# 1. Pehla Mahamantra
with st.popover("🏹 १. वीतरागभयक्रोधः (Na Lalach, Na Darr, Na Gussa)", use_container_width=True):
    st.markdown("""
    <div style="background-color: #FFF0F5; padding: 20px; border-radius: 12px; border-left: 8px solid #C71585;">
        <h2 style="color: #8B0000; font-size: 30px; font-weight: bold; margin-top: 0;">
            🏹 वीतरागभयक्रोधः <span style="font-size: 18px; color: #555;">*(Adhyay 2, Shlok 56)*</span>
        </h2>
        <p style="font-size: 21px; color: #2F4F4F; line-height: 1.6;">
            <strong style="color: #D2691E;">🔸 Sanskrit Arth:</strong> Jo asakti, darr aur krodh se poori tarah mukt ho chuka hai.
        </p>
        <p style="font-size: 22px; color: #800000; font-weight: bold; line-height: 1.6; margin-bottom: 0;">
            🎯 Trading Meaning: Lalach, Darr aur Gussa trading ke sabse bade dushman hain. Inse mukt hokar apne pre-marked zones par strict discipline ke sath trade execute karein.
        </p>
    </div>
    """, unsafe_allow_html=True)

# Doosra Mahamantra
with st.popover("⚖️ २. कर्मण्येवाधिकारस्ते (Mera kaam sirf Rule follow karna hai...)", use_container_width=True):
    st.markdown("""
    <div style="background-color: #F0FFF0; padding: 20px; border-radius: 12px; border-left: 8px solid #008000;">
        <h2 style="color: #006400; font-size: 30px; font-weight: bold; margin-top: 0;">
            ⚖️ कर्मण्येवाधिकारस्ते <span style="font-size: 18px; color: #555;">*(Adhyay 2, Shlok 47)*</span>
        </h2>
        <p style="font-size: 21px; color: #2F4F4F; line-height: 1.6;">
            <strong style="color: #008080;">🔸 Sanskrit Arth:</strong> Tumhara adhikar sirf karm karne par hai, uske phalon par kabhi nahi.
        </p>
        <p style="font-size: 22px; color: #004d00; font-weight: bold; line-height: 1.6; margin-bottom: 0;">
            🎯 Trading Meaning: Aapka control sirf rules follow karne aur risk management par hai. Profit market ka prasad hai, aap sirf apne process par dhyan dein.
        </p>
    </div>
    """, unsafe_allow_html=True)

# Teesra Mahamantra
with st.popover("⚔️ ३. युद्धाय कृतनिश्चयः (Ek Yoddha ki tarah bina emotions ke...)", use_container_width=True):
    st.markdown("""
    <div style="background-color: #F0F8FF; padding: 20px; border-radius: 12px; border-left: 8px solid #0000CD;">
        <h2 style="color: #00008B; font-size: 30px; font-weight: bold; margin-top: 0;">
            ⚔️ युद्धाय कृतनिश्चयः <span style="font-size: 18px; color: #555;">*(Adhyay 2, Shlok 38)*</span>
        </h2>
        <p style="font-size: 21px; color: #2F4F4F; line-height: 1.6;">
            <strong style="color: #4169E1;">🔸 Sanskrit Arth:</strong> Sukh-dukh aur labh-hani ko saman samajh kar yuddh ke liye taiyar ho jao.
        </p>
        <p style="font-size: 22px; color: #191970; font-weight: bold; line-height: 1.6; margin-bottom: 0;">
            🎯 Trading Meaning: Market ek jang ka maidan hai. Profit aur loss dono ko barabar accept karte hue bina kisi emotional baggage ke apne setup ka wait karein.
        </p>
    </div>
    """, unsafe_allow_html=True)

# Highlighted Daily Pledge Box
st.markdown("""
<div style="background: linear-gradient(90deg, #E8F5E9, #C8E6C9); padding: 16px 20px; border-radius: 12px; border: 2px solid #2E7D32; margin-top: 10px; margin-bottom: 20px; text-align: center; box-shadow: 0px 3px 8px rgba(0,0,0,0.1);">
    <p style="color: #1B5E20; font-size: 20px; font-weight: 800; margin: 0;">
        ✨ "Main Pritika Veer, apne in trading rules ka 100% palan karungi. Capital ko bachana mera pehla dharam hai, aur profit banana doosra."
    </p>
</div>
""", unsafe_allow_html=True)

# ==========================================
# QUICK LINKS SECTION (PRITIKA'S MASTER TOOLS)
# ==========================================
st.markdown("""
<div style="background: linear-gradient(90deg, #00695C, #00897B); padding: 12px 20px; border-radius: 12px; border-left: 8px solid #FFD700; margin-bottom: 15px; box-shadow: 0px 3px 8px rgba(0,0,0,0.15);">
    <h3 style="color: #FFFFFF; font-size: 26px; font-weight: 800; margin: 0;">
        🔗 Pritika's Master Tools
    </h3>
</div>
""", unsafe_allow_html=True)

col1, col2 = st.columns(2)
with col1:
    st.link_button("📰 Open Veer Market News", "https://veer-market-news.streamlit.app", use_container_width=True)
with col2:
    st.link_button("🔎 Open Veer Master Scanner", "https://trading-scanner--veer-crty7rxlsxven92q2buuiy.streamlit.app/", use_container_width=True)
    st.link_button("🌟 Open Market Breath Engine", "https://colab.research.google.com/drive/1ds5WtQaIqTkKUeqGPGXQSB9ZZLxmG_fk?usp=sharing", use_container_width=True)

st.write("")

# ==========================================
# STAGE 1: PRE-MARKET ROUTINE
# ==========================================
st.markdown("""
<div style="background: linear-gradient(90deg, #1565C0, #1E88E5); padding: 14px 20px; border-radius: 12px; border-left: 8px solid #FFD700; margin-bottom: 15px; box-shadow: 0px 4px 10px rgba(0,0,0,0.15);">
    <h3 style="color: #FFFFFF; font-size: 26px; font-weight: 800; margin: 0;">
        🌙 STAGE 1: Pre-Market & Data Analysis
    </h3>
</div>
""", unsafe_allow_html=True)

pm1 = st.checkbox("1. FII/DII Data & Option Chain: Maine Veer News App mein aaj ka data analyze kar liya hai.")
if pm1:
    st.warning("📌 IMP NOTE: Dhyan rahe! Agar FII aur DII dono Futures bech rahe hain, toh Call (CE) lene mein jaldbaazi na karein. Trend ke sath chalein.")

pm2 = st.checkbox("2. Zone Marking: 'Smart Structure & Liquidity' se zones mark kar liye hain.")
if pm2:
    st.info("📌 IMP NOTE: Fibonacci 0.618 level aur Gann ratios ko chart par cross-verify zaroor karein. Zone ke bahar NO ENTRY.")

pm3 = st.checkbox("3. Global Cues & Pre-Open: Gift Nifty aur 9:08 AM ka settlement dekh liya hai.")
pm4 = st.checkbox("4. Tech Ready: Veer Master Scanner aur Dhan Power Scalper login karke ready hain.")

st.write("")

# ==========================================
# STAGE 1.5: MASTER POWER SUMMARY 
# ==========================================
st.markdown("""
<div style="background: linear-gradient(90deg, #6A1B9A, #8E24AA); padding: 14px 20px; border-radius: 12px; border-left: 8px solid #FFD700; margin-bottom: 10px; box-shadow: 0px 4px 10px rgba(0,0,0,0.15);">
    <h3 style="color: #FFFFFF; font-size: 26px; font-weight: 800; margin: 0;">
        🧠 STAGE 1.5: Master Power Summary
    </h3>
    <p style="color: #F3E5F5; font-size: 16px; margin: 4px 0 0 0;">
        Apne teeno tools ka result yahan dalein aur aaj ka 'Power Note' banayein:
    </p>
</div>
""", unsafe_allow_html=True)

with st.expander("⚡ Generate Today's Trading Power Note", expanded=True):
    s1, s2, s3 = st.columns(3)
    
    with s1:
        fii_data = st.selectbox("1. Veer News (FII/DII)", ["Select...", "Bullish (Dono Buy)", "Bearish (Dono Sell)", "Mixed (Takkar)"])
    with s2:
        scanner_data = st.selectbox("2. Master Scanner", ["Select...", "CE (Long Setup)", "PE (Short Setup)", "No Clear Setup"])
    with s3:
        breath_data = st.selectbox("3. Market Breath", ["Select...", "Positive (+)", "Negative (-)", "Neutral"])
    
    if st.button("🔥 Generate Power Note"):
        if fii_data == "Select..." or scanner_data == "Select..." or breath_data == "Select...":
            st.error("Kripya teeno tools ka result select karein!")
        elif fii_data == "Bullish (Dono Buy)" and scanner_data == "CE (Long Setup)" and breath_data == "Positive (+)":
            st.success("🚀 **POWER NOTE (HIGH CONVICTION):** Teeno tools ek hi disha (BULLISH) mein ishara kar rahe hain! Aaj apne Zone par aate hi NORMAL/FULL quantity ke sath Call (CE) ka trade lein. Trend aapka dost hai.")
        elif fii_data == "Bearish (Dono Sell)" and scanner_data == "PE (Short Setup)" and breath_data == "Negative (-)":
            st.error("📉 **POWER NOTE (HIGH CONVICTION):** Teeno tools (BEARISH) ishara kar rahe hain! Aaj bounce aane par apne Zone se NORMAL/FULL quantity ke sath Put (PE) ka trade lein. Market weak hai.")
        elif fii_data == "Mixed (Takkar)" or breath_data == "Neutral" or scanner_data == "No Clear Setup":
            st.warning("⚠️ **POWER NOTE (CAUTION):** Data aapas mein match nahi kar raha hai! Market confused hai aur Trapping (SL Hunting) ho sakti hai. Aaj ya toh TRADE NA LEIN, ya sirf HALF (Aadhi) Quantity mein trade karein.")
        else:
            st.info("⚖️ **POWER NOTE (WAIT & WATCH):** Tools ek dusre ke khilaf (opposite) bol rahe hain. Aise din option buyer ka paisa zero hota hai. Jab tak Data ek taraf na mude, apne haath baandh kar rakhein!")

st.write("")

# ==========================================
# STAGE 2: LIVE MARKET ROUTINE
# ==========================================
st.markdown("""
<div style="background: linear-gradient(90deg, #B71C1C, #D84315); padding: 14px 20px; border-radius: 12px; border-left: 8px solid #FFD700; margin-bottom: 15px; box-shadow: 0px 4px 10px rgba(0,0,0,0.15);">
    <h3 style="color: #FFFFFF; font-size: 26px; font-weight: 800; margin: 0;">
        🎯 STAGE 2: Live Market Entry (Buy/Sell Dabaane Se Pehle)
    </h3>
</div>
""", unsafe_allow_html=True)

lm1 = st.checkbox("Rule 1: Trade strictly mere pre-marked 'ZONE' ke andar aa gaya hai (No FOMO).")
if lm1:
    st.error("🚨 ALERT: Market bhaag raha ho tab bhi chalti train mein nahi chadhna hai. Apne zone ka wait karein!")

lm2 = st.checkbox("Rule 2: Entry lene se pehle maine fix Stop Loss (SL) aur Target soch liya hai.")
lm3 = st.checkbox("Rule 3: Aaj ki Max 3 Trades ki limit abhi bachi hui hai.")
if lm3:
    st.warning("📌 IMP NOTE: Yaad rakhein - Sirf 3 Goliya! Pehle 2 trade loss mein gaye toh turant screen band karni hai.")

lm4 = st.checkbox("Rule 4: Main bina kisi Revenge ke, bilkul shant dimaag se trade le rahi hoon.")

# Calculate Progress
tasks = [pm1, pm2, pm3, pm4, lm1, lm2, lm3, lm4]
completed = sum(tasks)
total = len(tasks)
percentage = int((completed / total) * 100)

st.write("")

# ==========================================
# DISPLAY SCORE & PROGRESS BAR
# ==========================================
st.markdown(f"""
<div style="background: linear-gradient(90deg, #1B5E20, #388E3C); padding: 14px 20px; border-radius: 12px; border-left: 8px solid #FFD700; margin-bottom: 12px; box-shadow: 0px 4px 10px rgba(0,0,0,0.15);">
    <h3 style="color: #FFFFFF; font-size: 26px; font-weight: 800; margin: 0;">
        📈 Aapka Discipline Score: <span style="color: #FFD700;">{percentage}%</span>
    </h3>
</div>
""", unsafe_allow_html=True)

st.progress(percentage)

if percentage == 100:
    st.success("🟢 100% APPROVED: Excellent! Sab kuch perfect hai. Aap apna trade execute kar sakte hain. Happy Trading!")
    st.balloons()
else:
    st.error("🔴 DO NOT TRADE! Aapka homework ya rules abhi poore nahi hain.")
    st.markdown(f"<p style='font-size: 19px; font-weight: bold; color: #B71C1C;'>👉 Trade lene ke liye abhi <strong>{total - completed} rules</strong> check karna bache hain.</p>", unsafe_allow_html=True)

st.write("")

# ==========================================
# STAGE 3: TARGET ENFORCER & EXACT TAX CALCULATOR
# ==========================================
st.markdown("""
<div style="background: linear-gradient(90deg, #004D40, #00796B); padding: 14px 20px; border-radius: 12px; border-left: 8px solid #FFD700; margin-bottom: 12px; box-shadow: 0px 4px 10px rgba(0,0,0,0.15);">
    <h3 style="color: #FFFFFF; font-size: 26px; font-weight: 800; margin: 0;">
        🛡️ STAGE 3: Target Enforcer & Position Sizing
    </h3>
    <p style="color: #E0F2F1; font-size: 16px; margin: 4px 0 0 0;">
        Trade ka Buy/Sell button dabane se pehle Exact Brokerage aur apna Target check karein:
    </p>
</div>
""", unsafe_allow_html=True)

with st.expander("🧮 Calculate Safe Lots, Exact Taxes & Target", expanded=True):
    col1, col2 = st.columns(2)
    
    with col1:
        risk_amount = st.number_input("Max Loss (₹)", min_value=100, value=1000, step=100)
        sl_points = st.number_input("Stop Loss (Points)", min_value=1, value=20, step=1)
    with col2:
        lot_size = st.number_input("Current Lot Size", min_value=1, value=15, step=1)
        buy_price = st.number_input("Option Buy Price (Premium)", min_value=1, value=300, step=1)
    
    if st.button("Calculate Exact Tax & Target"):
        if sl_points > 0 and buy_price > 0:
            ideal_qty = int(risk_amount / sl_points)
            safe_lots = ideal_qty // lot_size
            final_qty = safe_lots * lot_size
            
            if safe_lots > 0:
                st.info(f"✅ Safe Limit: **{safe_lots} Lots** (Total **{final_qty} Qty**) | Max Loss Rule: **₹{risk_amount}**")
                
                # ---- EXACT BROKERAGE & TAX CALCULATION (NSE OPTIONS) ----
                target_points = sl_points * 2  # 1:2 Risk Reward Ratio
                sell_price = buy_price + target_points
                
                buy_turnover = buy_price * final_qty
                sell_turnover = sell_price * final_qty
                total_turnover = buy_turnover + sell_turnover
                
                # 1. Brokerage (Dhan Standard: ₹40 round-trip per executed order)
                brokerage = 40
                
                # 2. STT (Oct 2024 Rule: 0.1% on Sell Turnover for Options)
                stt = sell_turnover * 0.001
                
                # 3. Exchange Charges (NSE Options: 0.03503% on Total Turnover)
                exchange_charges = total_turnover * 0.0003503
                
                # 4. SEBI Charges (0.0001% on Total Turnover)
                sebi_charges = total_turnover * 0.000001
                
                # 5. Stamp Duty (0.003% on Buy Turnover)
                stamp_duty = buy_turnover * 0.00003
                
                # 6. GST (18% on Brokerage + Exchange + SEBI)
                gst = (brokerage + exchange_charges + sebi_charges) * 0.18
                
                total_taxes = round(brokerage + stt + exchange_charges + sebi_charges + stamp_duty + gst, 2)
                gross_profit = target_points * final_qty
                net_profit = round(gross_profit - total_taxes, 2)
                
                st.markdown("### 💸 Exact Govt. Tax & Brokerage Hisaab")
                bc1, bc2, bc3 = st.columns(3)
                bc1.metric("Brokerage + All Taxes", f"₹{total_taxes}")
                bc2.metric("Target (1:2)", f"{target_points} Pts (at ₹{sell_price})")
                bc3.metric("Net Profit (In Hand)", f"₹{net_profit}")
                
                st.warning(f"🚨 **TARGET ENFORCER:** Aapko trade strictly **₹{sell_price}** par hi bechna hai. Sarkar (STT, GST) aur Broker aapse iss trade par **₹{total_taxes}** tax katenge. Agar chhote profit mein nikal gaye, toh tax bharne ke baad jeb mein kuch nahi bachega. **Hold till Target!**")
                
            else:
                st.error("🚨 DO NOT TRADE! Aapka Stop Loss itna bada hai ki is Risk limit mein 1 Lot bhi nahi aayega.")

st.write("")

# ==========================================
# STAGE 4: MARKET MAUSAM & DIARY
# ==========================================
st.markdown("""
<div style="background: linear-gradient(90deg, #0277BD, #00ACC1); padding: 14px 20px; border-radius: 12px; border-left: 8px solid #FFD700; margin-bottom: 15px; box-shadow: 0px 4px 10px rgba(0,0,0,0.15);">
    <h3 style="color: #FFFFFF; font-size: 26px; font-weight: 800; margin: 0;">
        🌤️ STAGE 4: Market Mausam & Emotion Tracker
    </h3>
</div>
""", unsafe_allow_html=True)

col3, col4 = st.columns(2)

with col3:
    st.markdown("""
    <div style="background: #E1F5FE; padding: 12px; border-radius: 10px; border-left: 6px solid #0288D1; margin-bottom: 10px;">
        <h4 style="color: #01579B; margin: 0; font-size: 22px; font-weight: 800;">🧭 Market Direction</h4>
    </div>
    """, unsafe_allow_html=True)
    weather = st.radio("FII/DII Data ke hisaab se Market kaisa hai?", 
                       ["☀️ Clear (Strong Bullish/Bearish)", "🌫️ Foggy (Sideways - Premium Decay)", "🌧️ Stormy (Highly Volatile)"])
    
    if "Clear" in weather:
        st.success("Aap normal quantity ke sath pre-marked zone par trade le sakti hain.")
    elif "Foggy" in weather:
        st.warning("Option Buyers door rahein! Aaj premium decay hoga. No Trading Day.")
    else:
        st.error("Market bohot volatile hai. Quantity AADHI (Half) kar dein!")

with col4:
    st.markdown("""
    <div style="background: #F3E5F5; padding: 12px; border-radius: 10px; border-left: 6px solid #7B1FA2; margin-bottom: 10px;">
        <h4 style="color: #4A148C; margin: 0; font-size: 22px; font-weight: 800;">📖 Digital Trade Diary</h4>
    </div>
    """, unsafe_allow_html=True)
    with st.form("trade_journal"):
        trade_pnl = st.number_input("Trade ka Profit/Loss (₹)", value=0)
        reason = st.selectbox("Trade lene ka Reason kya tha?", 
                              ["Zone Entry (Rule Followed)", "FOMO (Jaldbaazi)", "Revenge (Gussa)", "Boredom"])
        mindset = st.select_slider("Trade lete time Mindset kaisa tha?", 
                                   options=["Bohot Shant", "Normal", "Dara Hua", "Gusse Mein"])
        
        submitted = st.form_submit_button("💾 Save Trade Record")
        if submitted:
            if "Rule Followed" in reason:
                st.success(f"Good Job! Rule follow kiya. PnL: ₹{trade_pnl}")
            else:
                st.error(f"Rule Break! Isliye loss ya stress hua. PnL: ₹{trade_pnl}. Kal se galti nahi dohrani hai.")
