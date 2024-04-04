import streamlit as st

# Page title and favicon for the entire app
# This should be the first Streamlit function called in your app
st.set_page_config(page_title="My Portfolio", page_icon=":bar_chart:", layout="wide")

# Define the page navigation
st.sidebar.title('Navigation')
# Ensure that the radio button has a unique key in case there are other radio buttons
page = st.sidebar.radio('Go to', ['Home', 'Power BI Report', 'ML Model'], key='main_navigation')

# Define the Power BI Embed URL
powerbi_embed_url = "https://app.powerbi.com/view?r=eyJrIjoiMmIwZGE0ZDgtN2RkMy00MjlhLWI5NDktMjhiNjUyYjBiMmM1IiwidCI6Ijk2NDY0YThhLWY4ZWQtNDBiMS05OWUyLTVmNmI1MGEyMDI1MCIsImMiOjN9"

# Apply custom CSS across all pages to maintain a consistent style
st.markdown("""
    <style>
        .reportview-container .main .block-container {
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

# Home Page
if page == 'Home':
    st.image('path_to_your_image.jpg', width=300)  # Adjust the width as needed
    st.title('HI THERE 👋')
    st.subheader('I AM A DATA SCIENTIST WHO:')
    st.markdown("""
    * 🔥 loves to solve complex problems in diverse domains
    * 🌍 is currently working in the field of Climate Change
    * 🧬 handled challenging tasks in Bioinformatics & Telecommunications
    * 💻 plays with all kinds of data structures - text, image, graph, numerical etc
    * 🌟 at the end of the day, aims to make the data shine!
    """)

# Power BI Report Page
elif page == 'Power BI Report':
    st.markdown(
        f"""
        <iframe title="Power BI Report" width="100%" height="100vh" src="{powerbi_embed_url}" frameborder="0" allowFullScreen="true"></iframe>
        """,
        unsafe_allow_html=True
    )

# ML Model Page
elif page == 'ML Model':
    st.title('ML Model')
    # Display your ML model content or widget here
    st.write('ML Model details to be added here.')

# Add the content for the Footer
st.sidebar.markdown('---')
st.sidebar.info('This is a simple multi-page Streamlit app to showcase a portfolio with a Power BI report and an ML model.')
