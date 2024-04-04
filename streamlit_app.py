import streamlit as st

# Define the Power BI Embed URL
powerbi_embed_url = "https://app.powerbi.com/view?r=eyJrIjoiMmIwZGE0ZDgtN2RkMy00MjlhLWI5NDktMjhiNjUyYjBiMmM1IiwidCI6Ijk2NDY0YThhLWY4ZWQtNDBiMS05OWUyLTVmNmI1MGEyMDI1MCIsImMiOjN9"

# Set the page to use a wide layout and the title and favicon
st.set_page_config(page_title="My Power BI Dashboard", page_icon=":bar_chart:", layout="wide")

# Custom CSS to remove Streamlit's padding and margins, and set the iframe height to 100vh
st.markdown("""
    <style>
        .reportview-container .main .block-container{
            padding-top: 0;
            padding-right: 0;
            padding-left: 0;
            padding-bottom: 0;
        }
        .reportview-container .main {
            color: #f0f0f0;
            background-color: #f0f0f0;
        }
        iframe {
            height: 100vh;
        }
    </style>
    """, unsafe_allow_html=True)

# Display the Power BI dashboard using the iframe with 100% width and 100vh height
st.markdown(
    f"""
    <iframe title="Final_Dashboard" width="100%" height="100vh" src="{powerbi_embed_url}" frameborder="0" allowFullScreen="true"></iframe>
    """,
    unsafe_allow_html=True,
)
