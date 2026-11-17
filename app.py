import streamlit as st

# App Settings
st.set_page_config(page_title="Pritika's Pro Trading Tracker", page_icon="📈", layout="centered")

# Header & Daily Pledge
st.title("📊 Pritika's Pro Trading Tracker")
st.info('"Main Pritika, apne in trading rules ka 100% palan karungi. Capital ko bachana mera pehla rule hai, aur profit banana doosra."')

st.write("---")

# Quick Links Section (Aapke dusre apps yahan link honge)
st.markdown("### 🔗 Pritika's Master Tools")
col1, col2 = st.columns(2)
with col1:
    # Aapka live news app link
    st.link_button("📰 Open Veer Market News", "https://veer-market-news.streamlit.app", use_container_width=True)
with col2:
    # DHYAN DEIN: Niche wali line mein apna asli Scanner ka link daalein
    st.link_button("🔎 Open Veer Master Scanner", "https://trading-scanner--veer-crty7rxlsxven92q2buuiy.streamlit.app/", use_container_width=True)
st.link_button("🌟 Open Market Breath Engine", "https://colab.research.google.com/drive/1ds5WtQaIqTkKUeqGPGXQSB9ZZLxmG_fk?usp=sharing", use_container_width=True)
st.write("---")

# STAGE 1: PRE-MARKET ROUTINE
st.subheader("🌙 STAGE 1: Pre-Market & Data Analysis")

pm1 = st.checkbox("1. FII/DII Data & Option Chain: Maine Veer News App mein aaj ka data analyze kar liya hai.")
if pm1:
    # TIK karne par flash hone wala IMP NOTE
    st.warning("📌 IMP NOTE: Dhyan rahe! Agar FII aur DII dono Futures bech rahe hain, toh Call (CE) lene mein jaldbaazi na karein. Trend ke sath chalein.")

pm2 = st.checkbox("2. Zone Marking: 'Smart Structure & Liquidity' se zones mark kar liye hain.")
if pm2:
    st.info("📌 IMP NOTE: Fibonacci 0.618 level aur Gann ratios ko chart par cross-verify zaroor karein. Zone ke bahar NO ENTRY.")

pm3 = st.checkbox("3. Global Cues & Pre-Open: Gift Nifty aur 9:08 AM ka settlement dekh liya hai.")
pm4 = st.checkbox("4. Tech Ready: Veer Master Scanner aur Dhan Power Scalper login karke ready hain.")

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
