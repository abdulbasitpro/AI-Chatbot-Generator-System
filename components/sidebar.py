import streamlit as st

def render_sidebar():
    st.sidebar.markdown(
        """
        <div style="font-size: 0.95rem; color: #94A3B8; margin-top: 0.5rem; margin-bottom: 1.5rem; line-height: 1.6;">
            Deploy custom AI chatbots powered by <b>Llama 3.1</b> & <b>Gemma 2</b>.
        </div>
        """, unsafe_allow_html=True
    )
    st.sidebar.markdown(
        """
        <div style="background: rgba(17, 24, 39, 0.5); padding: 1rem; border-radius: 8px; border: 1px solid rgba(255,255,255,0.05); margin-top: 1rem;">
            <div style="font-size: 0.75rem; color: #64748B; font-weight: 700; text-transform: uppercase; letter-spacing: 1px; margin-bottom: 0.5rem;">
                System Status
            </div>
            <div style="display: flex; align-items: center; gap: 8px;">
                <div style="width: 8px; height: 8px; border-radius: 50%; background-color: #10B981; box-shadow: 0 0 10px #10B981; animation: pulseGlow 2s infinite alternate;"></div>
                <span style="font-size: 0.85rem; color: #F8FAFC; font-weight: 500;">Groq API Connected</span>
            </div>
        </div>
        """, unsafe_allow_html=True
    )
