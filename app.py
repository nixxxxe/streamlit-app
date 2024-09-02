import streamlit as st
from st_pages import add_page_title, get_nav_from_toml

st.set_page_config(layout="wide")

# Load the navigation from the pages_sections.toml file
nav = get_nav_from_toml(".streamlit/pages_sections.toml")

# Add a logo if you have one
#st.image("logo.png", width=100)

pg = st.navigation(nav)

add_page_title(pg)

pg.run()
