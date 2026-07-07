import streamlit as st
import requests

# This line tells the app to look for a hidden secret named GOLD_API_KEY
# It will not be visible in your GitHub code.
API_KEY = st.secrets["GOLD_API_KEY"]

def get_live_gold_price():
    url = "https://www.goldapi.io/api/XAU/USD"
    headers = {
        "x-access-token": API_KEY,
        "Content-Type": "application/json"
    }
    try:
        response = requests.get(url, headers=headers)
        return float(response.json()['price'])
    except:
        return 4123.84 # Fallback
