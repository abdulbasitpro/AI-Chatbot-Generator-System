import streamlit as st
from utils.auth import get_current_user, logout, is_logged_in, get_user_api_key

def render_sidebar():
    # ── Branding ───────────────────────────────────────────────────────────────
    st.sidebar.markdown("""
<div style="padding:0.5rem 0 1.2rem 0;">
    <div style="font-size:0.75rem; font-weight:800; color:#6366F1;
                letter-spacing:1.5px; text-transform:uppercase; margin-bottom:0.35rem;">
        ✦ AI Chatbot Generator
    </div>
    <div style="font-size:0.82rem; color:#64748B; line-height:1.5;">
        Build &amp; deploy AI chatbots powered by<br>
        <b style="color:#94A3B8;">Llama 3.1</b> &amp; <b style="color:#94A3B8;">Gemma 2</b> via Groq.
    </div>
</div>
""", unsafe_allow_html=True)

    # ── Only show user info if logged in ───────────────────────────────────────
    if not is_logged_in(st.session_state):
        return

    user    = get_current_user(st.session_state)
    user_id = user["id"]
    api_key = get_user_api_key(user_id)

    # ── API Key status pill ────────────────────────────────────────────────────
    if api_key:
        masked = api_key[:8] + "••••••••••••" + api_key[-4:]
        st.sidebar.markdown(f"""
<div style="background:rgba(16,185,129,0.08); border:1px solid rgba(16,185,129,0.25);
            border-radius:10px; padding:0.7rem 0.9rem; margin-bottom:1rem;">
    <div style="display:flex; align-items:center; gap:6px; margin-bottom:0.2rem;">
        <div style="width:7px; height:7px; border-radius:50%; background:#10B981;
                    box-shadow:0 0 6px #10B981;"></div>
        <span style="font-size:0.72rem; font-weight:700; color:#10B981;
                     text-transform:uppercase; letter-spacing:0.8px;">Groq API Connected</span>
    </div>
    <div style="font-size:0.7rem; color:#475569; font-family:monospace;">{masked}</div>
</div>
""", unsafe_allow_html=True)
    else:
        st.sidebar.markdown("""
<div style="background:rgba(239,68,68,0.08); border:1px solid rgba(239,68,68,0.3);
            border-radius:10px; padding:0.7rem 0.9rem; margin-bottom:1rem;">
    <div style="display:flex; align-items:center; gap:6px;">
        <div style="width:7px; height:7px; border-radius:50%; background:#EF4444;"></div>
        <span style="font-size:0.72rem; font-weight:700; color:#EF4444;
                     text-transform:uppercase; letter-spacing:0.8px;">No API Key</span>
    </div>
    <div style="font-size:0.72rem; color:#94A3B8; margin-top:0.2rem;">
        Add your Groq key in the Builder.
    </div>
</div>
""", unsafe_allow_html=True)

    # ── User account card ──────────────────────────────────────────────────────
    initials = "".join(w[0].upper() for w in user.get("name", "U").split()[:2])
    st.sidebar.markdown(f"""
<div style="background:linear-gradient(135deg,rgba(99,102,241,0.1),rgba(168,85,247,0.1));
            border:1px solid rgba(99,102,241,0.2); border-radius:12px;
            padding:0.85rem 1rem; margin-bottom:0.6rem;">
    <div style="display:flex; align-items:center; gap:0.7rem;">
        <div style="width:36px; height:36px; border-radius:50%;
                    background:linear-gradient(135deg,#6366F1,#A855F7);
                    display:flex; align-items:center; justify-content:center;
                    font-size:0.85rem; font-weight:700; color:white; flex-shrink:0;">
            {initials}
        </div>
        <div style="overflow:hidden;">
            <div style="font-size:0.88rem; font-weight:600; color:#F8FAFC;
                        white-space:nowrap; overflow:hidden; text-overflow:ellipsis;">
                {user.get("name", "User")}
            </div>
            <div style="font-size:0.7rem; color:#64748B;
                        white-space:nowrap; overflow:hidden; text-overflow:ellipsis;">
                {user.get("email", "")}
            </div>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

    if st.sidebar.button("🚪 Sign Out", use_container_width=True, key="sidebar_logout"):
        logout(st.session_state)
        st.switch_page("pages/0_Auth.py")
