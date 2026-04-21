import streamlit as st
import streamlit.components.v1 as components
from components.sidebar import render_sidebar
from components.bot_card import render_bot_card
from utils.storage import load_chatbots

from components.styles import get_saas_css

st.set_page_config(page_title="Dashboard | AI Chatbot Generator", page_icon="📊", layout="wide")
st.markdown(get_saas_css(), unsafe_allow_html=True)
render_sidebar()

col1, col2 = st.columns([1, 1])
with col1:
    st.markdown('<h2 style="color: var(--text-primary); font-family: var(--font);">Your Chatbots</h2>', unsafe_allow_html=True)
with col2:
    st.markdown("<div style='text-align:right'>", unsafe_allow_html=True)
    if st.button("➕ New Chatbot", type="primary"):
        st.session_state["selected_bot_id"] = None
        st.switch_page("pages/2_Builder.py")
    st.markdown("</div>", unsafe_allow_html=True)

bots = load_chatbots()

if not bots:
    st.markdown("""
    <div style="text-align: center; padding: 4rem 2rem; background: var(--bg-surface); border-radius: var(--radius); border: 1px dashed var(--border); margin-top: 2rem;">
        <h3 style="color: var(--text-secondary); margin-bottom: 1rem;">No chatbots yet</h3>
    </div>
    """, unsafe_allow_html=True)
    col_c1, col_c2, col_c3 = st.columns([1, 1, 1])
    with col_c2:
        if st.button("Create your first chatbot", use_container_width=True):
            st.switch_page("pages/2_Builder.py")
else:
    # Display in a grid
    cols_per_row = 3
    for i in range(0, len(bots), cols_per_row):
        cols = st.columns(cols_per_row)
        for j, bot in enumerate(bots[i:i+cols_per_row]):
            with cols[j]:
                html_code = render_bot_card(bot)
                components.html(html_code, height=170)
                
                # Render native Streamlit buttons underneath
                b1, b2, b3 = st.columns([2, 2, 1])
                with b1:
                    if st.button("Chat", key=f"chat_{bot['id']}", use_container_width=True, type="primary"):
                        st.session_state["selected_bot_id"] = bot["id"]
                        st.switch_page("pages/3_Chat.py")
                with b2:
                    if st.button("Edit", key=f"edit_{bot['id']}", use_container_width=True):
                        st.session_state["selected_bot_id"] = bot["id"]
                        st.switch_page("pages/2_Builder.py")
                with b3:
                    if st.button("🗑️", key=f"delete_{bot['id']}", use_container_width=True, help="Delete Chatbot"):
                        from utils.storage import delete_chatbot
                        delete_chatbot(bot['id'])
                        st.rerun()
                
                st.markdown("<br>", unsafe_allow_html=True)
