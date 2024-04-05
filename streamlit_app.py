import streamlit as st
import requests


# Page title and favicon for the entire app
st.set_page_config(page_title="Nikhil Ambati's Portfolio", page_icon=":bar_chart:", layout="wide")

with st.container():
    st.markdown("## Nikhil Ambati's Portfolio")
    page = st.selectbox('Navigate to', ['Home', 'Projects', 'Power BI Report', 'ML Model'], index=0)
    if page == 'Projects':
        project_page = st.selectbox('Select Project', ['Smart Farming', 'Project 2', 'Project 3'])
    else:
        project_page = None


def create_json_payload(input_data):
    return {
        "dataframe_split": {
            "columns": [
                "PRODN_PRACTICE_DESC",
                "UTIL_PRACTICE_DESC",
                "COMMODITY_DESC",
                "STATISTICCAT_DESC",
                "year"
            ],
            "data": [input_data]
        }
    }
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
    - 🚀 Aim to leverage my skills in data engineering to make a significant impact in the field of data science.
    """)
    
    st.markdown("### Projects")
    st.markdown("""
    - **Sales Flow Pro**: Developed an analytics pipeline integrating Python, Airflow, GCP, and BigQuery, culminating in a Looker Studio dashboard for data quality checks.
    - **AI-Driven SQL Queries**: Transformed sales data into BCNF compliance using PySpark and PostgreSQL, and created a local website for AI-driven SQL query capabilities.
    - **Data-Driven Agricultural Insights**:
        - Automated data pipeline utilizing Azure Data Factory, Databricks, and Delta Lake to process USDA datasets. This ensures real-time, actionable insights through Power BI visualizations and a predictive analytics dashboard hosted online.
        - Developed sophisticated machine learning models to predict crop yields, classifying them as high or low. Enabled monthly retraining to refine predictions, leveraging transformed data in Delta Lake.
        - Launched an interactive web platform allowing users to input parameters and receive yield predictions. This showcases a commitment to accessibility and user engagement in the agricultural sector.
    """, unsafe_allow_html=True)
    
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

elif project_page:
    if project_page == 'Smart Farming':
        # Smart Farming Project content
        elif page == 'Smart Farming':
            st.title('Smart Farming Initiative: Revolutionizing Agriculture with Data Analytics')
        
            st.markdown("""
            ## Project Overview:
        
            In an age where agriculture meets digital innovation, the Smart Farming Initiative epitomizes the transformative power of data analytics. By leveraging a vast dataset from the USDA, we are pioneering a new approach to farming that enhances efficiency, sustainability, and economic viability. Our robust data pipeline offers unprecedented insights, guiding farmers and stakeholders towards environmentally conscious decisions that also boost profitability.
        
            ## Technical Architecture:
        
            The backbone of our initiative is the Azure Data Factory (ADF) pipeline, engineered for high-performance data handling:
            
            - **Data Ingestion**: Scheduled tasks faithfully gather the USDA datasets at 3:30 AM daily, ensuring that our data is as fresh as the morning harvest.
            - **Extraction and Transformation**: Our pipeline adeptly processes the ZIP files, converting them into Parquet format within Azure Data Lake Storage Gen2—a testament to efficiency and scalability.
            - **Orchestration and Logging**: Orchestrated workflows and meticulous logging are the unsung heroes, ensuring smooth operations and transparent process tracking.
            - **Databricks Ecosystem**: Delta Lake on Databricks forms the sanctum for our data, enshrined with ACID transactions, while Hive metastore integration provides a structured query layer for analysis.
        
            ## Operational Excellence:
        
            Our pipeline is not just a marvel of automation; it's the standard-bearer for operational excellence in data-driven agriculture. Running transformations at 3:40 AM, we refine raw data into a canvas of intelligence that paints a clear picture of crop yields and farming practices.
        
            ## Impact:
        
            The Smart Farming Initiative isn't merely a project; it's a manifesto for the future of farming. By marrying cutting-edge technology with the timeless art of agriculture, we're equipping farmers with a powerful lens to view and optimize their practices.
        
            ## Enhancing Predictive Analytics and Visualization:
        
            The journey doesn't end with data collection and transformation; it extends into the realm of predictive analytics and rich visualizations:
            
            - **Interactive Dashboards**: Through Power BI, we offer a window into the soul of farming data, providing real-time insights and enabling deep dives into critical metrics.
            
            ## Machine Learning Advancements:
        
            We leverage Databricks' computational might to prepare our data for machine learning, setting the stage for predictive models that forecast crop yields with remarkable accuracy.
            
            - **Predictive Modeling**: We employ a dual-model strategy to classify crop yields and predict numerical outcomes, capturing the nuances of agricultural productivity.
            - **Model Retraining Pipeline**: A dedicated pipeline for model retraining embodies our commitment to adaptability, ensuring our predictions evolve alongside the changing tides of data.
        
            ## Web Integration and Interactive Prediction:
        
            The initiative culminates in a user-friendly interface, where stakeholders engage with our models in real time to gain instant predictions:
            
            - **Real-Time Predictions**: Stakeholders can directly input parameters into our web portal, sparking our models to life and delivering predictions within moments.
            
            ## Accessibility:
        
            Hosted on a dedicated platform, our analytics tools break free from the confines of complexity, offering intuitive access to those who steward the land.
        
            Experience our Interactive Smart Farming Platform and see how data analytics is sowing seeds for a brighter agricultural future: [Launch the Platform](https://app-4zwfadkqr5d7vsetidxdhp.streamlit.app/).
            """, unsafe_allow_html=True)

    elif project_page == 'Project 2':
        # Project 2 content
        # ...
    elif project_page == 'Project 3':
        # Project 3 content
        # ...
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
            'Authorization': f'Bearer {"dapic2ee1f0502ff40015b06a22379d25e12-3"}',
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

# ... your existing Streamlit code ...


# ... the rest of your Streamlit code ...

    
st.sidebar.markdown('---')
st.sidebar.info('This Streamlit app showcases the portfolio of Nikhil Ambati, a Data Engineer and Data Scientist.')
