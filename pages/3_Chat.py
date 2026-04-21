import streamlit as st
import time
from components.sidebar import render_sidebar
from utils.storage import load_chatbots
from utils.groq_client import stream_chat_response, get_available_models

from components.styles import get_saas_css

st.set_page_config(page_title="Chat | AI Chatbot Generator", page_icon="💬", layout="wide")
st.markdown(get_saas_css(), unsafe_allow_html=True)
render_sidebar()

bot_id = st.session_state.get("selected_bot_id") or st.query_params.get("bot_id", None)
bots = load_chatbots()
bot = next((b for b in bots if b.get("id") == bot_id), None)

if not bot:
    st.warning("Chatbot not found or no bot selected. Please select a bot from the Dashboard.")
    if st.button("Go to Dashboard", type="primary"):
        st.switch_page("pages/1_Dashboard.py")
    st.stop()

# Set up session state for chat
session_key = f"chat_messages_{bot['id']}"
if session_key not in st.session_state:
    st.session_state[session_key] = [{"role": "assistant", "content": bot.get("greeting", "Hello!"), "avatar": bot.get("avatar", "🤖")}]

if st.sidebar.button("Clear Chat History", use_container_width=True):
    st.session_state[session_key] = [{"role": "assistant", "content": bot.get("greeting", "Hello!"), "avatar": bot.get("avatar", "🤖")}]
    st.rerun()

st.markdown(f"<h2>{bot.get('avatar', '🤖')} {bot.get('name', 'Chat')}</h2>", unsafe_allow_html=True)

# Render existing messages
for msg in st.session_state[session_key]:
    with st.chat_message(msg["role"], avatar=msg.get("avatar")):
        st.markdown(msg["content"])
        if "meta" in msg:
            st.markdown(f'<div class="chat-meta">{msg["meta"]}</div>', unsafe_allow_html=True)
        # copy button is natively supported in st.chat_message since Streamlit 1.34+ context menu, or we could add custom html, but st native is fine

user_input = st.chat_input("Type your message...")

if user_input:
    # 1. Output user message
    st.session_state[session_key].append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    # 2. Output assistant message with streaming
    with st.chat_message("assistant", avatar=bot.get("avatar", "🤖")):
        with st.spinner("Thinking..."):
            history = [{"role": m["role"], "content": m["content"]} for m in st.session_state[session_key]]
            
            try:
                # Need to run via write_stream
                stream = stream_chat_response(
                    messages=history[:-1], # Don't send the user_input again if we already appended it... wait, we APPENDED it, so history includes it. Fine.
                    model=bot.get("model", "llama-3.1-8b-instant"),
                    system_prompt=bot.get("system_prompt", ""),
                    temperature=bot.get("temperature", 0.7),
                    max_tokens=bot.get("max_tokens", 500)
                )
                
                # We need to wrap it to yield chunks and capture total time if we want,
                # but groq_client yields strings AND returns time at the very end... wait! Python `yield` generator doesn't 'return' a value through typical iteration easily. 
                # Let's just time it here.
                
                start = time.time()
                response = st.write_stream(stream)
                elapsed = round(time.time() - start, 2)
                
                model_name = get_available_models().get(bot.get('model'), bot.get('model'))
                meta_html = f"⚡ {elapsed}s • {model_name}"
                st.markdown(f'<div class="chat-meta">{meta_html}</div>', unsafe_allow_html=True)
                
                st.session_state[session_key].append({
                    "role": "assistant",
                    "content": response,
                    "avatar": bot.get("avatar", "🤖"),
                    "meta": meta_html
                })
            except Exception as e:
                st.error(f"Error communicating with AI: {str(e)}")
