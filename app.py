from pathlib import Path

import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Appointment Booking",
    page_icon="📅",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# Remove Streamlit chrome so the booking app fills the page
st.markdown(
    """
    <style>
      #MainMenu, footer, header {visibility: hidden;}
      .block-container {padding: 0 !important; max-width: 100% !important;}
      iframe {border: 0; border-radius: 0;}
    </style>
    """,
    unsafe_allow_html=True,
)

HTML_FILE = Path(__file__).parent / "index.html"

if HTML_FILE.exists():
    components.html(HTML_FILE.read_text(encoding="utf-8"), height=1100, scrolling=True)
else:
    st.error("index.html was not found. Keep it in the same folder as app.py.")
