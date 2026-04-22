import streamlit as st
import os
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

from components.styles import get_saas_css
from utils.auth import is_logged_in

st.set_page_config(
    page_title="AI Chatbot Generator SaaS",
    page_icon="✨",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Inject global SaaS CSS
st.markdown(get_saas_css(), unsafe_allow_html=True)

# ── Auth guard: must be logged in to see the landing page features ─────────────
if not is_logged_in(st.session_state):
    st.switch_page("pages/0_Auth.py")

from components.sidebar import render_sidebar
render_sidebar()

# Hero Section
st.markdown("""
<div style="text-align: center; padding: 6rem 2rem 4rem 2rem;">
    <div class="saas-badge">
        ✦ GENERATIVE AI PLATFORM
    </div>
    <h1 style="color: var(--text-primary); font-size: 4.5rem; font-weight: 800; margin-bottom: 1.5rem; line-height: 1.1;">
        Build Intelligent <br>
        <span class="saas-gradient-text">AI Chatbots</span> in Seconds
    </h1>
    <p style="color: var(--text-secondary); font-size: 1.25rem; max-width: 600px; margin: 0 auto 3rem auto; line-height: 1.6;">
        Deploy custom AI assistants powered by industry-leading models like Llama-3.1 and Gemma-2. Completely free. No coding required.
    </p>
</div>
""", unsafe_allow_html=True)

# Call to action
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    if st.button("Start Building For Free", type="primary", use_container_width=True):
        st.switch_page("pages/2_Builder.py")

st.markdown("<br><br><br>", unsafe_allow_html=True)

# Features Section
col_f1, col_f2, col_f3 = st.columns(3)

def saas_feature_card(icon, title, desc):
    return f"""
    <div class="saas-feature-card">
        <div class="feature-icon-wrapper">{icon}</div>
        <h3 style="color: var(--text-primary); font-size: 1.3rem; margin-bottom: 0.75rem;">{title}</h3>
        <p style="color: var(--text-secondary); font-size: 0.95rem; line-height: 1.5;">{desc}</p>
    </div>
    """

with col_f1:
    st.markdown(saas_feature_card(
        "🧠", 
        "State-of-the-art Models", 
        "Harness the power of the fastest open-source models available via the Groq accelerator."
    ), unsafe_allow_html=True)
    
with col_f2:
    st.markdown(saas_feature_card(
        "🎭", 
        "Persona Engine", 
        "Define strict behaviors, custom greeting messages, and hyper-specific instructions."
    ), unsafe_allow_html=True)
    
with col_f3:
    st.markdown(saas_feature_card(
        "🚀", 
        "One-Click Deploy", 
        "Save configurations and instantly deploy your personalized chatbots across your ecosystem."
    ), unsafe_allow_html=True)

# Footer
st.markdown("""
<div style="text-align: center; margin-top: 6rem; padding: 2rem 0; border-top: 1px solid var(--border); color: var(--text-secondary); font-size: 0.9rem;">
    <p>Project: AI Chatbot Generator System</p>
    <p>Student: Abdul Basit | Trainer: Faiza Ghaffar</p>
</div>
""", unsafe_allow_html=True)
