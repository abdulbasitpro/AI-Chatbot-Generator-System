import streamlit as st
import time
from components.sidebar import render_sidebar
from components.chat_ui import render_chat_preview
from utils.storage import save_chatbot, load_chatbots
from utils.groq_client import get_available_models, validate_api_key
from utils.auth import is_logged_in, get_current_user, save_user_api_key, get_user_api_key
from components.styles import get_saas_css

st.set_page_config(page_title="Builder | AI Chatbot Generator", page_icon="🛠️", layout="wide")
st.markdown(get_saas_css(), unsafe_allow_html=True)

if not is_logged_in(st.session_state):
    st.switch_page("pages/0_Auth.py")

render_sidebar()

user = get_current_user(st.session_state)
user_id = user["id"]

st.markdown('<h2 style="color:var(--text-primary);font-family:var(--font);">🛠️ Bot Builder</h2>', unsafe_allow_html=True)

# ── Load existing bot if editing ───────────────────────────────────────────────
bot_id = st.session_state.get("selected_bot_id") or st.query_params.get("bot_id", None)
existing_bot = {}
if bot_id:
    for b in load_chatbots():
        if b.get("id") == bot_id:
            existing_bot = b
            break

# ══════════════════════════════════════════════════════════════════════════════
#  SECTION 1 — Groq API Key (required before building)
# ══════════════════════════════════════════════════════════════════════════════
stored_key = get_user_api_key(user_id) or ""

st.markdown("""
<div style="background:linear-gradient(135deg,rgba(99,102,241,0.08),rgba(168,85,247,0.08));
            border:1px solid rgba(99,102,241,0.25); border-radius:16px;
            padding:1.4rem 1.6rem; margin-bottom:1.5rem;">
    <div style="display:flex; align-items:center; gap:0.6rem; margin-bottom:0.8rem;">
        <span style="font-size:1.2rem;">🔑</span>
        <span style="font-size:1rem; font-weight:700; color:#F8FAFC;">Your Groq API Key</span>
        <span style="font-size:0.72rem; background:rgba(99,102,241,0.2); color:#A5B4FC;
                     padding:0.15rem 0.5rem; border-radius:6px; font-weight:600;">Required</span>
    </div>
    <p style="color:#94A3B8; font-size:0.85rem; margin:0 0 0.5rem 0; line-height:1.6;">
        Each user provides their own free API key from Groq.
        Your key is saved to your account and never shared.
    </p>
    <a href="https://console.groq.com/keys" target="_blank"
       style="color:#818CF8; font-size:0.82rem; font-weight:600; text-decoration:none;">
        🔗 Get your free API key at console.groq.com/keys →
    </a>
</div>
""", unsafe_allow_html=True)

key_col, btn_col = st.columns([5, 1])
with key_col:
    api_key_input = st.text_input(
        "Groq API Key",
        value=stored_key,
        placeholder="gsk_••••••••••••••••••••••••••••••••••••••••",
        type="password",
        label_visibility="collapsed",
        help="Starts with 'gsk_'. Get it free at console.groq.com/keys"
    )
with btn_col:
    verify_clicked = st.button("✓ Save Key", use_container_width=True, type="primary")

if verify_clicked:
    if not api_key_input:
        st.error("Please paste your Groq API key first.")
    else:
        with st.spinner("Verifying key with Groq…"):
            result = validate_api_key(api_key_input)
        if result["ok"]:
            save_user_api_key(user_id, api_key_input)
            # Refresh session user object so sidebar shows updated status
            st.session_state["auth_user"]["groq_api_key"] = api_key_input
            stored_key = api_key_input
            st.success("✅ API key verified and saved to your account!")
        else:
            st.error(f"❌ {result['error']}")

# Block builder if no valid key is stored
if not stored_key:
    st.warning("⚠️ Please enter and save your Groq API key above before building a chatbot.")
    st.stop()

# ══════════════════════════════════════════════════════════════════════════════
#  SECTION 2 — Bot Configuration
# ══════════════════════════════════════════════════════════════════════════════
col_form, col_preview = st.columns([1, 1])

with col_form:
    st.markdown("### ⚙️ Configuration")

    bot_name   = st.text_input("Bot Name",         value=existing_bot.get("name",   "Support Bot"))
    bot_avatar = st.text_input("Bot Avatar Emoji", value=existing_bot.get("avatar", "🤖"),
                               help="Paste any single emoji")

    system_prompt = st.text_area(
        "System Prompt / Personality",
        value=existing_bot.get("system_prompt",
              "You are a friendly customer support assistant. Always be helpful and concise."),
        height=140,
        help="This is the hidden instruction that defines how your bot behaves."
    )

    models = get_available_models()
    model_keys = list(models.keys())
    default_idx = model_keys.index(existing_bot.get("model", "llama-3.1-8b-instant")) \
                  if existing_bot.get("model") in model_keys else 0

    selected_model = st.selectbox("AI Model", options=model_keys,
                                  index=default_idx, format_func=lambda x: models[x])

    c1, c2 = st.columns(2)
    with c1:
        temperature = st.slider("Temperature",
                                0.0, 1.0, float(existing_bot.get("temperature", 0.7)),
                                help="Higher = more creative. Lower = more focused.")
    with c2:
        max_tokens = st.slider("Max Tokens",
                               100, 2000, int(existing_bot.get("max_tokens", 500)),
                               help="Maximum length of each reply.")

    greeting  = st.text_input("Greeting Message",
                              value=existing_bot.get("greeting", "Hello! How can I help you today?"))
    is_public = st.toggle("Make Public", value=existing_bot.get("is_public", False),
                          help="Public bots can be embedded on any website via the embed code.")

    st.markdown("<div style='height:0.5rem'></div>", unsafe_allow_html=True)

    if st.button("💾 Save Chatbot", type="primary", use_container_width=True):
        if not bot_name.strip():
            st.error("Bot name cannot be empty.")
        else:
            config = {
                "id":            bot_id if bot_id else "",
                "owner_id":      user_id,          # link bot to its owner
                "name":          bot_name.strip(),
                "avatar":        bot_avatar,
                "system_prompt": system_prompt,
                "model":         selected_model,
                "temperature":   temperature,
                "max_tokens":    max_tokens,
                "greeting":      greeting,
                "is_public":     is_public,
            }
            save_chatbot(config)
            st.success(f"✅ '{bot_name}' saved!")
            time.sleep(0.8)
            st.switch_page("pages/1_Dashboard.py")

with col_preview:
    st.markdown("### 👁️ Preview")
    st.markdown(render_chat_preview(bot_avatar, greeting), unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)
    st.info("💡 Save the bot first, then use **Chat** on the Dashboard to test it with your real API key.")
