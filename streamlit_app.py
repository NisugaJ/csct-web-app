import streamlit as st

st.set_page_config(page_title="Home", page_icon='🌱', layout='wide')


# Sidebar
sidebar = st.sidebar
sidebar.title(':green[Planta]', anchor=False)
sidebar.write(':grey[Affordable plant-based food better than meat]')

# Main content
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