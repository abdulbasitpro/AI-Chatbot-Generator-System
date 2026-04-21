import json
import os
import uuid
from datetime import datetime

STORAGE_FILE = "data/chatbots.json"

def load_chatbots():
    if not os.path.exists(STORAGE_FILE):
        return []
    with open(STORAGE_FILE, "r") as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return []

def save_chatbot(config: dict):
    bots = load_chatbots()
    if "id" not in config or not config["id"]:
        config["id"] = str(uuid.uuid4())[:8]
    config["created_at"] = datetime.now().strftime("%Y-%m-%d %H:%M")
    
    # Remove older version if updating
    bots = [b for b in bots if b["id"] != config["id"]]
    bots.append(config)
    
    os.makedirs("data", exist_ok=True)
    with open(STORAGE_FILE, "w") as f:
        json.dump(bots, f, indent=2)
    return config["id"]

def delete_chatbot(bot_id: str):
    bots = [b for b in load_chatbots() if b["id"] != bot_id]
    with open(STORAGE_FILE, "w") as f:
        json.dump(bots, f, indent=2)
