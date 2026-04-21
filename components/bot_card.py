def render_bot_card(bot):
    html_code = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <script src="https://unpkg.com/react@18/umd/react.production.min.js"></script>
        <script src="https://unpkg.com/react-dom@18/umd/react-dom.production.min.js"></script>
        <script src="https://unpkg.com/@babel/standalone/babel.min.js"></script>
        <link href="https://fonts.googleapis.com/css2?family=Outfit:wght@400;500;600&display=swap" rel="stylesheet">
        <style>
            :root {{
                --bg-primary: #060913;
                --bg-surface: rgba(30, 36, 51, 0.6);
                --bg-surface-hover: rgba(40, 48, 68, 0.8);
                --accent: #6366F1;
                --text-primary: #F8FAFC;
                --text-secondary: #94A3B8;
                --border: rgba(255, 255, 255, 0.08);
                --shadow-glow: 0 0 20px rgba(99, 102, 241, 0.15);
                --radius-lg: 16px;
                --font: 'Outfit', sans-serif;
            }}
            body {{
                margin: 0;
                font-family: var(--font);
                background-color: transparent;
            }}
            .card {{
                background-color: var(--bg-surface);
                border: 1px solid var(--border);
                border-radius: var(--radius-lg);
                padding: 1.5rem;
                color: var(--text-primary);
                display: flex;
                flex-direction: column;
                gap: 0.85rem;
                height: 100%;
                box-sizing: border-box;
                backdrop-filter: blur(10px);
                transition: transform 0.3s ease, border-color 0.3s ease, box-shadow 0.3s ease, background-color 0.3s ease;
            }}
            .card:hover {{
                transform: translateY(-4px);
                border-color: rgba(99, 102, 241, 0.4);
                box-shadow: var(--shadow-glow);
                background-color: var(--bg-surface-hover);
            }}
            .header {{
                display: flex;
                align-items: center;
                gap: 1rem;
            }}
            .avatar-wrapper {{
                background: rgba(255,255,255,0.05);
                padding: 0.5rem;
                border-radius: 50%;
                font-size: 1.7rem;
                border: 1px solid rgba(255,255,255,0.1);
                box-shadow: inset 0 0 10px rgba(255,255,255,0.05);
            }}
            .title {{
                margin: 0;
                font-size: 1.2rem;
                font-weight: 600;
            }}
            .model {{
                background: linear-gradient(135deg, rgba(99, 102, 241, 0.2) 0%, rgba(168, 85, 247, 0.2) 100%);
                color: #A5B4FC;
                padding: 0.25rem 0.75rem;
                border-radius: 6px;
                font-size: 0.75rem;
                font-weight: 500;
                width: max-content;
                border: 1px solid rgba(99, 102, 241, 0.3);
            }}
            .preview {{
                color: var(--text-secondary);
                font-size: 0.9rem;
                line-height: 1.6;
                display: -webkit-box;
                -webkit-line-clamp: 2;
                -webkit-box-orient: vertical;
                overflow: hidden;
                flex-grow: 1;
            }}
            .footer {{
                font-size: 0.75rem;
                color: var(--text-secondary);
                margin-top: auto;
                border-top: 1px solid var(--border);
                padding-top: 0.75rem;
            }}
        </style>
    </head>
    <body>
        <div id="root"></div>
        <script type="text/babel">
            const BotCard = () => {{
                return (
                    <div className="card">
                        <div className="header">
                            <div className="avatar-wrapper">{bot.get('avatar', '🤖')}</div>
                            <h3 className="title">{bot.get('name', 'Unnamed Bot')}</h3>
                        </div>
                        <div className="model">{bot.get('model', 'llama-3.1-8b-instant')}</div>
                        <p className="preview">"{bot.get('system_prompt', 'No personality defined.')[:60]}..."</p>
                        <div className="footer">Created: {bot.get('created_at', 'Unknown')}</div>
                    </div>
                );
            }};
            const root = ReactDOM.createRoot(document.getElementById('root'));
            root.render(<BotCard />);
        </script>
    </body>
    </html>
    """
    return html_code
