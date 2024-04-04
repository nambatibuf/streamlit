import streamlit as st
import requests


# Page title and favicon for the entire app
st.set_page_config(page_title="Nikhil Ambati's Portfolio", page_icon=":bar_chart:", layout="wide")

# Define the page navigation
st.sidebar.title('Navigation')
page = st.sidebar.radio('Go to', ['Home', 'Power BI Report', 'ML Model'], key='main_navigation')

# Define the Power BI Embed URL
powerbi_embed_url = "https://app.powerbi.com/view?r=eyJrIjoiMmIwZGE0ZDgtN2RkMy00MjlhLWI5NDktMjhiNjUyYjBiMmM1IiwidCI6Ijk2NDY0YThhLWY4ZWQtNDBiMS05OWUyLTVmNmI1MGEyMDI1MCIsImMiOjN9"

# Apply custom CSS across all pages to maintain a consistent style, including a round image style
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
        .image-round {
            border-radius: 50%;
            width: 300px;
            height: 300px;
            object-fit: cover;
        }
    </style>
    """, unsafe_allow_html=True)

# Home Page
if page == 'Home':
    # Use the st.image function to display the image
    st.image('your_image_url.jpeg', width=300)  # Adjust the width as needed

    # Your greeting and contact information
    st.markdown("""
    ### Hi, I’m Nikhil Ambati 👋
    Buffalo, NY | [(716)-247-3355](tel:+17162473355) | [Email](mailto:nambati@buffalo.edu) | [LinkedIn](https://linkedin.com/in/nikhil-ambati) | [GitHub](https://github.com/nambatibuf)
    """, unsafe_allow_html=True)
    st.markdown("### About Me")
    st.markdown("""
    - 🎓 Pursuing a Master of Science in Data Science from SUNY Buffalo with coursework in Statistical Learning, Data Mining, and Machine Learning.
    - 💼 Experienced Data Engineer with professional experience at Tata Consultancy Services and Accenture Technology.
    - 🌟 Passionate about transforming complex data into actionable insights and enhancing decision-making processes.
    - 🛠️ Technical proficiency in Python, Scala, SQL, AWS, Azure, and big data technologies.
    - 💡 Led projects such as Sales Flow Pro and transformed sales data into insights with AI-driven SQL queries.
    - 🚀 Aim to leverage my skills in data analysis and engineering to make a significant impact in the field of data science.
    """)
    
    st.markdown("### Projects")
    st.markdown("""
    - **Sales Flow Pro**: Developed an analytics pipeline integrating Python, Airflow, GCP, and BigQuery, culminating in a Looker Studio dashboard for data quality checks.
    - **AI-Driven SQL Queries**: Transformed sales data into BCNF compliance using PySpark and PostgreSQL, and created a local website for AI-driven SQL query capabilities.
    """)
    
    st.markdown("### Technical Skills")
    st.markdown("""
    - **Languages**: Python, R, Scala, SQL, C++, Java, SAP ABAP, MATLAB
    - **Technologies**: AWS, Azure, Apache Spark, Hadoop, GCP, Docker, Linux, Tableau, Power BI
    - **Libraries & Databases**: SQL Server, PostgreSQL, MySQL, Snowflake, MongoDB, Oracle, SAP S/4 HANA
    - **Certifications**: Azure Data Engineer Associate, Data Fundamentals, AI Fundamentals
    """)
    
    st.markdown("### Education")
    st.markdown("""
    - **Master of Science in Data Science**  
      State University Of New York At Buffalo  
      January 2023 – May 2024  
      Courses: Statistical Learning & Data Mining, Machine Learning, Data Models & Query Languages, Predictive Analytics.
    - **B.E. in Information Technology**  
      University Of Mumbai  
      August 2015 – June 2019  
      Courses: Advance Database Management Systems, Big Data Analytics & Cloud Computing, Software Engineering.
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
# ... your existing Streamlit code ...

elif page == 'ML Model':
    st.title('Databricks ML Model Prediction')

    # Define inputs for the user to fill in
    prod_practice_desc = st.text_input("Production Practice Description")
    util_practice_desc = st.text_input("Utilization Practice Description")
    commodity_desc = st.text_input("Commodity Description")
    statisticcat_desc = st.text_input("Statistic Category Description")
    year = st.number_input("Year", min_value=1900, max_value=2100, step=1)

    # Button to make prediction
    if st.button('Predict'):
        # Collect the inputs into a list
        input_data = [
            prod_practice_desc,
            util_practice_desc,
            commodity_desc,
            statisticcat_desc,
            int(year)  # Ensure the year is an integer
        ]
        
        # Create the payload for the request
        data_json = create_json_payload(input_data)
        
        # URL of your Databricks endpoint
        url = 'https://adb-5969458442430489.9.azuredatabricks.net/serving-endpoints/temp/invocations'
        
        # Headers including the authorization token
        # NOTE: Store your token in Streamlit's secrets or as an environment variable for security
        headers = {
            'Authorization': f'Bearer {"your_databricks_token"}',
            'Content-Type': 'application/json'
        }
        
        # Send the request
        response = requests.post(url, headers=headers, json=data_json)
        
        # Check if the request was successful
        if response.status_code == 200:
            prediction = response.json()
            st.success(f"Prediction: {prediction}")
        else:
            st.error(f"Failed to get prediction. Status code: {response.status_code}, Response: {response.text}")

    # Add the content for the Footer
    st.sidebar.markdown('---')
    st.sidebar.info('This Streamlit app showcases the portfolio of Nikhil Ambati, a Data Engineer and Data Scientist.')


st.sidebar.markdown('---')
st.sidebar.info('This Streamlit app showcases the portfolio of Nikhil Ambati, a Data Engineer and Data Scientist.')
