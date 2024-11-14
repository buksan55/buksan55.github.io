# put streamlit code here as needed
import altair as alt
import streamlit as st
import pandas as pd


url = "https://github.com/UIUC-iSchool-DataViz/is445_data/raw/main/licenses_fall2022.csv"
df = pd.read_csv(url)

# Display the data
st.write("## Licenses Data", df)

# Bar Chart: Count of licenses by license type
st.write("### License Count by Type")
license_count = df['License Type'].value_counts().reset_index()
license_count.columns = ['License Type', 'Count']
bar_chart = alt.Chart(license_count).mark_bar().encode(
    x='License Type',
    y='Count',
    color='License Type'
).properties(width=600, height=400)
st.altair_chart(bar_chart)

if 'Original Issue Date' in df.columns and 'Business Name' in df.columns and 'City' in df.columns:
    # Convert Original Issue Date to datetime
    df['Original Issue Date'] = pd.to_datetime(df['Original Issue Date'], errors='coerce')
    
    # Group by Business Name and City
    business_city_time_series = df.groupby(['Business Name', 'City']).size().reset_index(name='Count')

    st.write("### Licenses Issued by Business Name and City")

    # Filter for top 10 businesses by total licenses issued
    top_businesses = business_city_time_series.groupby('Business Name')['Count'].sum().nlargest(10).index
    filtered_data = business_city_time_series[business_city_time_series['Business Name'].isin(top_businesses)]

    # Line Chart with Business Name and City
    line_chart = alt.Chart(filtered_data).mark_line().encode(
        x='City:N',  # X축에 City 표시
        y='Count:Q',
        color='Business Name:N',
        tooltip=['Business Name:N', 'City:N', 'Count:Q']
    ).properties(width=1000, height=800)

    st.altair_chart(line_chart)
else:
    st.write("The dataset does not have the required columns 'Original Issue Date', 'Business Name', or 'City'.")


