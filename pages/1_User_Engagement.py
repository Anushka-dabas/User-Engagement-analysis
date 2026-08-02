import streamlit as st
import pandas as pd
import plotly.express as px

from theme import apply_theme
apply_theme()

st.set_page_config(
    page_title ='Customer Engagement Analysis',
    page_icon='📊',
    layout='wide'
)

st.title('Customer Engagement Analysis')
st.markdown("Analyze how customer interactions, such as reviews, check-ins, and tips, drive restaurant performance.")

st.markdown('---')

# correlation

st.subheader('Interconnection Between Engagement Metrics')
st.markdown('According to the analysis of the Yelp dataset, user engagement metrics across different platforms are heavily interlinked. When activity rises in one area (e.g., reviews), it strongly stimulates activity in others (tips and check-ins).')

correlation_data = pd.DataFrame({
    'Metric':['Review count', 'Check-in count', 'Tip count'],
    'Review Count':[1.00, 0.63, 0.77],
    'Check-in Count':[0.63, 1.00, 0.77],
    'Tip Count': [0.77, 0.77, 1.00]
})


st.dataframe(correlation_data, use_container_width=True)

st.markdown('---')


# charts

st.subheader('Average Engagement by Restaurant Rating')
st.markdown('This chart illustrates how average reviews, check-ins, and tips rise as ratings improve up to 4 stars')

rating_engagement_df = pd.DataFrame({
    'Star Rating':[1,1.5,2,2.5,3,3.5,4,4.5,5],
    'Avg Review Count': [14.36, 24.36, 27.76, 36.63, 48.05, 63.73, 73.14, 65.28, 31.13],
    'Avg Checkin Count':[17.52, 34.48, 52.39, 79.35, 105.97, 125.78, 127.14, 86.18, 27.55],
    'Avg Tip Count':[2.78, 3.88, 4.58, 6.33, 8.30, 10.32, 11.33, 9.00, 4.27]
                         
})

metric_choice = st.selectbox(
    'choose metric to visualize:',
    ['Avg Review Count', 'Avg Checkin Count', 'Avg Tip Count']
)


fig = px.bar(
    rating_engagement_df,
    x='Star Rating',
    y=metric_choice,
    title=f'{metric_choice} across restaurant ratings',
    color=metric_choice,
    color_continuous_scale='Oranges'
)

st.plotly_chart(fig, use_container_width=True)


# Bottom navigation

st.markdown('---')
if st.button('⬅️ Back to home'):
    st.switch_page('app.py')

