import json
import hashlib
import uuid
import os
from datetime import datetime
from cryptography.fernet import Fernet
from dotenv import load_dotenv

# Ensure env vars are loaded even if called directly
load_dotenv()

USERS_FILE = "data/users.json"

# ── Encryption Helpers ─────────────────────────────────────────────────────────

def _get_fernet():
    """Initialize Fernet with the key from environment or generate a temporary one."""
    key = os.getenv("ENCRYPTION_KEY")
    if not key:
        # Fallback for development (in production, this would cause issues if key changes)
        # Ideally, we should log a warning or raise an error in production.
        return None
    try:
        return Fernet(key.encode())
    except Exception:
        return None

def encrypt_key(plain_text: str) -> str:
    """Encrypt a string using the ENCRYPTION_KEY."""
    if not plain_text: return ""
    f = _get_fernet()
    if not f: return plain_text  # Fallback to plain text if no key is configured
    return f.encrypt(plain_text.encode()).decode()

def decrypt_key(encrypted_text: str) -> str:
    """Decrypt a string using the ENCRYPTION_KEY."""
    if not encrypted_text: return ""
    # If it doesn't look like Fernet (doesn't have the signature), return as is
    # This handles legacy plain-text keys gracefully.
    if not encrypted_text.startswith("gAAAA"):
        return encrypted_text
    
    f = _get_fernet()
    if not f: return encrypted_text
    try:
        return f.decrypt(encrypted_text.encode()).decode()
    except Exception:
        return encrypted_text

# ── Storage Helpers ────────────────────────────────────────────────────────────

def _hash(password: str) -> str:
    """SHA-256 hash of password (no external libs needed)."""
    return hashlib.sha256(password.encode("utf-8")).hexdigest()

def _load_users() -> list:
    if not os.path.exists(USERS_FILE):
        return []
    with open(USERS_FILE, "r") as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return []

def _save_users(users: list):
    os.makedirs("data", exist_ok=True)
    with open(USERS_FILE, "w") as f:
        json.dump(users, f, indent=2)

# ── Public API ─────────────────────────────────────────────────────────────────

def register_user(name: str, email: str, password: str) -> dict:
    """
    Register a new user.
    Returns {"ok": True, "user": {...}} or {"ok": False, "error": "..."}
    """
    name  = name.strip()
    email = email.strip().lower()
    if not name or not email or not password:
        return {"ok": False, "error": "All fields are required."}
    if len(password) < 6:
        return {"ok": False, "error": "Password must be at least 6 characters."}
    if "@" not in email or "." not in email:
        return {"ok": False, "error": "Enter a valid email address."}

    users = _load_users()
    if any(u["email"] == email for u in users):
        return {"ok": False, "error": "An account with this email already exists."}

    user = {
        "id":         str(uuid.uuid4()),
        "name":       name,
        "email":      email,
        "password":   _hash(password),
        "created_at": datetime.now().strftime("%Y-%m-%d %H:%M"),
    }
    users.append(user)
    _save_users(users)
    return {"ok": True, "user": _safe(user)}


def login_user(email: str, password: str) -> dict:
    """
    Authenticate user.
    Returns {"ok": True, "user": {...}} or {"ok": False, "error": "..."}
    """
    email = email.strip().lower()
    users = _load_users()
    for u in users:
        if u["email"] == email and u["password"] == _hash(password):
            return {"ok": True, "user": _safe(u)}
    return {"ok": False, "error": "Invalid email or password."}


def _safe(user: dict) -> dict:
    """Return user dict without the password hash."""
    return {k: v for k, v in user.items() if k != "password"}


# ── Streamlit session helpers ──────────────────────────────────────────────────

def is_logged_in(session_state) -> bool:
    return bool(session_state.get("auth_user"))

def get_current_user(session_state) -> dict | None:
    return session_state.get("auth_user")

def set_session(session_state, user: dict):
    session_state["auth_user"] = user

def logout(session_state):
    session_state.pop("auth_user", None)

# ── Per-user Groq API key ──────────────────────────────────────────────────────

def save_user_api_key(user_id: str, api_key: str) -> bool:
    """Save Groq API key (encrypted) to the user's account record."""
    users = _load_users()
    updated = False
    for u in users:
        if u["id"] == user_id:
            u["groq_api_key"] = encrypt_key(api_key.strip())
            updated = True
            break
    if updated:
        _save_users(users)
    return updated

def get_user_api_key(user_id: str) -> str | None:
    """Return the decrypted Groq API key for a user, or None."""
    for u in _load_users():
        if u["id"] == user_id:
            val = u.get("groq_api_key")
            return decrypt_key(val) if val else None
    return None
