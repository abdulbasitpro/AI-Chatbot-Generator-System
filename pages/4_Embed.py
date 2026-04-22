"""
Public embed page — no authentication required for public bots.
URL: http://localhost:8503/Embed?bot_id=<id>
"""
import streamlit as st
import time
from utils.storage import load_chatbots
from utils.auth import get_user_api_key
from utils.groq_client import stream_chat_response, get_available_models
from components.styles import get_saas_css

st.set_page_config(
    page_title="Chat",
    page_icon="💬",
    layout="centered",
    initial_sidebar_state="collapsed",
)

st.markdown(get_saas_css(), unsafe_allow_html=True)
st.markdown("""
<style>
[data-testid="stSidebar"]        { display: none !important; }
[data-testid="collapsedControl"] { display: none !important; }
[data-testid="stHeader"]         { display: none !important; }
footer                           { display: none !important; }
.block-container { padding-top: 0.8rem !important; max-width: 780px !important; }

/* Delete message button — always visible red button */
.del-msg-btn {
    display: flex;
    align-items: center;
    justify-content: center;
    padding-top: 0.6rem;
}
.del-msg-btn button {
    background: rgba(239,68,68,0.15) !important;
    border: 1px solid rgba(239,68,68,0.4) !important;
    color: #F87171 !important;
    font-size: 0.8rem !important;
    font-weight: 700 !important;
    padding: 0.2rem 0.5rem !important;
    min-height: unset !important;
    height: 1.8rem !important;
    border-radius: 6px !important;
    line-height: 1 !important;
    transition: all 0.15s ease !important;
    width: 100% !important;
}
.del-msg-btn button:hover {
    background: rgba(239,68,68,0.35) !important;
    border-color: #EF4444 !important;
    color: #FCA5A5 !important;
    transform: scale(1.05) !important;
}
</style>
""", unsafe_allow_html=True)

# ── Resolve bot ────────────────────────────────────────────────────────────────
bot_id = st.query_params.get("bot_id", None)
if not bot_id:
    st.error("No bot specified. Add ?bot_id=YOUR_BOT_ID to the URL.")
    st.stop()

bots = load_chatbots()
bot  = next((b for b in bots if b.get("id") == bot_id), None)

if not bot:
    st.error("Bot not found. It may have been deleted.")
    st.stop()

if not bot.get("is_public", False):
    st.markdown("""
<div style="text-align:center; padding:4rem 2rem;">
    <div style="font-size:3rem; margin-bottom:1rem;">🔒</div>
    <h2 style="color:#F8FAFC;">This chatbot is private</h2>
    <p style="color:#64748B;">The owner has not made this bot public.</p>
</div>
""", unsafe_allow_html=True)
    st.stop()

owner_id = bot.get("owner_id")
api_key  = get_user_api_key(owner_id) if owner_id else None
if not api_key:
    st.error("This bot is not properly configured. The owner needs to add their API key.")
    st.stop()

# ── Session init ───────────────────────────────────────────────────────────────
session_key = f"embed_chat_{bot_id}"
if session_key not in st.session_state:
    st.session_state[session_key] = [{
        "role":    "assistant",
        "content": bot.get("greeting", "Hello! How can I help you today?"),
        "avatar":  bot.get("avatar", "🤖"),
    }]

# ── Header + Clear button ──────────────────────────────────────────────────────
hdr_col, clr_col = st.columns([4, 1])
with hdr_col:
    st.markdown(f"""
<div style="display:flex; align-items:center; gap:0.7rem; padding:0.5rem 0 0.8rem 0;
            border-bottom:1px solid rgba(255,255,255,0.06); margin-bottom:0.8rem;">
    <span style="font-size:1.8rem;">{bot.get('avatar','🤖')}</span>
    <div>
        <div style="font-size:1rem; font-weight:700; color:#F8FAFC;">{bot.get('name','Chatbot')}</div>
        <div style="font-size:0.68rem; color:#475569;">Powered by AI Chatbot Generator</div>
    </div>
</div>
""", unsafe_allow_html=True)
with clr_col:
    st.markdown("<div style='padding-top:0.4rem'></div>", unsafe_allow_html=True)
    if st.button("🧹 Clear", use_container_width=True, help="Clear all messages"):
        st.session_state[session_key] = [{
            "role":    "assistant",
            "content": bot.get("greeting", "Hello!"),
            "avatar":  bot.get("avatar", "🤖"),
        }]
        st.rerun()

# ── Render messages with per-message delete ────────────────────────────────────
msgs = st.session_state[session_key]
delete_idx = None

for idx, msg in enumerate(msgs):
    msg_col, del_col = st.columns([12, 1])
    with msg_col:
        with st.chat_message(msg["role"], avatar=msg.get("avatar")):
            st.markdown(msg["content"])
            if "meta" in msg:
                st.markdown(f'<div class="chat-meta">{msg["meta"]}</div>',
                            unsafe_allow_html=True)
    with del_col:
        # Don't allow deleting the very first greeting
        if idx > 0:
            st.markdown('<div class="del-msg-btn">', unsafe_allow_html=True)
            if st.button("✕", key=f"embed_del_{idx}", help="Delete this message"):
                delete_idx = idx
            st.markdown("</div>", unsafe_allow_html=True)

if delete_idx is not None:
    st.session_state[session_key].pop(delete_idx)
    st.rerun()

# ── Chat input ─────────────────────────────────────────────────────────────────
user_input = st.chat_input(f"Message {bot.get('name','the bot')}…")

if user_input:
    st.session_state[session_key].append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    with st.chat_message("assistant", avatar=bot.get("avatar", "🤖")):
        history = [
            {"role": m["role"], "content": m["content"]}
            for m in st.session_state[session_key]
        ]
        try:
            stream = stream_chat_response(
                messages=history[:-1],
                model=bot.get("model", "llama-3.1-8b-instant"),
                system_prompt=bot.get("system_prompt", ""),
                api_key=api_key,
                temperature=bot.get("temperature", 0.7),
                max_tokens=bot.get("max_tokens", 500),
            )
            start    = time.time()
            response = st.write_stream(stream)
            elapsed  = round(time.time() - start, 2)
            model_label = get_available_models().get(bot.get("model"), bot.get("model"))
            meta_html   = f"⚡ {elapsed}s · {model_label}"
            st.markdown(f'<div class="chat-meta">{meta_html}</div>', unsafe_allow_html=True)
            st.session_state[session_key].append({
                "role":    "assistant",
                "content": response,
                "avatar":  bot.get("avatar", "🤖"),
                "meta":    meta_html,
            })
        except Exception as e:
            st.error(f"Error: {str(e)[:200]}")
