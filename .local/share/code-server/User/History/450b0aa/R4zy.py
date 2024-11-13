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

    # Filter the data
    filtered_data = business_city_counts[
        (business_city_counts['City'].isin(selected_cities)) &
        (business_city_counts['Business Name'].isin(selected_businesses))
    ]

    st.write("### Improved Bubble Chart of Licenses by Business Name and City")

    # Improved Bubble Chart
    bubble_chart = alt.Chart(filtered_data).mark_circle().encode(
        x=alt.X('City:N', sort='-y', title='City', axis=alt.Axis(labelAngle=-45)),  # Rotate city names for readability
        y=alt.Y('Business Name:N', title='Business Name', sort='-x'),  # Top-down sort for clarity
        size=alt.Size('Count:Q', title='License Count', scale=alt.Scale(range=[100, 1000])),  # Adjust size scale for less overlap
        color=alt.Color('Count:Q', scale=alt.Scale(scheme='viridis'), title='Count'),  # Use a perceptually uniform color scale
        tooltip=['City:N', 'Business Name:N', 'Count:Q']  # Add detailed tooltips
    ).properties(
        width=800,
        height=600,
        title="Licenses by Business Name and City (Filtered and Optimized)"
    ).configure_title(
        fontSize=20,
        anchor='start'
    )

    st.altair_chart(bubble_chart)
else:
    st.write("The dataset does not have the required columns 'Business Name' or 'City'.")