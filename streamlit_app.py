from time import sleep

import requests
import streamlit as st
from st_aggrid import AgGrid
import pandas as pd
from st_pages import show_pages, Page

st.set_page_config(page_title="Home", page_icon='🌱', layout='wide')

show_pages(
    [
        Page("streamlit_app.py", "Home", "🏠"),
        Page("pages/All Products.py", "All Products", ":document:"),
        Page("pages/Chat.py", "Chat", ":bot:"),
        Page("pages/Search.py", "Search", ":search:"),
        Page("pages/About.py.py", "About", ":info:"),
    ]
)

sidebar = st.sidebar
sidebar.title(':green[Planta]', anchor=False)
sidebar.write(':grey[Affordable plant-based food better than meat]')


st.write('### Welcome to Planta!')
st.write(':grey[Affordable plant-based food better than meat]')
st.divider()
left_col2, left_col1, col1, col2, col3, right_col1, right_col2 = st.columns([1, 1, 3, 3, 3, 1, 1])

with col1:
   st.link_button(
       "Search",
       "/Search",
       use_container_width=True
       )

with col2:
   st.link_button(
       "Chat",
       "/Chat",
       use_container_width=True
   )

with col3:
   st.link_button(
       "All Products",
       "/All_Products",
       use_container_width=True
   )