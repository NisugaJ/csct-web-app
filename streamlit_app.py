from time import sleep

import requests
import streamlit as st
from st_aggrid import AgGrid
import pandas as pd


st.set_page_config(page_title="Home", page_icon='🌱', layout='wide')

sidebar = st.sidebar
sidebar.title(':green[Planta]', anchor=False)
sidebar.write(':grey[Affordable plant based food better than meat]')


st.write('### Welcome to Planta!')

col1, col2, col3 = st.columns([2, 1, 2])

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