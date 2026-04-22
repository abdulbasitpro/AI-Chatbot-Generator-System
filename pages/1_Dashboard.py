import streamlit as st
from components.sidebar import render_sidebar
from components.bot_card import render_bot_card
from utils.storage import load_chatbots
from utils.auth import is_logged_in
from components.styles import get_saas_css

st.set_page_config(page_title="Dashboard | AI Chatbot Generator", page_icon="📊", layout="wide")
st.markdown(get_saas_css(), unsafe_allow_html=True)

if not is_logged_in(st.session_state):
    st.switch_page("pages/0_Auth.py")

render_sidebar()

# ── Header row ────────────────────────────────────────────────────────────────
hdr, new_btn_col = st.columns([3, 1])
with hdr:
    st.markdown('<h2 class="dash-title">Your Chatbots</h2>', unsafe_allow_html=True)
with new_btn_col:
    if st.button("➕ New Chatbot", type="primary", use_container_width=True):
        st.session_state["selected_bot_id"] = None
        st.switch_page("pages/2_Builder.py")

bots = load_chatbots()

if not bots:
    st.markdown("""
    <div class="empty-state">
        <div class="empty-icon">🤖</div>
        <h3>No chatbots yet</h3>
        <p>Create your first AI-powered chatbot in minutes.</p>
    </div>
    """, unsafe_allow_html=True)
    _, mid, _ = st.columns([1, 1, 1])
    with mid:
        if st.button("Create your first chatbot", use_container_width=True, type="primary"):
            st.switch_page("pages/2_Builder.py")
else:
    cols_per_row = 3
    for i in range(0, len(bots), cols_per_row):
        row_bots = bots[i:i + cols_per_row]
        cols = st.columns(cols_per_row)   # always 3 equal columns
        for j in range(cols_per_row):
            with cols[j]:
                if j < len(row_bots):
                    bot = row_bots[j]

                    # ── Card ─────────────────────────────────────────────────
                    st.markdown(render_bot_card(bot), unsafe_allow_html=True)

                    # ── Button row 1: Chat | Edit ────────────────────────────
                    b_chat, b_edit = st.columns(2)
                    with b_chat:
                        if st.button("💬 Chat", key=f"chat_{bot['id']}",
                                     use_container_width=True, type="primary"):
                            st.session_state["selected_bot_id"] = bot["id"]
                            st.switch_page("pages/3_Chat.py")
                    with b_edit:
                        if st.button("✏️ Edit", key=f"edit_{bot['id']}",
                                     use_container_width=True):
                            st.session_state["selected_bot_id"] = bot["id"]
                            st.switch_page("pages/2_Builder.py")

                    # ── Button row 2: Deploy | Delete ────────────────────────
                    b_deploy, b_del = st.columns([3, 1])
                    with b_deploy:
                        deploy_key = f"show_deploy_{bot['id']}"
                        if st.button("🚀 Deploy", key=f"deploy_{bot['id']}",
                                     use_container_width=True):
                            st.session_state[deploy_key] = not st.session_state.get(deploy_key, False)
                    with b_del:
                        if st.button("Del", key=f"delete_{bot['id']}",
                                     use_container_width=True, help="Delete this chatbot"):
                            from utils.storage import delete_chatbot
                            delete_chatbot(bot["id"])
                            st.rerun()

                    # ── Deploy embed panel ────────────────────────────────────
                    if st.session_state.get(f"show_deploy_{bot['id']}", False):
                        bid       = bot["id"]
                        is_public = bot.get("is_public", False)
                        # Streamlit strips numeric prefix: pages/4_Embed.py → /Embed
                        base_url  = "http://localhost:8503"
                        chat_url  = f"{base_url}/Embed?bot_id={bid}"
                        iframe_tag = f'<iframe src="{chat_url}" width="100%" height="600" frameborder="0" style="border-radius:12px;"></iframe>'

                        if not is_public:
                            st.warning(
                                "⚠️ This bot is **Private**. Go to **Edit** → "
                                "turn on **Make Public** → Save — then the embed link will work."
                            )
                        else:
                            # Use st.code() so HTML is shown as text, NOT rendered
                            st.markdown("""
<div style="background:rgba(17,24,39,0.9); border:1px solid rgba(99,102,241,0.3);
            border-radius:12px; padding:1rem 1.2rem; margin-top:0.3rem;">
    <div style="font-size:0.72rem; color:#94A3B8; font-weight:700;
                text-transform:uppercase; letter-spacing:1px; margin-bottom:0.4rem;">
        🔗 Direct Chat Link
    </div>
""", unsafe_allow_html=True)
                            st.code(chat_url, language=None)
                            st.markdown("""
    <div style="font-size:0.72rem; color:#475569; margin:-0.5rem 0 0.8rem 0;">
        Open this link in any browser to chat with your bot.
    </div>
    <div style="font-size:0.72rem; color:#94A3B8; font-weight:700;
                text-transform:uppercase; letter-spacing:1px; margin-bottom:0.4rem;">
        🌐 Embed on Any Website
    </div>
""", unsafe_allow_html=True)
                            st.code(iframe_tag, language="html")
                            st.markdown("""
    <div style="font-size:0.72rem; color:#475569; margin-top:-0.5rem;">
        Paste into any webpage HTML.
        Replace <b style="color:#94A3B8;">localhost:8502</b> with your
        deployed URL after publishing to
        <a href="https://streamlit.io/cloud" target="_blank"
           style="color:#818CF8;">Streamlit Cloud</a>.
    </div>
</div>
""", unsafe_allow_html=True)

                    st.markdown("<div style='margin-bottom:1.5rem'></div>", unsafe_allow_html=True)
