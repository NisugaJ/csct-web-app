import requests
import streamlit as st
from st_aggrid import AgGrid
import pandas as pd

from streamlit_utils import filter_dataframe, search_page_columns, send_search_request

api_url = st.secrets["API_BASE_URL"]


st.session_state.search_results = []
st.session_state.search_q = ''
st.session_state.search_filter = {"product_type": "PLANT_BASED"}

st.set_page_config(page_title="Search Planta", page_icon='🌱', layout='wide')


st.write('##### Search for your plant based food!')

all_products = requests.get(f"{api_url}/products/all?type=PLANT_BASED").json()

st.info(f"{len(all_products)} plant-based products are available")

search_query = st.text_input('Search', key='search_bar',  placeholder="Search anything here. (E.g. cheese )")

if len(search_query) > 1:
    send_search_request(search_query, st.session_state.search_filter)

df = pd.DataFrame(
    st.session_state.search_results,
)

# filter_dataframe(df)

ag_grid = AgGrid(df, theme='streamlit', height=400, width='100%', enable_quicksearch=True, gridOptions={
    'columnDefs': search_page_columns
})