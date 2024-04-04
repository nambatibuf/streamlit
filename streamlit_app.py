import streamlit as st
import pandas as pd

# Define the Power BI Embed URL
powerbi_embed_url = "https://app.powerbi.com/view?r=eyJrIjoiMmIwZGE0ZDgtN2RkMy00MjlhLWI5NDktMjhiNjUyYjBiMmM1IiwidCI6Ijk2NDY0YThhLWY4ZWQtNDBiMS05OWUyLTVmNmI1MGEyMDI1MCIsImMiOjN9"

# Set the page title and favicon
st.set_page_config(page_title="My Power BI Dashboard", page_icon=":bar_chart:")

# Create a container for the Power BI iframe
powerbi_container = st.empty()

# Display the Power BI dashboard using the iframe
powerbi_container.markdown(
    f"""
    <iframe title="Final_Dashboard" width="100%" height="600" src="{powerbi_embed_url}" frameborder="0" allowFullScreen="true"></iframe>
    """,
    unsafe_allow_html=True,
)

