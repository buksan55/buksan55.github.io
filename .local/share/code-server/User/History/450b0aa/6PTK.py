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
if 'Original Issue Date' in df.columns and 'Business Name' in df.columns:
    # Convert DATE ISSUED to datetime
    df['Original Issue Date'] = pd.to_datetime(df['Original Issue Date'], errors='coerce')
    
    # Group by Business Name and Date
    business_time_series = df.groupby([df['Original Issue Date'].dt.year, 'Business Name']).size().reset_index(name='Count')
    business_time_series.columns = ['Year', 'Business Name', 'Count']

    st.write("### Licenses Issued Over Time by Business Name")
    


    # Line Chart with Business Name
    top_businesses = df['Business Name'].value_counts().head(10).index
    filtered_df = df[df['Business Name'].isin(top_businesses)]
    line_chart = alt.Chart(business_time_series).mark_line().encode(
        x='Year:O',
        y='Count:Q',
        color='Business Name:N',
        tooltip=['Year:O', 'Business Name:N', 'Count:Q']
    ).properties(width=1000, height=800)

    st.altair_chart(line_chart)
else:
    st.write("The dataset does not have the required columns 'DATE ISSUED' or 'BUSINESS NAME'.")