from groq import Groq
import streamlit as st
import time

def get_groq_client():
    return Groq(api_key=st.secrets["GROQ_API_KEY"])

def stream_chat_response(messages, model, system_prompt, temperature=0.7, max_tokens=500):
    client = get_groq_client()
    full_messages = [{"role": "system", "content": system_prompt}] + messages
    start = time.time()
    stream = client.chat.completions.create(
        model=model,
        messages=full_messages,
        temperature=temperature,
        max_tokens=max_tokens,
        stream=True
    )
    for chunk in stream:
        content = chunk.choices[0].delta.content
        if content:
            yield content
    elapsed = round(time.time() - start, 2)
    return elapsed

def get_available_models():
    return {
        "llama-3.1-8b-instant": "Llama 3.1 8B — Fast & Free",
        "llama-3.1-70b-versatile": "Llama 3.1 70B — Smart & Free",
        "mixtral-8x7b-32768": "Mixtral 8x7B — Balanced & Free",
        "gemma2-9b-it": "Gemma 2 9B — Lightweight & Free"
    }
