def render_chat_preview(avatar, greeting):
    return f"""
    <div style="
        background-color: var(--bg-surface);
        border: 1px solid var(--border);
        border-radius: var(--radius);
        padding: 1.25rem;
        color: var(--text-primary);
        display: flex;
        flex-direction: column;
        gap: 1rem;
        font-family: var(--font);
    ">
        <h4 style="margin:0; border-bottom: 1px solid var(--border); padding-bottom: 0.5rem;">Live Preview</h4>
        <div style="display: flex; gap: 0.75rem; align-items: flex-start;">
            <div style="font-size: 1.5rem;">{avatar}</div>
            <div style="
                background-color: var(--bg-primary);
                border: 1px solid var(--border);
                padding: 0.75rem 1rem;
                border-radius: 0 12px 12px 12px;
                font-size: 0.9rem;
            ">
                {greeting}
            </div>
        </div>
    </div>
    """
