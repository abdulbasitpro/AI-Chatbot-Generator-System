def render_bot_card(bot):
    """Returns a pure HTML/CSS bot card — use with st.markdown(unsafe_allow_html=True)
    No iframes, no React — guaranteed equal size across all columns."""
    name    = bot.get('name', 'Unnamed Bot')
    avatar  = bot.get('avatar', '🤖')
    model   = bot.get('model', 'llama-3.1-8b-instant')
    prompt  = bot.get('system_prompt', 'No personality defined.')[:75]
    created = bot.get('created_at', 'Unknown')
    pub     = "🌐 Public" if bot.get('is_public') else "🔒 Private"

    return f"""
<div class="bot-card">
    <div class="bot-card-header">
        <div class="bot-avatar-wrap">{avatar}</div>
        <div class="bot-card-info">
            <h3 class="bot-card-name">{name}</h3>
            <span class="bot-card-pub">{pub}</span>
        </div>
    </div>
    <span class="bot-card-model">{model}</span>
    <p class="bot-card-preview">"{prompt}…"</p>
    <div class="bot-card-footer">📅 {created}</div>
</div>
"""
