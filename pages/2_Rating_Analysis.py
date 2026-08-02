import streamlit as st
import pandas as pd
import plotly.express as px

from theme import apply_theme
apply_theme()

st.set_page_config(
    page_title= 'Rating Analysis',
    page_icon = '⭐',
    layout= 'wide'
)

st.title('Rating & Success Analysis')
st.markdown("""This page examines how restaurant ratings compare with review volumes, highlighting differences between high-rated and low-rated establishments.""")


st.markdown('---')

# High-Rated vs. Low-Rated

st.subheader('High-Rated vs. Low-Rated Restaurant Engagement')

st.markdown('Restaurants categorized as **High-Rated** (3.5 stars and above) exhibit significantly higher average customer engagement across reviews, check-ins, and tips compared to lower-rated venues.')

rating_distribution_df = pd.DataFrame({
    'Rating Category': ['High-Rated (>=3.5 stars)', 'Low-Rated (<3.5 stars)'],
    'Average Review Count': [63.10, 37.15],
    'Average Check-in Count': [80.72, 64.84],
    'Average Tip Count': [8.07, 5.46]

})

st.dataframe (rating_distribution_df, use_container_width=True)

st.markdown('---')

# Charts

st.subheader("Visualizing Engagement by Rating Category")
st.markdown("Compare the differences in review, check-in, and tip volumes between high-rated and low-rated restaurants.")

melted_df = rating_distribution_df.melt(
    id_vars='Rating Category',
    value_vars=['Average Review Count', 'Average Check-in Count', 'Average Tip Count'],
    var_name='Engagement Type',
    value_name='Average Count'
)

fig = px.bar(
    melted_df,
    x='Engagement Type',
    y='Average Count',
    color='Rating Category',
    barmode='group',
    title='Engagement Metrics: High-Rated vs. Low-Rated Restaurants',
    color_discrete_sequence=['#F8862C', '#CB754B'],
)

st.plotly_chart(fig, use_container_width=True)

if st.button('⬅️Back to Home'):
    st.switch_page('app.py')