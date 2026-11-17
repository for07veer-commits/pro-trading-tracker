import streamlit as st

# App Settings
st.set_page_config(page_title="Pritika's Pro Trading Tracker", page_icon="📈", layout="centered")

# Header & Daily Pledge
st.title("📊 Pritika's Pro Trading Tracker")
st.markdown("### 🕉️ गीता के ३ महामंत्र (Trader's Mindset)")
st.error("🏹 **१. वीतरागभयक्रोधः** (Na Lalach, Na Darr, Na Gussa)")
st.warning("⚖️ **२. कर्मण्येवाधिकारस्ते** (Mera kaam sirf Rule follow karna hai, Profit market ka prasad hai)")
st.success("⚔️ **३. युद्धाय कृतनिश्चयः** (Ek Yoddha ki tarah bina emotions ke apna Dharm nibhaungi)")

st.info('✨ "Main Pritika Veer, apne in trading rules ka 100% palan karungi. Capital ko bachana mera pehla dharam hai, aur profit banana doosra."')
st.write("---")

# Quick Links Section (Aapke dusre apps yahan link honge)
st.markdown("### 🔗 Pritika's Master Tools")
col1, col2 = st.columns(2)
with col1:
    # Aapka live news app link
    st.link_button("📰 Open Veer Market News", "https://veer-market-news.streamlit.app", use_container_width=True)
with col2:
    st.link_button("🔎 Open Veer Master Scanner", "https://trading-scanner--veer-crty7rxlsxven92q2buuiy.streamlit.app/", use_container_width=True)
    st.link_button("🌟 Open Market Breath Engine", "https://colab.research.google.com/drive/1ds5WtQaIqTkKUeqGPGXQSB9ZZLxmG_fk?usp=sharing", use_container_width=True)

st.write("---")

# STAGE 1: PRE-MARKET ROUTINE
st.subheader("🌙 STAGE 1: Pre-Market & Data Analysis")

pm1 = st.checkbox("1. FII/DII Data & Option Chain: Maine Veer News App mein aaj ka data analyze kar liya hai.")
if pm1:
    st.warning("📌 IMP NOTE: Dhyan rahe! Agar FII aur DII dono Futures bech rahe hain, toh Call (CE) lene mein jaldbaazi na karein. Trend ke sath chalein.")

pm2 = st.checkbox("2. Zone Marking: 'Smart Structure & Liquidity' se zones mark kar liye hain.")
if pm2:
    st.info("📌 IMP NOTE: Fibonacci 0.618 level aur Gann ratios ko chart par cross-verify zaroor karein. Zone ke bahar NO ENTRY.")

pm3 = st.checkbox("3. Global Cues & Pre-Open: Gift Nifty aur 9:08 AM ka settlement dekh liya hai.")
pm4 = st.checkbox("4. Tech Ready: Veer Master Scanner aur Dhan Power Scalper login karke ready hain.")

st.write("---")
# ==========================================
# STAGE 1.5: MASTER POWER SUMMARY (DATA COMBINER)
# ==========================================
st.markdown("## 🧠 STAGE 1.5: Master Power Summary")
st.write("Apne teeno tools ka result yahan dalein aur aaj ka 'Power Note' banayein:")

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
        
        # Super Bullish Setup
        elif fii_data == "Bullish (Dono Buy)" and scanner_data == "CE (Long Setup)" and breath_data == "Positive (+)":
            st.success("🚀 **POWER NOTE (HIGH CONVICTION):** Teeno tools ek hi disha (BULLISH) mein ishara kar rahe hain! Aaj apne Zone par aate hi NORMAL/FULL quantity ke sath Call (CE) ka trade lein. Trend aapka dost hai.")
        
        # Super Bearish Setup
        elif fii_data == "Bearish (Dono Sell)" and scanner_data == "PE (Short Setup)" and breath_data == "Negative (-)":
            st.error("📉 **POWER NOTE (HIGH CONVICTION):** Teeno tools (BEARISH) ishara kar rahe hain! Aaj bounce aane par apne Zone se NORMAL/FULL quantity ke sath Put (PE) ka trade lein. Market weak hai.")
        
        # Trapping / Sideways Setup
        elif fii_data == "Mixed (Takkar)" or breath_data == "Neutral" or scanner_data == "No Clear Setup":
            st.warning("⚠️ **POWER NOTE (CAUTION):** Data aapas mein match nahi kar raha hai! Market confused hai aur Trapping (SL Hunting) ho sakti hai. Aaj ya toh TRADE NA LEIN, ya sirf HALF (Aadhi) Quantity mein trade karein.")
        
        # Contradiction (Khilaf)
        else:
            st.info("⚖️ **POWER NOTE (WAIT & WATCH):** Tools ek dusre ke khilaf (opposite) bol rahe hain. Aise din option buyer ka paisa zero hota hai. Jab tak Data ek taraf na mude, apne haath baandh kar rakhein!")

