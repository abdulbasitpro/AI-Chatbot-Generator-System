def render_bot_card(bot):
    html_code = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <script src="https://unpkg.com/react@18/umd/react.production.min.js"></script>
        <script src="https://unpkg.com/react-dom@18/umd/react-dom.production.min.js"></script>
        <script src="https://unpkg.com/@babel/standalone/babel.min.js"></script>
        <style>
            :root {{
                --bg-primary: #0A0E1A;
                --bg-surface: #1E2433;
                --accent: #6366F1;
                --accent-hover: #4F46E5;
                --text-primary: #F1F5F9;
                --text-secondary: #94A3B8;
                --border: #1E2D45;
                --radius: 12px;
                --font: 'Inter', sans-serif;
            }}
            body {{
                margin: 0;
                font-family: var(--font);
            }}
            .card {{
                background-color: var(--bg-surface);
                border: 1px solid var(--border);
                border-radius: var(--radius);
                padding: 1.25rem;
                color: var(--text-primary);
                display: flex;
                flex-direction: column;
                gap: 0.75rem;
                height: 100%;
                box-sizing: border-box;
            }}
            .header {{
                display: flex;
                align-items: center;
                gap: 0.75rem;
            }}
            .avatar {{
                font-size: 1.5rem;
            }}
            .title {{
                margin: 0;
                font-size: 1.1rem;
                font-weight: 600;
            }}
            .model {{
                background-color: var(--bg-primary);
                color: var(--text-secondary);
                padding: 0.25rem 0.5rem;
                border-radius: 4px;
                font-size: 0.75rem;
                width: max-content;
                border: 1px solid var(--border);
            }}
            .preview {{
                color: var(--text-secondary);
                font-size: 0.85rem;
                line-height: 1.4;
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
            }}
            .actions {{
                display: flex;
                gap: 0.5rem;
                margin-top: 0.5rem;
            }}
            .btn {{
                flex: 1;
                padding: 0.5rem;
                border-radius: 6px;
                border: none;
                cursor: pointer;
                font-weight: 600;
                font-size: 0.85rem;
                text-align: center;
                text-decoration: none;
                transition: background-color 0.2s;
            }}
            .btn-chat {{
                background-color: var(--accent);
                color: white;
            }}
            .btn-chat:hover {{
                background-color: var(--accent-hover);
            }}
            .btn-edit {{
                background-color: var(--bg-primary);
                border: 1px solid var(--border);
                color: var(--text-primary);
            }}
            .btn-edit:hover {{
                border-color: var(--text-secondary);
            }}
        </style>
    </head>
    <body>
        <div id="root"></div>
        <script type="text/babel">
            const BotCard = () => {{
                // Note: clicking these will reload the parent window to the specific page and query param.
                return (
                    <div className="card">
                        <div className="header">
                            <span className="avatar">{bot.get('avatar', '🤖')}</span>
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
