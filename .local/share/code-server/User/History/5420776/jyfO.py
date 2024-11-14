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

if 'Business Name' in df.columns and 'City' in df.columns:
    # Group by Business Name and City to calculate count
    business_city_counts = df.groupby(['Business Name', 'City']).size().reset_index(name='Count')

    st.write("### Licenses Count by Business Name and City (Bar Chart)")

    # Bar Chart
    bar_chart = alt.Chart(business_city_counts).mark_bar().encode(
        x=alt.X('Business Name:N', sort='-y', title='Business Name'),
        y=alt.Y('Count:Q', title='License Count'),
        color='City:N',
        tooltip=['Business Name:N', 'City:N', 'Count:Q']
    ).properties(width=1000, height=500)

    st.altair_chart(bar_chart)

    st.write("### Heatmap of Licenses by Business Name and City")

    # Heatmap
    heatmap = alt.Chart(business_city_counts).mark_rect().encode(
        x=alt.X('City:N', title='City'),
        y=alt.Y('Business Name:N', title='Business Name', sort='-x'),
        color=alt.Color('Count:Q', scale=alt.Scale(scheme='blues'), title='License Count'),
        tooltip=['Business Name:N', 'City:N', 'Count:Q']
    ).properties(width=800, height=600)

    st.altair_chart(heatmap)
else:
    st.write("The dataset does not have the required columns 'Business Name' or 'City'.")