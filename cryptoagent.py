import requests
import streamlit as st

# 🔧 Binance tool
def get_crypto_price(symbol):
    url = f"https://api.binance.com/api/v3/ticker/price?symbol={symbol.upper()}"
    res = requests.get(url)
    if res.status_code == 200:
        return res.json().get("price")
    return None

# 🎨 Page Config
st.set_page_config(page_title="Crypto Price Checker", page_icon="💸", layout="centered")

# 💱 UI Layout
st.markdown("""
    <div style='text-align: center; margin-bottom: 20px;'>
        <h1 style='color: #4CAF50;'>💹 Crypto Price Checker</h1>
        <p style='font-size: 16px; color: gray;'>Check real-time prices for popular cryptocurrencies using Binance API</p>
    </div>
""", unsafe_allow_html=True)

# 📥 Input
symbol = st.text_input("🔎 Enter Crypto Symbol (e.g., BTCUSDT, ETHUSDT):", max_chars=15)

# 🖱️ Button
if st.button("Check Price"):
    if symbol.strip() == "":
        st.warning("Please enter a valid symbol like BTCUSDT.")
    else:
        with st.spinner("Fetching latest price..."):
            price = get_crypto_price(symbol)
            if price:
                st.success(f"💰 Current Price of **{symbol.upper()}** is: **${price}**")
            else:
                st.error("⚠️ Could not fetch price. Make sure the symbol is valid.")
