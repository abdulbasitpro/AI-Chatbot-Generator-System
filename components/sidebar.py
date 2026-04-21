import streamlit as st

def render_sidebar():
    st.sidebar.title("🤖 AI Chatbot Generator")
    st.sidebar.markdown("---")
    st.sidebar.markdown(
        """
        Build custom AI chatbots powered by Llama 3.1 & Gemma 2.
    """)
    st.sidebar.markdown("<br>", unsafe_allow_html=True)
    st.sidebar.page_link("app.py", label="Home", icon="🏠")
    st.sidebar.page_link("pages/1_Dashboard.py", label="Dashboard", icon="📊")
    st.sidebar.page_link("pages/2_Builder.py", label="Builder", icon="🛠️")
    st.sidebar.page_link("pages/3_Chat.py", label="Chat", icon="💬")
    st.sidebar.markdown("---")
    st.sidebar.caption("Powered by Groq API")
