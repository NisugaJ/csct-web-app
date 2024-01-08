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
