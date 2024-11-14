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
    # Group data by Business Name and City
    business_city_counts = df.groupby(['City', 'Business Name']).size().reset_index(name='Count')

    st.write("### Bubble Chart of Licenses by Business Name and City")

    # Create Bubble Chart
    bubble_chart = alt.Chart(business_city_counts).mark_circle().encode(
        x=alt.X('City:N', title='City', sort='-y'),
        y=alt.Y('Business Name:N', title='Business Name'),
        size=alt.Size('Count:Q', title='License Count', scale=alt.Scale(range=[10, 1000])),  # Circle size
        color=alt.Color('City:N', legend=None),  # Optional: use color to differentiate cities
        tooltip=['City:N', 'Business Name:N', 'Count:Q']  # Interactive tooltip
    ).properties(
        width=1000,
        height=800,
        title="Bubble Chart of Licenses by Business Name and City"
    )

    st.altair_chart(bubble_chart)

else:
    st.write("The dataset does not have the required columns 'Business Name' or 'City'.")