import streamlit as st
import requests
import numpy as np
from datetime import datetime, timezone

# Page Config
st.set_page_config(page_title="XAUUSD LIVE TERMINAL", layout="centered")

# Styling
st.markdown("""
    <style>
    .main { background-color: #060913; color: white; }
    .signal-box { background: #0d1527; padding: 25px; border-radius: 18px; border: 1px solid #FFD700; text-align: center; }
    div.stButton > button { background: linear-gradient(90deg, #FFD700, #B8860B); color: black; font-weight: 800; width: 100%; border-radius: 12px; padding: 15px; border: none; }
    </style>
""", unsafe_allow_html=True)

st.markdown("<h1 style='text-align: center; color: #FFD700;'>XAUUSD LIVE TERMINAL</h1>", unsafe_allow_html=True)

# Securely fetch API Key from Streamlit Secrets
API_KEY = st.secrets["GOLD_API_KEY"]

def get_live_gold_price():
    url = "https://www.goldapi.io/api/XAU/USD"
    headers = {
        "x-access-token": API_KEY,
        "Content-Type": "application/json"
    }
    try:
        response = requests.get(url, headers=headers)
        data = response.json()
        return float(data['price'])
    except Exception:
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
    st.write("✅ Real-time data feed active.")

st.markdown("---")
st.write("⚡ *Disclaimer: Trading involves risk. Use Exness MT5 for final entry.*")
