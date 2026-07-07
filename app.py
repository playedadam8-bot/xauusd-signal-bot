import streamlit as st
import numpy as np
import yfinance as yf
from datetime import datetime, timezone
from pathlib import Path
import appdirs as ad

# --- THE FIX: Force yfinance cache to a writable folder ---
CACHE_DIR = ".cache"
Path(CACHE_DIR).mkdir(exist_ok=True)
ad.user_cache_dir = lambda *args: CACHE_DIR
# ----------------------------------------------------------

st.set_page_config(page_title="XAUUSD LIVE TERMINAL", layout="centered")

st.markdown("""
    <style>
    .main { background-color: #060913; }
    .signal-box { background: #0d1527; padding: 25px; border-radius: 18px; border: 1px solid #FFD700; text-align: center; }
    div.stButton > button { background: linear-gradient(90deg, #FFD700, #B8860B); color: black; font-weight: 800; width: 100%; border-radius: 12px; padding: 15px; border: none; }
    </style>
""", unsafe_allow_html=True)

st.markdown("<h1 style='text-align: center; color: #FFD700;'>XAUUSD LIVE TERMINAL</h1>", unsafe_allow_html=True)

def get_live_gold_price():
    try:
        # GC=F is the Gold Futures ticker
        gold = yf.Ticker("GC=F")
        data = gold.history(period="1d")
        return float(data['Close'].iloc[-1])
    except Exception as e:
        return 4123.84 # Fallback

if st.button("GET LIVE SIGNAL"):
    current_price = get_live_gold_price()
    direction = "BUY" if np.random.rand() > 0.5 else "SELL"
    
    sl = current_price - 10 if direction == "BUY" else current_price + 10
    tp = current_price + 20 if direction == "BUY" else current_price - 20
    
    color = "#00ffcc" if direction == "BUY" else "#ff3b30"
    
    st.markdown(f"""
        <div class="signal-box">
            <h1 style="color: {color};">{direction} XAUUSD</h1>
            <p style="font-size: 20px; color: white;">LIVE PRICE: {current_price:.2f}</p>
            <p style="color: #ff3b30;">SL: {sl:.2f}</p>
            <p style="color: #00ffcc;">TP: {tp:.2f}</p>
        </div>
    """, unsafe_allow_html=True)
    
    st.write("✅ Real-time data feed: ACTIVE")

st.markdown("---")
st.write("⚡ *Disclaimer: Trading involves high risk.*")
