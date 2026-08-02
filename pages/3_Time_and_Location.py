import streamlit as st
import pandas as pd
import plotly.express as px

from theme import apply_theme
apply_theme()

st.set_page_config(
    page_title='Time & Location Trends',
    page_icon = '🌍',
    layout='wide'
)

st.title('Time & Location Trends')
st.markdown("Explore how time and location influence restaurant engagement patterns.")

st.markdown('---')

# Top cities by engagement

st.subheader('Top Cities by Engagement Metrics')
st.markdown("**Philadelphia** emerges as the premier city with the highest success score, combining strong star ratings and active user engagement.")

top_cities_df = pd.DataFrame({
    'City':['Philadelphia', 'Tampa', 'Indianapols','Tucson', 'Nashville', 'New Orleans', 'Saint Louis', 'Reno', 'Edmonton', 'Boise' ],
    'State': ['PA', 'FL', 'IN', 'AZ', 'TN', 'LA', 'MO', 'NV', 'AB', 'ID'],
    'Average Rating': [3.53, 3.57, 3.41, 3.39, 3.49, 3.69, 3.41, 3.48, 3.51, 3.56],
    'Total Review Count': [175487, 104376, 92639, 91613, 87070, 69239, 51490, 48393, 45916, 36104],
    'Restaurant Count': [3001, 1715, 1701, 1419, 1404, 1012, 811, 589, 1546, 561]
})

st.dataframe(top_cities_df, use_container_width=True)


st.markdown('---')

st.subheader('Peak Operating & Engagement Hours')
st.markdown('Analysis of review and tip timestamps shows that restaurants experience their highest levels of customer engagement between **4 PM and 1 AM**, reflecting prime dinner and evening social demand.')

hourly_engagement_df = pd.DataFrame({
    'Hour of Day': list(range(24)),
    'Engagement Volume': [65000, 62000, 55000, 40000, 28000, 18000, 11000, 7000, 5000, 4000, 5000, 9000, 14000, 22000, 30000, 37000, 53000, 62000, 64000, 61000, 59000, 60000, 66000, 71000]
})



fig = px.bar(
    hourly_engagement_df,
    x='Hour of Day',
    y='Engagement Volume',
    title='Hourly Engagement Patterns',
    color='Engagement Volume',
    color_continuous_scale='Oranges',

)

st.plotly_chart(fig, use_container_width=True)

if st.button('⬅️Back to Home'):
    st.switch_page('home.py')
