# put streamlit code here as needed
import altair as alt
import streamlit as st
from vega_datasets import data 
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

if 'DATE ISSUED' in df.columns:
    df['DATE ISSUED'] = pd.to_datetime(df['DATE ISSUED'])
    df['Year'] = df['DATE ISSUED'].dt.year
    time_series = df.groupby('Year').size().reset_index(name='Count')
    
    st.write("### Licenses Issued Over Time")
    line_chart = alt.Chart(time_series).mark_line().encode(
        x='Year:O',
        y='Count',
        tooltip=['Year', 'Count']
    ).properties(width=600, height=400)
    st.altair_chart(line_chart)
line_chart

if 'BUSINESS ACTIVITY' in df.columns:
    st.write("### Distribution of Licenses by Business Activity")
    business_activity_count = df['BUSINESS ACTIVITY'].value_counts().reset_index()
    business_activity_count.columns = ['Business Activity', 'Count']
    pie_chart = alt.Chart(business_activity_count).mark_arc().encode(
        theta=alt.Theta(field='Count', type='quantitative'),
        color=alt.Color(field='Business Activity', type='nominal'),
        tooltip=['Business Activity', 'Count']
    ).properties(width=600, height=400)
    st.altair_chart(pie_chart)
else:
    st.write("Business Activity column not found for pie chart visualization.")
pie_chart