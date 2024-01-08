import streamlit as st
import pandas as pd
import requests
from st_aggrid import AgGrid

from streamlit_utils import filter_dataframe

api_url = st.secrets["API_BASE_URL"]

all_products = requests.get(f"{api_url}/products/all").json()

st.info(f"{len(all_products)} products are available")


df = pd.DataFrame(
    all_products,
)

filter_dataframe(df)

ag_grid = AgGrid(df,  allow_unaligned_rows=True, theme='streamlit', height=400, width='100%', enable_quicksearch=True)