import streamlit as st
import requests

api_url = st.secrets["API_BASE_URL"]

all_products = requests.get(f"{api_url}/products/all").json()

st.info(f"{len(all_products)} products are available")

all_products

