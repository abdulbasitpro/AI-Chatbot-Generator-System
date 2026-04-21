import streamlit as st
import streamlit.components.v1 as components

def get_design_system_css():
    return """
<style>
/* Dark theme matching Stitch design tokens */
:root {
    --bg-primary: #0A0E1A;
    --bg-secondary: #111827;
    --bg-surface: #1E2433;
    --accent: #6366F1;
    --accent-hover: #4F46E5;
    --text-primary: #F1F5F9;
    --text-secondary: #94A3B8;
    --border: #1E2D45;
    --green: #10B981;
    --radius: 12px;
    --font: 'Inter', sans-serif;
}

.stApp { background: var(--bg-primary) !important; color: var(--text-primary) !important; }
.stAppHeader { background: transparent !important; }
.stChatMessage { background: var(--bg-surface) !important; border-radius: var(--radius) !important; border: 1px solid var(--border); }
.stTextInput input, .stTextArea textarea, .stSelectbox select {
    background: var(--bg-secondary) !important;
    border: 1px solid var(--border) !important;
    color: var(--text-primary) !important;
    border-radius: 8px !important;
}
button[kind="primary"] {
    background: var(--accent) !important;
    border: none !important;
    border-radius: 8px !important;
    color: white !important;
}
button[kind="primary"]:hover {
    background: var(--accent-hover) !important;
}
</style>
"""

st.set_page_config(
    page_title="AI Chatbot Generator System",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Inject global CSS
st.markdown(get_design_system_css(), unsafe_allow_html=True)

from components.sidebar import render_sidebar

render_sidebar()

st.markdown("""
<div style="text-align: center; padding: 4rem 2rem;">
    <h1 style="color: var(--text-primary); font-size: 3.5rem; font-weight: 800; margin-bottom: 1rem; font-family: var(--font);">
        AI Chatbot Generator
    </h1>
    <p style="color: var(--text-secondary); font-size: 1.25rem; max-width: 600px; margin: 0 auto 2rem auto; font-family: var(--font);">
        Build custom AI chatbots powered by Llama 3, Mixtral & Gemma — completely free.
    </p>
</div>
""", unsafe_allow_html=True)

col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    if st.button("Create Your First Chatbot", type="primary", use_container_width=True):
        st.switch_page("pages/2_Builder.py")

st.markdown("<br><br>", unsafe_allow_html=True)

# Features Section
col_f1, col_f2, col_f3 = st.columns(3)

def feature_card(icon, title, desc):
    st.markdown(f"""
    <div style="background: var(--bg-surface); border: 1px solid var(--border); border-radius: var(--radius); padding: 1.5rem; text-align: center; height: 100%;">
        <div style="font-size: 2.5rem; margin-bottom: 1rem;">{icon}</div>
        <h3 style="color: var(--text-primary); font-size: 1.2rem; margin-bottom: 0.5rem;">{title}</h3>
        <p style="color: var(--text-secondary); font-size: 0.9rem;">{desc}</p>
    </div>
    """, unsafe_allow_html=True)

with col_f1:
    feature_card("🧠", "Multiple AI Models", "Choose between Llama 3, Mixtral, and Gemma models for different tasks and speeds.")
    
with col_f2:
    feature_card("🎭", "Custom Personality", "Define exact behaviors, system prompts, avatars, and greeting messages.")
    
with col_f3:
    feature_card("🚀", "Instant Deploy", "Save your configurations and instantly chat across your deployed web suite.")

st.markdown("""
<div style="text-align: center; margin-top: 4rem; padding-top: 2rem; border-top: 1px solid var(--border); color: var(--text-secondary); font-size: 0.9rem;">
    <p>Project: AI Chatbot Generator System</p>
    <p>Student: [Your Name] | Trainer: Faiza Ghaffar</p>
</div>
""", unsafe_allow_html=True)
