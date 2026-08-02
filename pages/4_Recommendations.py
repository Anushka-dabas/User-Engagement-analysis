import streamlit as st
from theme import apply_theme
apply_theme()

st.set_page_config(
    page_title="Strategic Recommendations",
    page_icon="💡",
    layout="wide"
)


st.title("Strategic Recommendations & Business Insights")
st.markdown("""
Based on the comprehensive Yelp dataset analysis across 35,000 restaurants, here are the core data-driven recommendations for stakeholders, restaurant owners, and investors.
""")

st.markdown("---")


col1, col2 = st.columns(2)

with col1:
    st.subheader(" 1. Leverage Elite User Influence")
    st.markdown("""
    * **High Impact:** Elite users make up a small fraction of the community (approx. 4.6%) but account for a major share of total reviews (over 55%).
    * **Action:** Build strong relationships with elite users through exclusive experiences or loyalty programs to amplify brand visibility and customer trust.
    """)

    st.subheader(" 2. Capitalize on Peak Operating Hours")
    st.markdown("""
    * **Evening Demand:** User engagement peaks heavily between **4 PM and 1 AM**[cite: 1].
    * **Action:** Optimize staffing levels, kitchen efficiency, and resource allocation during these hours to ensure smooth operations and superior service delivery[cite: 1].
    """)

with col2:
    st.subheader(" 3. Focus on Service Quality & Engagement")
    st.markdown("""
    * **Sustained Growth:** Successful restaurants maintain steady or growing engagement over time, reflecting ongoing customer interest[cite: 1].
    * **Action:** Less successful businesses should focus on enhancing service quality and actively responding to customer feedback to build long-term interaction[cite: 1].
    """)

    st.subheader(" 4. Strategic Geographic Expansion")
    st.markdown("""
    * **Thriving Markets:** Cities like Philadelphia, Tampa, Indianapolis, and Tucson exhibit the highest success scores[cite: 1].
    * **Investment:** These top-performing metropolitan areas present prime opportunities for restaurant chains looking to expand or invest further[cite: 1].
    """)

# 4. Bottom Navigation
st.markdown("---")
if st.button("⬅️ Back to Home"):
    st.switch_page("home.py")