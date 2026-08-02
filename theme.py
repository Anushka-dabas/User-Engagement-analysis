import streamlit as st

def apply_theme():
    st.markdown("""
    <style>
        /* 1. Main Background a few shades deeper (#E9ECEF) */
        .stApp, .main, .block-container, [data-testid="stMain"] {
            background-color: #E9ECEF !important;
            color: #1E293B !important;
        }
        
        /* 2. Sidebar Slate-Gray Background & White Text */
        [data-testid="stSidebar"], section[data-testid="stSidebar"], [data-testid="stSidebar"] > div:first-child {
            background-color: #6D8196 !important;
            border-right: 1px solid #5A6E82 !important;
        }
        [data-testid="stSidebar"] span, [data-testid="stSidebar"] p, [data-testid="stSidebar"] div, [data-testid="stSidebar"] label, [data-testid="stSidebar"] a {
            color: #FFFFFF !important;
            font-weight: 500 !important;
        }
        
        /* 3. Main Headings in #01796F */
        h1, h2, h3, h4, h5, h6, 
        div[data-testid="stMarkdownContainer"] h1,
        div[data-testid="stMarkdownContainer"] h2,
        div[data-testid="stMarkdownContainer"] h3 {
            color: #01796F !important;
            font-weight: 700 !important;
        }
        p, span, label, .stMarkdown, .stText, li {
            color: #334155 !important;
        }
        
        /* 4. Metric & Content Cards (Kept crisp white so they pop against the deeper background) */
        div[data-testid="stMetric"], div[data-testid="column"] > div {
            background-color: #FFFFFF !important;
            border-radius: 10px;
            padding: 15px;
            box-shadow: 0 1px 3px rgba(0,0,0,0.05);
            border: 1px solid #CBD5E1 !important;
        }
        div[data-testid="stMetric"] label, div[data-testid="stMetric"] div {
            color: #1E293B !important;
        }
        
        /* 5. Dropdown / Selectbox */
        .stSelectbox div[data-baseweb="select"] {
            background-color: #FFFFFF !important;
            color: #1E293B !important;
            border-color: #CBD5E1 !important;
        }
        .stSelectbox div[data-baseweb="select"] * {
            color: #1E293B !important;
        }
        div[data-baseweb="popover"] div[role="listbox"] {
            background-color: #FFFFFF !important;
            color: #1E293B !important;
        }
        
        /* 6. Buttons */
        .stButton>button {
            background-color: #01796F !important;
            color: #FFFFFF !important;
            border-radius: 8px;
            border: none;
            font-weight: 600;
        }
        .stButton>button p, .stButton>button span {
            color: #FFFFFF !important;
        }
        .stButton>button:hover {
            background-color: #0B2E33 !important;
            color: #FFFFFF !important;
        }
    </style>
    """, unsafe_allow_html=True)