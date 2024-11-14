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

if 'License Type' in df.columns and 'City' in df.columns:
    # Group by License Type and City to calculate count
    license_city_counts = df.groupby(['License Type', 'City']).size().reset_index(name='Count')

    st.write("### Heatmap of License Type by City")

    # Create Heatmap
    heatmap = alt.Chart(license_city_counts).mark_rect().encode(
        x=alt.X('City:N', title='City', sort='-y', axis=alt.Axis(labelAngle=-45)),
        y=alt.Y('License Type:N', title='License Type'),
        color=alt.Color('Count:Q', scale=alt.Scale(scheme='blues'), title='License Count'),
        tooltip=['License Type:N', 'City:N', 'Count:Q']
    ).properties(
        width=800,
        height=600,
        title="Heatmap of License Types across Cities"
    )

    st.altair_chart(heatmap)
else:
    st.write("The dataset does not have the required columns 'License Type' or 'City'.")