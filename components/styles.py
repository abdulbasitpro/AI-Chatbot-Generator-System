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

/* Hide Default Streamlit Clutter */
header { visibility: hidden !important; }
.block-container {
    padding-top: 2rem !important;
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
    height: 100%;
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

</style>
"""
