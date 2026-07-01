import streamlit as st
from streamlit_option_menu import option_menu
import os

# -----------------------------
# PAGE CONFIG
# -----------------------------
st.set_page_config(
    page_title="Customer Churn Prediction",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# -----------------------------
# LOAD CSS
# -----------------------------
def load_css():
    css_path = os.path.join("assets", "style.css")

    if os.path.exists(css_path):
        with open(css_path, "r", encoding="utf-8") as f:
            st.markdown(
                f"<style>{f.read()}</style>",
                unsafe_allow_html=True
            )

load_css()

# -----------------------------
# SIDEBAR
# -----------------------------
with st.sidebar:

    st.image(
        "https://img.icons8.com/color/96/artificial-intelligence.png",
        width=70
    )

    st.markdown("## Customer Churn")
    st.caption("AI Powered Analytics")

    selected = option_menu(
        menu_title=None,
        options=[
            "Home",
            "Dashboard",
            "Prediction",
            "Visualizations",
            "About"
        ],
        icons=[
            "house-fill",
            "bar-chart-fill",
            "cpu-fill",
            "graph-up-arrow",
            "info-circle-fill"
        ],
        menu_icon="cast",
        default_index=0,
        styles={
            "container": {
                "padding": "0!important",
                "background-color": "#0E1117",
            },
            "icon": {
                "color": "#4CAF50",
                "font-size": "18px",
            },
            "nav-link": {
                "font-size": "16px",
                "text-align": "left",
                "margin": "4px",
                "--hover-color": "#1f77b4",
            },
            "nav-link-selected": {
                "background-color": "#3b82f6",
            },
        },
    )

# -----------------------------
# PAGE ROUTING
# -----------------------------
try:

    if selected == "Home":
        from pages.home import show_home
        show_home()

    elif selected == "Dashboard":
        from pages.dashboard import show_dashboard
        show_dashboard()

    elif selected == "Prediction":
        from pages.prediction import show_prediction
        show_prediction()

    elif selected == "Visualizations":
        from pages.visualization import show_visualization
        show_visualization()

    elif selected == "About":
        from pages.about import show_about
        show_about()

except Exception as e:
    st.exception(e)

# -----------------------------
# FOOTER
# -----------------------------
st.markdown("---")

st.markdown(
    """
    <div style='text-align:center;color:gray;'>

    Customer Churn Prediction System<br>
    Built with ❤️ using Python, Streamlit, Scikit-learn & XGBoost<br>
    © 2026

    </div>
    """,
    unsafe_allow_html=True
)