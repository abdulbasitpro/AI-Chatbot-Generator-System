import streamlit as st
import time
from components.sidebar import render_sidebar
from components.chat_ui import render_chat_preview
from utils.storage import save_chatbot, load_chatbots
from utils.groq_client import get_available_models

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
    --radius: 12px;
    --font: 'Inter', sans-serif;
}
.stApp { background: var(--bg-primary) !important; color: var(--text-primary) !important; }
.stAppHeader { background: transparent !important; }
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
</style>
"""

st.set_page_config(page_title="Builder | AI Chatbot Generator", page_icon="🛠️", layout="wide")
st.markdown(get_design_system_css(), unsafe_allow_html=True)
render_sidebar()

st.markdown('<h2 style="color: var(--text-primary); font-family: var(--font);">🛠️ Bot Builder</h2>', unsafe_allow_html=True)

# Load existing bot if edit
bot_id = st.session_state.get("selected_bot_id") or st.query_params.get("bot_id", None)
existing_bot = {}
if bot_id:
    for b in load_chatbots():
        if b.get("id") == bot_id:
            existing_bot = b
            break

col_form, col_preview = st.columns([1, 1])

with col_form:
    with st.container():
        st.markdown("### Configuration")
        bot_name = st.text_input("Bot Name", value=existing_bot.get("name", "Support Bot"))
        bot_avatar = st.text_input("Bot Avatar Emoji", value=existing_bot.get("avatar", "🤖"))
        
        system_prompt = st.text_area("System Prompt / Personality", 
            value=existing_bot.get("system_prompt", "You are a friendly customer support assistant for a tech company. Always be helpful and concise."),
            height=150)
            
        models = get_available_models()
        model_keys = list(models.keys())
        default_model_index = model_keys.index(existing_bot.get("model", "llama-3.1-8b-instant")) if existing_bot.get("model") in model_keys else 0
        
        selected_model_key = st.selectbox("AI Model", options=model_keys, index=default_model_index, format_func=lambda x: models[x])
        
        temperature = st.slider("Temperature", 0.0, 1.0, float(existing_bot.get("temperature", 0.7)))
        max_tokens = st.slider("Max tokens", 100, 2000, int(existing_bot.get("max_tokens", 500)))
        
        greeting = st.text_input("Greeting Message", value=existing_bot.get("greeting", "Hello! How can I help you today?"))
        is_public = st.toggle("Is Public", value=existing_bot.get("is_public", False))
        
        if st.button("Save Chatbot", type="primary"):
            config = {
                "id": bot_id if bot_id else "",
                "name": bot_name,
                "avatar": bot_avatar,
                "system_prompt": system_prompt,
                "model": selected_model_key,
                "temperature": temperature,
                "max_tokens": max_tokens,
                "greeting": greeting,
                "is_public": is_public
            }
            new_id = save_chatbot(config)
            st.success(f"Chatbot '{bot_name}' saved successfully!")
            time.sleep(1)
            st.switch_page("pages/1_Dashboard.py")

with col_preview:
    st.markdown(render_chat_preview(bot_avatar, greeting), unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)
    if st.button("Test Chat (Unsaved)", use_container_width=True):
        st.info("To chat with this bot, save it first and click 'Chat' from the dashboard.")
