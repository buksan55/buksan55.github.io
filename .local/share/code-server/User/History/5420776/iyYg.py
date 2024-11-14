# put streamlit code here as needed
import altair as alt
import streamlit as st
import pandas as pd


url = "https://github.com/UIUC-iSchool-DataViz/is445_data/raw/main/licenses_fall2022.csv"
df = pd.read_csv(url)

st.write("## Licenses Data", df)

st.write("### License Count by Type")
license_count = df['License Type'].value_counts().reset_index()
license_count.columns = ['License Type', 'Count']
bar_chart = alt.Chart(license_count).mark_bar().encode(
    x='License Type',
    y='Count',
    color='License Type'
).properties(width=600, height=400)
st.altair_chart(bar_chart)

st.text("I am highlighting the distribution of licenses issued across different License Types and Cities to reveal trends and disparities in lincensig activity.")
st.text("The primary feature being emphasized ")
st.text("")
if 'License Type' in df.columns and 'City' in df.columns and 'Original Issue Date' in df.columns:
    df['Original Issue Date'] = pd.to_datetime(df['Original Issue Date'], errors='coerce')
    
    df['Year'] = df['Original Issue Date'].dt.year
    license_city_time_series = df.groupby(['Year', 'License Type', 'City']).size().reset_index(name='Count')

    st.write("### Licenses Issued Over Time by License Type and City")

    selected_cities = st.multiselect(
        "Select Cities",
        options=license_city_time_series['City'].unique(),
        default=license_city_time_series['City'].unique()[:5]  
    )
    selected_license_types = st.multiselect(
        "Select License Types",
        options=license_city_time_series['License Type'].unique(),
        default=license_city_time_series['License Type'].unique()[:3]  
    )

    filtered_data = license_city_time_series[
        (license_city_time_series['City'].isin(selected_cities)) &
        (license_city_time_series['License Type'].isin(selected_license_types))
    ]

    
    line_chart = alt.Chart(filtered_data).mark_line().encode(
        x='Year:O',
        y='Count:Q',
        color='License Type:N',
        strokeDash='City:N',  
        tooltip=['Year:O', 'License Type:N', 'City:N', 'Count:Q']
    ).properties(
        width=800,
        height=500,
        title="Licenses Issued Over Time by License Type and City"
    )

    st.altair_chart(line_chart)
else:
    st.write("The dataset does not have the required columns 'License Type', 'City', or 'Original Issue Date'.")
