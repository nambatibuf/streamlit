import streamlit as st
from PIL import Image

# Page title and favicon for the entire app
# This should be the first Streamlit function called in your app
st.set_page_config(page_title="My Portfolio", page_icon=":bar_chart:", layout="wide")

# Define the page navigation
st.sidebar.title('Navigation')
page = st.sidebar.radio('Go to', ['Home', 'Power BI Report', 'ML Model'])

# ... Rest of your code follows

# Define the page navigation
st.sidebar.title('Navigation')
page = st.sidebar.radio('Go to', ['Home', 'Power BI Report', 'ML Model'])

# Define the Power BI Embed URL
powerbi_embed_url = "https://app.powerbi.com/view?r=eyJrIjoiMmIwZGE0ZDgtN2RkMy00MjlhLWI5NDktMjhiNjUyYjBiMmM1IiwidCI6Ijk2NDY0YThhLWY4ZWQtNDBiMS05OWUyLTVmNmI1MGEyMDI1MCIsImMiOjN9"

# Page title and favicon for the entire app
st.set_page_config(page_title="My Portfolio", page_icon=":bar_chart:", layout="wide")

# Load your image
# Make sure to have an image named 'your_image.jpg' in the same directory as your script
image = Image.open('your_image.jpg')

# Apply custom CSS across all pages to maintain a consistent style
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

# Home Page
if page == 'Home':
    st.header('HI THERE 👋')
    st.image(image, width=300)  # You can adjust the width as needed
    st.subheader('I AM A DATA SCIENTIST WHO :')
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
        unsafe_allow_html=True,
    )

# ML Model Page
elif page == 'ML Model':
    st.header('ML Model')
    # Display your ML model content or widget here
    st.write('ML Model details to be added here.')

# Footer
st.sidebar.markdown('---')
st.sidebar.info('This is a simple multi-page Streamlit app to showcase a portfolio with a Power BI report and an ML model.')

