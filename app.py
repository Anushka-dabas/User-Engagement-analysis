import streamlit as st
import pandas as pd
import plotly.express as px

# 1. Page Configuration 
st.set_page_config(
    page_title="Yelp Restaurant Engagement Analysis",
    page_icon="🍽️",
    layout="wide"
)

# 2. App Title & Introduction
st.title("🍽️ Yelp Restaurant Engagement & Sentiment Analysis")
st.markdown("""
This application analyzes structured Yelp data to uncover insights on customer engagement, sentiment distribution, and operational trends for restaurant stakeholders.
""")

# 3. Key Metrics Row 
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("Total Businesses Analyzed", "31,537")
with col2:
    st.metric("Average Star Rating", "3.48 / 5.0")
with col3:
    st.metric("Average Review Count", "56 per venue")
with col4:
    st.metric("Top Engagement City", "Philadelphia")

st.markdown("---") 

# 4. Visualizations Section: Engagement vs Ratings
st.header("📊 Customer Engagement vs. Restaurant Ratings")
col_left, col_right = st.columns(2)

with col_left:
    st.subheader("Average Engagement by Rating Level")
    
    # Creating a small data table based on your analysis findings
    rating_data = pd.DataFrame({
        'Rating': ['1.0', '1.5', '2.0', '2.5', '3.0', '3.5', '4.0', '4.5', '5.0'],
        'Avg Review Count': [14.3, 24.3, 27.7, 36.6, 48.0, 63.7, 73.1, 65.2, 31.1],
        'Avg Checkin Count': [17.5, 34.4, 52.3, 79.3, 105.9, 125.7, 127.1, 86.1, 27.5]
    })
    
    # Building an interactive Plotly bar chart
    fig_bar = px.bar(
        rating_data, 
        x='Rating', 
        y=['Avg Review Count', 'Avg Checkin Count'], 
        barmode='group', 
        title="Review & Check-in Volume across Star Ratings"
    )
    st.plotly_chart(fig_bar, use_container_width=True)

with col_right:
    st.subheader("Key Takeaway on Ratings")
    st.info("""
    - **Engagement Peaks at 4 Stars:** Venues with a 4.0-star rating experience the highest user interaction.
    - **The 5-Star Saturation Paradox:** Engagement drops sharply at the 5.0-star level, indicating a saturation or selectivity point where fewer customers leave feedback.
    """)


# 5. Sentiment Analysis Overview
st.markdown("---")
st.header("💬 Review Sentiment Analysis (VADER NLP)")
col_s1, col_s2 = st.columns(2)

with col_s1:
    sentiment_data = pd.DataFrame({
        'Sentiment': ['Positive', 'Neutral', 'Negative'],
        'Percentage': [72.5, 18.2, 9.3]
    })
    fig_pie = px.pie(
        sentiment_data, 
        names='Sentiment', 
        values='Percentage', 
        title="Overall Sentiment Distribution in Sampled Reviews",
        color_discrete_sequence=['#2ecc71', '#f1c40f', '#e74c3c']
    )
    st.plotly_chart(fig_pie, use_container_width=True)

with col_s2:
    st.subheader("Operational Recommendations")
    st.markdown("""
    1. **Optimize Staffing During Peak Hours:** Check-in trends show heavy activity blocks requiring aligned staffing.
    2. **Leverage Positive Feedback Loops:** High-rated venues show strong cross-platform engagement.
    3. **Proactive Review Management:** Monitoring negative sentiment helps operators resolve friction swiftly.
    """)

# Footer
st.markdown("---")
st.markdown("Developed as part of a Data Analytics Portfolio | Target Role: Data Analyst at Google")