def get_saas_css():
    return """
<style>
/* Advanced SaaS Theme matching Modern Aesthetics */
@import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;500;600;700&display=swap');

:root {
    --bg-base: #060913;
    --bg-surface: rgba(30, 36, 51, 0.6);
    --bg-card: rgba(17, 24, 39, 0.6);
    --accent-gradient: linear-gradient(135deg, #6366F1 0%, #A855F7 100%);
    --accent: #6366F1;
    --accent-hover: #4F46E5;
    --text-primary: #F8FAFC;
    --text-secondary: #94A3B8;
    --border: rgba(255, 255, 255, 0.08);
    --radius-lg: 16px;
    --radius-md: 12px;
    --shadow-glow: 0 0 20px rgba(99, 102, 241, 0.15);
    --font: 'Outfit', sans-serif;
}

/* Base Body Modifications */
.stApp {
    background-color: var(--bg-base) !important;
    background-image: 
        radial-gradient(circle at 15% 50%, rgba(99, 102, 241, 0.08), transparent 25%),
        radial-gradient(circle at 85% 30%, rgba(168, 85, 247, 0.08), transparent 25%) !important;
    color: var(--text-primary) !important;
    font-family: var(--font) !important;
}

h1, h2, h3, h4, h5, h6 {
    font-family: var(--font) !important;
}

/* Hide only Streamlit footer — leave header & sidebar toggle UNTOUCHED */
footer { visibility: hidden !important; }


.block-container {
    padding-top: 3.5rem !important;  /* space for Streamlit deploy toolbar */
    max-width: 1200px !important;
}



/* Button Upgrades */
button[kind="primary"] {
    background: var(--accent-gradient) !important;
    border: 1px solid rgba(255, 255, 255, 0.1) !important;
    border-radius: var(--radius-md) !important;
    color: white !important;
    font-weight: 600 !important;
    padding: 0.5rem 1.5rem !important;
    transition: all 0.3s ease !important;
    box-shadow: 0 4px 15px rgba(99, 102, 241, 0.2) !important;
}
button[kind="primary"]:hover {
    transform: translateY(-2px) !important;
    box-shadow: 0 6px 20px rgba(99, 102, 241, 0.4) !important;
}

/* Input Fields Glassmorphism */
.stTextInput input, .stTextArea textarea, .stSelectbox > div > div {
    background: var(--bg-card) !important;
    border: 1px solid var(--border) !important;
    color: var(--text-primary) !important;
    border-radius: var(--radius-md) !important;
    backdrop-filter: blur(10px);
    transition: border-color 0.3s ease, box-shadow 0.3s ease;
    font-family: var(--font) !important;
}
.stTextInput input:focus, .stTextArea textarea:focus {
    border-color: var(--accent) !important;
    box-shadow: 0 0 0 2px rgba(99, 102, 241, 0.2) !important;
}

/* Chat Messages */
.stChatMessage {
    background: var(--bg-surface) !important;
    border: 1px solid var(--border) !important;
    border-radius: var(--radius-lg) !important;
    padding: 1rem !important;
    backdrop-filter: blur(10px);
    box-shadow: var(--shadow-glow);
}

/* Feature Cards from App.py */
.saas-feature-card {
    background: var(--bg-surface);
    border: 1px solid var(--border);
    border-radius: var(--radius-lg);
    padding: 2rem;
    text-align: center;
    height: 300px;               /* fixed height — all cards identical */
    box-sizing: border-box;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: flex-start;
    overflow: hidden;
    backdrop-filter: blur(10px);
    box-shadow: 0 8px 32px rgba(0, 0, 0, 0.2);
    transition: transform 0.3s ease, box-shadow 0.3s ease, border-color 0.3s ease;
}

.saas-feature-card:hover {
    transform: translateY(-5px);
    box-shadow: var(--shadow-glow);
    border-color: rgba(99, 102, 241, 0.4);
}

.feature-icon-wrapper {
    background: rgba(255,255,255,0.05);
    width: 60px;
    height: 60px;
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    margin: 0 auto 1.5rem auto;
    font-size: 1.8rem;
    box-shadow: inset 0 0 10px rgba(255,255,255,0.05);
    border: 1px solid rgba(255,255,255,0.1);
}

/* Custom CSS Classes */
.saas-badge {
    background: rgba(99, 102, 241, 0.1);
    border: 1px solid rgba(99, 102, 241, 0.3);
    color: #818CF8;
    padding: 0.5rem 1.25rem;
    border-radius: 20px;
    font-size: 0.85rem;
    font-weight: 600;
    display: inline-block;
    margin-bottom: 2rem;
    letter-spacing: 0.5px;
    animation: pulseGlow 2.5s infinite alternate;
}

.saas-gradient-text {
    background: var(--accent-gradient);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    display: inline-block;
    font-weight: 800;
}

@keyframes pulseGlow {
    0% { box-shadow: 0 0 5px rgba(99, 102, 241, 0.1); }
    100% { box-shadow: 0 0 20px rgba(99, 102, 241, 0.4); }
}

/* --- SIDEBAR SAAS OVERHAUL --- */
[data-testid="stSidebar"] {
    background-color: #03050a !important; 
    border-right: 1px solid rgba(255, 255, 255, 0.05) !important;
}

[data-testid="stSidebarNav"] {
    padding-top: 1.5rem !important;
}

/* Hide the Auth + Embed pages from the sidebar navigation list */
[data-testid="stSidebarNav"] a[href*="0_Auth"],
[data-testid="stSidebarNav"] a[href*="Auth"],
[data-testid="stSidebarNav"] a[href*="4_Embed"],
[data-testid="stSidebarNav"] a[href*="Embed"],
[data-testid="stSidebarNav"] li:has(a[href*="0_Auth"]),
[data-testid="stSidebarNav"] li:has(a[href*="Auth"]),
[data-testid="stSidebarNav"] li:has(a[href*="4_Embed"]),
[data-testid="stSidebarNav"] li:has(a[href*="Embed"]) {
    display: none !important;
}


[data-testid="stSidebarNav"]::before {
    content: "✦ AI PLATFORM";
    font-size: 0.8rem;
    font-weight: 800;
    color: var(--accent);
    padding: 0 1.5rem 1rem 1.5rem;
    display: block;
    letter-spacing: 1.5px;
}

/* Nav Links */
[data-testid="stSidebarNav"] a {
    border-radius: 8px !important;
    margin: 0.2rem 1rem !important;
    transition: all 0.2s ease !important;
    font-weight: 500 !important;
    color: var(--text-secondary) !important;
}

[data-testid="stSidebarNav"] a:hover {
    background-color: rgba(255, 255, 255, 0.03) !important;
    color: var(--text-primary) !important;
}

[data-testid="stSidebarNav"] a span {
    font-size: 0.95rem !important;
}

/* Active Nav Link */
[data-testid="stSidebarNav"] a[aria-current="page"] {
    background-color: rgba(99, 102, 241, 0.1) !important;
    border-left: 3px solid var(--accent) !important;
    color: var(--text-primary) !important;
    font-weight: 600 !important;
    border-radius: 4px 8px 8px 4px !important;
}

/* ════════════════════════════════════════════════════════
   DASHBOARD — Bot Cards (pure HTML, no iframes)
   ════════════════════════════════════════════════════════ */

.dash-title {
    color: var(--text-primary);
    font-family: var(--font);
    font-size: 1.9rem;
    font-weight: 700;
    margin: 0 0 1.5rem 0;
}

/* ── Bot Card ─────────────────────────────────────────── */
.bot-card {
    background: linear-gradient(145deg, rgba(30,36,51,0.85) 0%, rgba(17,24,39,0.9) 100%);
    border: 1px solid rgba(255,255,255,0.08);
    border-radius: 18px;
    padding: 1.4rem 1.5rem 1.2rem 1.5rem;
    height: 210px;
    box-sizing: border-box;
    display: flex;
    flex-direction: column;
    gap: 0.6rem;
    backdrop-filter: blur(12px);
    box-shadow: 0 8px 32px rgba(0,0,0,0.25);
    transition: transform 0.25s ease, border-color 0.25s ease, box-shadow 0.25s ease;
    overflow: hidden;
    font-family: var(--font);
}

.bot-card:hover {
    transform: translateY(-5px);
    border-color: rgba(99,102,241,0.45);
    box-shadow: 0 12px 40px rgba(99,102,241,0.2);
}

/* Header row: avatar + name + public badge */
.bot-card-header {
    display: flex;
    align-items: center;
    gap: 0.85rem;
}

.bot-avatar-wrap {
    font-size: 1.8rem;
    background: rgba(255,255,255,0.06);
    border: 1px solid rgba(255,255,255,0.1);
    border-radius: 50%;
    width: 48px;
    height: 48px;
    display: flex;
    align-items: center;
    justify-content: center;
    flex-shrink: 0;
    box-shadow: inset 0 0 10px rgba(255,255,255,0.04);
}

.bot-card-info {
    display: flex;
    flex-direction: column;
    gap: 0.15rem;
    overflow: hidden;
}

.bot-card-name {
    margin: 0;
    font-size: 1.1rem;
    font-weight: 700;
    color: var(--text-primary);
    white-space: nowrap;
    overflow: hidden;
    text-overflow: ellipsis;
}

.bot-card-pub {
    font-size: 0.7rem;
    color: #64748B;
    font-weight: 500;
    letter-spacing: 0.3px;
}

/* Model badge */
.bot-card-model {
    display: inline-block;
    width: fit-content;
    background: linear-gradient(135deg, rgba(99,102,241,0.18) 0%, rgba(168,85,247,0.18) 100%);
    color: #A5B4FC;
    border: 1px solid rgba(99,102,241,0.3);
    border-radius: 6px;
    padding: 0.18rem 0.65rem;
    font-size: 0.72rem;
    font-weight: 600;
    font-family: var(--font);
    white-space: nowrap;
    overflow: hidden;
    text-overflow: ellipsis;
    max-width: 100%;
}

/* Prompt preview */
.bot-card-preview {
    margin: 0;
    color: #94A3B8;
    font-size: 0.83rem;
    line-height: 1.55;
    display: -webkit-box;
    -webkit-line-clamp: 2;
    -webkit-box-orient: vertical;
    overflow: hidden;
    flex: 1;
    font-style: italic;
}

/* Footer date */
.bot-card-footer {
    font-size: 0.72rem;
    color: #475569;
    border-top: 1px solid rgba(255,255,255,0.05);
    padding-top: 0.5rem;
    margin-top: auto;
}

/* ── Button row: prevent text wrapping ────────────────── */
/* Force all dashboard action buttons to single line */
[data-testid="stHorizontalBlock"] button p,
[data-testid="stHorizontalBlock"] button div {
    white-space: nowrap !important;
    overflow: hidden !important;
    text-overflow: ellipsis !important;
}

/* Secondary (Edit / Deploy) button style */
button[kind="secondary"] {
    background: rgba(255,255,255,0.04) !important;
    border: 1px solid rgba(255,255,255,0.1) !important;
    border-radius: var(--radius-md) !important;
    color: var(--text-secondary) !important;
    font-weight: 500 !important;
    transition: all 0.25s ease !important;
}
button[kind="secondary"]:hover {
    background: rgba(255,255,255,0.08) !important;
    border-color: rgba(255,255,255,0.2) !important;
    color: var(--text-primary) !important;
}

/* Delete button — red danger style
   Targets the last button in each bot card button group */
[data-testid="stColumns"] button[kind="secondary"]:last-child,
button[key*="delete_"] {
    background: rgba(239,68,68,0.1) !important;
    border: 1px solid rgba(239,68,68,0.3) !important;
    color: #F87171 !important;
}
button[key*="delete_"]:hover {
    background: rgba(239,68,68,0.25) !important;
    border-color: rgba(239,68,68,0.6) !important;
    color: #FCA5A5 !important;
}

/* ── Empty state ──────────────────────────────────────── */
.empty-state {
    text-align: center;
    padding: 5rem 2rem;
    background: rgba(17,24,39,0.5);
    border: 1px dashed rgba(255,255,255,0.08);
    border-radius: 20px;
    margin-top: 2rem;
}
.empty-icon { font-size: 3rem; margin-bottom: 1rem; }
.empty-state h3 { color: var(--text-primary); font-size: 1.4rem; margin-bottom: 0.5rem; }
.empty-state p  { color: var(--text-secondary); font-size: 0.95rem; }

/* ── Deploy panel ─────────────────────────────────────── */
.deploy-panel {
    background: rgba(17,24,39,0.9);
    border: 1px solid rgba(99,102,241,0.35);
    border-radius: 12px;
    padding: 1rem 1.2rem;
    margin-top: 0.3rem;
}
.deploy-panel-title {
    font-size: 0.72rem;
    color: #94A3B8;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 1px;
    margin-bottom: 0.5rem;
    font-family: var(--font);
}
.deploy-code {
    display: block;
    font-size: 0.68rem;
    color: #A5B4FC;
    word-break: break-all;
    line-height: 1.6;
    background: rgba(99,102,241,0.08);
    padding: 0.5rem;
    border-radius: 6px;
}
.deploy-hint {
    font-size: 0.7rem;
    color: #475569;
    margin-top: 0.5rem;
    font-family: var(--font);
}

/* ════════════════════════════════════════════════════════
   AUTH PAGE — Login / Register
   ════════════════════════════════════════════════════════ */

/* Center the auth page content */
.auth-wrapper {
    text-align: center;
    padding: 3rem 1rem 2rem 1rem;
}

.auth-logo {
    font-size: 2.5rem;
    color: #6366F1;
    margin-bottom: 0.8rem;
    display: block;
    animation: pulseGlow 3s infinite alternate;
}

.auth-headline {
    font-size: 2rem;
    font-weight: 800;
    color: var(--text-primary);
    margin: 0 0 0.5rem 0;
    font-family: var(--font);
    background: linear-gradient(135deg, #F8FAFC 0%, #A5B4FC 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

.auth-sub {
    color: var(--text-secondary);
    font-size: 1rem;
    margin: 0;
    font-family: var(--font);
}

/* Card container inside tabs */
.auth-card {
    background: linear-gradient(145deg, rgba(30,36,51,0.8), rgba(17,24,39,0.9));
    border: 1px solid rgba(255,255,255,0.07);
    border-radius: 20px;
    padding: 2rem;
    backdrop-filter: blur(16px);
    box-shadow: 0 20px 60px rgba(0,0,0,0.3), 0 0 0 1px rgba(99,102,241,0.05);
    margin-top: 0.5rem;
}

.auth-card-sub {
    color: var(--text-secondary) !important;
    font-size: 0.88rem !important;
    margin: -0.5rem 0 1.2rem 0 !important;
}

/* Style the Streamlit tabs to look SaaS */
[data-testid="stTabs"] [data-baseweb="tab-list"] {
    background: rgba(17,24,39,0.6) !important;
    border-radius: 12px !important;
    padding: 4px !important;
    border: 1px solid rgba(255,255,255,0.06) !important;
    gap: 4px !important;
}

[data-testid="stTabs"] [data-baseweb="tab"] {
    background: transparent !important;
    border-radius: 9px !important;
    color: var(--text-secondary) !important;
    font-weight: 500 !important;
    font-family: var(--font) !important;
    padding: 0.5rem 1.5rem !important;
    transition: all 0.2s ease !important;
    border: none !important;
}

[data-testid="stTabs"] [aria-selected="true"] {
    background: linear-gradient(135deg, #6366F1, #A855F7) !important;
    color: white !important;
    font-weight: 600 !important;
    box-shadow: 0 4px 12px rgba(99,102,241,0.3) !important;
}

[data-testid="stTabs"] [data-baseweb="tab-highlight"] {
    display: none !important;
}

/* Auth page: center the block container */
.auth-page-wrap .block-container {
    max-width: 500px !important;
}

</style>
"""


