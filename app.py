import streamlit as st

from theme import apply_theme
apply_theme()

st.set_page_config(
    page_title = 'Restaurant success dashboard',
    page_icon="🍽️",
    layout = 'wide',   
)


st.title('Restaurant success dashboard')
st.markdown("Welcome to the Yelp Data Analytics platform. Explore customer engagement, rating dynamics, and geographical trends.")

#KPIs
 
st.markdown('---')
st.subheader('Dataset Overview')

col1,col2,col3,col4 = st.columns(4)

with col1: 
    st.metric(label='Total Restaurants', value='35000')

with col2: 
    st.metric(label='Average Rating', value='3.48')

with col3: 
    st.metric(label='Average Reviews', value='56')

with col4: 
    st.metric(label='Top City', value='Philadelphia')


st.markdown('---')

# Navigation 

st.subheader('Explore Analytical Modules')
st.markdown('Select a module below to dive deep into the specific analyses:')

col1_b1, col2_b1, col3_b1 = st.columns(3)

with col1_b1:
    if st.button('📊Customer Engagement Analysis'):
        st.switch_page('pages/1_User_Engagement.py')

with col2_b1:
    if st.button('⭐Rating & Success Analysis'):
        st.switch_page('pages/2_Rating_Analysis.py')

with col3_b1:
    if st.button('🌍 Time & Location Trends'):
        st.switch_page('pages/3_Time_and_Location.py')

# Footer

st.markdown('---')
st.caption('Developed by Anushka dabas. Data sourced from Yelp. For inquiries, contact anushhkadabas@gmail.com')