st.write("---")
# STAGE 2: LIVE MARKET ROUTINE
st.subheader("🎯 STAGE 2: Live Market Entry (Buy/Sell Dabaane Se Pehle)")

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

st.write("---")

# Display Score & Progress Bar
st.subheader("📈 Aapka Discipline Score")
st.progress(percentage)
st.write(f"**Score: {percentage}%**")

st.write("---")

# Logic: Can Pritika Trade?
if percentage == 100:
    st.success("🟢 100% APPROVED: Excellent Pritika! Sab kuch perfect hai. Aap apna trade execute kar sakti hain. Happy Trading!")
    st.balloons()
else:
    st.error("🔴 DO NOT TRADE! Aapka homework ya rules abhi poore nahi hain.")
    st.write(f"Trade lene ke liye abhi **{total - completed} rules** check karna bache hain.")

# ==========================================
# STAGE 3: NAYA LOT SIZE CALCULATOR
# ==========================================
st.markdown("---")
st.markdown("## 🛡️ STAGE 3: Position Sizing (Capital Protector)")
st.write("Trade ka Buy/Sell button dabane se pehle apni Risk limit aur Lot Size check karein:")

with st.expander("🧮 Calculate Safe Lots / Quantity Before Entry", expanded=True):
    col1, col2, col3 = st.columns(3)
    
    with col1:
        risk_amount = st.number_input("Max Loss (₹)", min_value=100, value=1000, step=100)
    with col2:
        sl_points = st.number_input("Stop Loss (Points)", min_value=1, value=20, step=1)
    with col3:
        # HINT HATA DIYA HAI: Aap apna naya lot size directly is dabbe mein type kar sakti hain!
        lot_size = st.number_input("Current Lot Size Likhien", min_value=1, value=15, step=1)
    
    if st.button("Calculate Safe Quantity"):
        if sl_points > 0:
            ideal_qty = int(risk_amount / sl_points)
            safe_lots = ideal_qty // lot_size
            final_qty = safe_lots * lot_size
            
            st.success(f"🛑 Aapka Stop Loss: **{sl_points} points** | Max Risk: **₹{risk_amount}**")
            
            if safe_lots > 0:
                st.info(f"✅ Safe Limit: **{safe_lots} Lots** (Total **{final_qty} Qty**)")
                st.warning("⚠️ Warning: Agar isse zyada Lot liye, toh risk limit cross ho jayegi. Rule break mat karna!")
            else:
                st.error("🚨 DO NOT TRADE! Aapka Stop Loss itna bada hai ki is Risk limit mein 1 Lot bhi nahi aayega. Ya toh chhote SL wala trade dhoondein, ya trade chhod dein.")

# ==========================================
# STAGE 4: MARKET MAUSAM & DIARY
# ==========================================
st.markdown("---")
st.markdown("## 🌤️ Market Mausam & Emotion Tracker")

col3, col4 = st.columns(2)

with col3:
    st.markdown("### 🧭 Market Direction")
    weather = st.radio("FII/DII Data ke hisaab se Market kaisa hai?", 
                       ["☀️ Clear (Strong Bullish/Bearish)", "🌫️ Foggy (Sideways - Premium Decay)", "🌧️ Stormy (Highly Volatile)"])
    
    if "Clear" in weather:
        st.success("Aap normal quantity ke sath pre-marked zone par trade le sakti hain.")
    elif "Foggy" in weather:
        st.warning("Option Buyers door rahein! Aaj premium decay hoga. No Trading Day.")
    else:
        st.error("Market bohot volatile hai. Quantity AADHI (Half) kar dein!")

with col4:
    st.markdown("### 📖 Digital Trade Diary")
    with st.form("trade_journal"):
        trade_pnl = st.number_input("Trade ka Profit/Loss (₹)", value=0)
        reason = st.selectbox("Trade lene ka Reason kya tha?", 
                              ["Zone Entry (Rule Followed)", "FOMO (Jaldbaazi)", "Revenge (Gussa)", "Boredom"])
        mindset = st.select_slider("Trade lete time Mindset kaisa tha?", 
                                   options=["Bohot Shant", "Normal", "Dara Hua", "Gusse Mein"])
        
        submitted = st.form_submit_button("Save Trade Record")
        if submitted:
            if "Rule Followed" in reason:
                st.success(f"Good Job Pritika! Rule follow kiya. PnL: ₹{trade_pnl}")
            else:
                st.error(f"Rule Break! Isliye loss ya stress hua. PnL: ₹{trade_pnl}. Kal se galti nahi dohrani hai.")
