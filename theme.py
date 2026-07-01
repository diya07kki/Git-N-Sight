import streamlit as st

def apply_theme():
    st.markdown("""
    <style>

    /* Hide Streamlit branding */
    #MainMenu {
        visibility: hidden;
    }

    footer {
        visibility: hidden;
    }


    /* Background */
    .stApp {
        background: #0D1117;
    }

    /* Hero Banner */
    .hero {
        padding: 35px;
        border-radius: 18px;
        background: linear-gradient(
            135deg,
            #161B22,
            #21262D
        );
        border: 1px solid #30363D;
        margin-bottom: 25px;
    }

    .hero h1 {
        color: #58A6FF;
        font-size: 50px;
        margin-bottom: 8px;
    }

    .hero p {
        color: #C9D1D9;
        font-size: 18px;
        line-height: 1.6;
    }

    /* Metric Cards */

    .metric-card{
        background:#161B22;
        padding:22px;
        border-radius:16px;
        border:1px solid #30363D;
        text-align:center;
        transition:.3s;
    }

    .metric-card:hover{
        border-color:#58A6FF;
    }

    .metric-icon{
        font-size:36px;
    }

    .metric-value{
        font-size:34px;
        font-weight:bold;
        color:#58A6FF;
    }

    .metric-title{
        color:#C9D1D9;
        font-size:16px;
    }

    /* Profile Card */

    .profile-card{

        background:#161B22;

        border-radius:18px;

        padding:25px;

        border:1px solid #30363D;
    }
                
    .footer{

        position:fixed;

        bottom:15px;

        left:55%;

        transform:translateX(-50%);

        color:#8B949E;

        font-size:14px;

    }

    </style>
    """, unsafe_allow_html=True)