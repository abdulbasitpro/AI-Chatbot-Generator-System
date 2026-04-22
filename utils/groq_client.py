from groq import Groq
import time

def get_groq_client(api_key: str) -> Groq:
    """Return a Groq client using the provided API key."""
    return Groq(api_key=api_key)

def validate_api_key(api_key: str) -> dict:
    """
    Quick validation: calls the models list endpoint.
    Returns {"ok": True} or {"ok": False, "error": "..."}
    """
    if not api_key or not api_key.strip().startswith("gsk_"):
        return {"ok": False, "error": "A valid Groq API key starts with 'gsk_'."}
    try:
        client = get_groq_client(api_key.strip())
        client.models.list()          # lightweight call — no tokens used
        return {"ok": True}
    except Exception as e:
        msg = str(e)
        if "401" in msg or "invalid_api_key" in msg.lower():
            return {"ok": False, "error": "Invalid API key. Check it at console.groq.com."}
        return {"ok": False, "error": f"Could not connect: {msg[:120]}"}

def stream_chat_response(messages, model, system_prompt,
                         api_key: str,
                         temperature=0.7, max_tokens=500):
    """Stream a chat completion using the caller's own Groq API key."""
    client = get_groq_client(api_key)
    full_messages = [{"role": "system", "content": system_prompt}] + messages
    stream = client.chat.completions.create(
        model=model,
        messages=full_messages,
        temperature=temperature,
        max_tokens=max_tokens,
        stream=True,
    )
    for chunk in stream:
        content = chunk.choices[0].delta.content
        if content:
            yield content

def get_available_models() -> dict:
    return {
        "llama-3.1-8b-instant":    "Llama 3.1 8B  — Fast & Free",
        "llama-3.3-70b-versatile": "Llama 3.3 70B — Smart & Free",
        "mixtral-8x7b-32768":      "Mixtral 8x7B  — Balanced & Free",
        "gemma2-9b-it":            "Gemma 2 9B    — Lightweight & Free",
    }
