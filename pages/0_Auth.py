import streamlit as st
from utils.auth import register_user, login_user, set_session, is_logged_in
from components.styles import get_saas_css

st.set_page_config(
    page_title="Sign In | AI Chatbot Generator",
    page_icon="✨",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Inject CSS + hide sidebar completely on auth page
st.markdown(get_saas_css(), unsafe_allow_html=True)
st.markdown("""
<style>
/* Hide sidebar entirely on auth page */
[data-testid="stSidebar"]          { display: none !important; }
[data-testid="collapsedControl"]   { display: none !important; }
[data-testid="stSidebarNav"]       { display: none !important; }

/* Full-height centered layout */
.block-container {
    max-width: 420px !important;
    padding-top: 6vh !important;
    padding-bottom: 4rem !important;
}
</style>
""", unsafe_allow_html=True)

# Already logged in → go directly to dashboard
if is_logged_in(st.session_state):
    st.switch_page("pages/1_Dashboard.py")

# Toggle between login / register
if "auth_mode" not in st.session_state:
    st.session_state["auth_mode"] = "login"

mode = st.session_state["auth_mode"]

# ── BRAND LOGO ─────────────────────────────────────────────────────────────────
st.markdown("""
<div style="text-align:center; margin-bottom: 2rem;">
    <div style="font-size:2.8rem; margin-bottom:0.5rem;">✦</div>
    <div style="font-size:1.05rem; font-weight:800; color:#6366F1;
                letter-spacing:2px; text-transform:uppercase;">
        AI Chatbot Generator
    </div>
</div>
""", unsafe_allow_html=True)

# ══════════════════════════════════════════════════════
#  SIGN IN
# ══════════════════════════════════════════════════════
if mode == "login":
    st.markdown("""
<div style="background:linear-gradient(145deg,rgba(30,36,51,0.9),rgba(17,24,39,0.95));
            border:1px solid rgba(255,255,255,0.08); border-radius:20px;
            padding:2.2rem 2rem; box-shadow:0 24px 64px rgba(0,0,0,0.4),
            0 0 0 1px rgba(99,102,241,0.07);">
""", unsafe_allow_html=True)

    st.markdown("""
<h2 style="margin:0 0 0.25rem 0; font-size:1.5rem; font-weight:700;
           color:#F8FAFC; font-family:'Outfit',sans-serif;">Sign in</h2>
<p style="color:#64748B; font-size:0.88rem; margin:0 0 1.5rem 0;">
    to continue to AI Chatbot Generator
</p>
""", unsafe_allow_html=True)

    with st.form("login_form"):
        email    = st.text_input("Email address", placeholder="you@example.com")
        password = st.text_input("Password",      placeholder="••••••••", type="password")
        st.markdown("<div style='height:0.2rem'></div>", unsafe_allow_html=True)
        submitted = st.form_submit_button("Sign in →", use_container_width=True, type="primary")

    if submitted:
        if not email or not password:
            st.error("Please enter your email and password.")
        else:
            result = login_user(email, password)
            if result["ok"]:
                set_session(st.session_state, result["user"])
                st.switch_page("pages/1_Dashboard.py")
            else:
                st.error(result["error"])

    st.markdown("</div>", unsafe_allow_html=True)

    # Switch to register
    st.markdown("<div style='height:1rem'></div>", unsafe_allow_html=True)
    st.markdown("""
<div style="text-align:center; background:rgba(255,255,255,0.03);
            border:1px solid rgba(255,255,255,0.07); border-radius:12px;
            padding:1rem; font-size:0.9rem; color:#94A3B8;">
    New here?
</div>
""", unsafe_allow_html=True)
    if st.button("Create an account →", use_container_width=True):
        st.session_state["auth_mode"] = "register"
        st.rerun()

# ══════════════════════════════════════════════════════
#  REGISTER
# ══════════════════════════════════════════════════════
else:
    st.markdown("""
<div style="background:linear-gradient(145deg,rgba(30,36,51,0.9),rgba(17,24,39,0.95));
            border:1px solid rgba(255,255,255,0.08); border-radius:20px;
            padding:2.2rem 2rem; box-shadow:0 24px 64px rgba(0,0,0,0.4),
            0 0 0 1px rgba(99,102,241,0.07);">
""", unsafe_allow_html=True)

    st.markdown("""
<h2 style="margin:0 0 0.25rem 0; font-size:1.5rem; font-weight:700;
           color:#F8FAFC; font-family:'Outfit',sans-serif;">Create your account</h2>
<p style="color:#64748B; font-size:0.88rem; margin:0 0 1.5rem 0;">
    Free forever. No credit card required.
</p>
""", unsafe_allow_html=True)

    with st.form("register_form"):
        name     = st.text_input("Full name",         placeholder="Abdul Basit")
        email    = st.text_input("Email address",     placeholder="you@example.com")
        password = st.text_input("Password",          placeholder="At least 6 characters", type="password")
        confirm  = st.text_input("Confirm password",  placeholder="Repeat your password",  type="password")
        st.markdown("<div style='height:0.2rem'></div>", unsafe_allow_html=True)
        submitted_r = st.form_submit_button("Create account →", use_container_width=True, type="primary")

    if submitted_r:
        if password != confirm:
            st.error("Passwords do not match.")
        else:
            result = register_user(name, email, password)
            if result["ok"]:
                set_session(st.session_state, result["user"])
                st.success(f"Welcome, {result['user']['name']}! 🎉")
                st.switch_page("pages/1_Dashboard.py")
            else:
                st.error(result["error"])

    st.markdown("</div>", unsafe_allow_html=True)

    # Switch back to login
    st.markdown("<div style='height:1rem'></div>", unsafe_allow_html=True)
    st.markdown("""
<div style="text-align:center; background:rgba(255,255,255,0.03);
            border:1px solid rgba(255,255,255,0.07); border-radius:12px;
            padding:1rem; font-size:0.9rem; color:#94A3B8;">
    Already have an account?
</div>
""", unsafe_allow_html=True)
    if st.button("Sign in instead →", use_container_width=True):
        st.session_state["auth_mode"] = "login"
        st.rerun()
