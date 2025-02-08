import json
import os

DEFAULT_LANG = "en"

def load_messages(lang=DEFAULT_LANG):
    lang_file = f"src/lang/{lang}.json"
    if not os.path.exists(lang_file):
        lang_file = f"src/lang/{DEFAULT_LANG}.json"  # Fallback to English
    with open(lang_file, "r", encoding="utf-8") as f:
        return json.load(f)

def translate(key, lang="en", **kwargs):
    messages = load_messages(lang)
    message = messages.get(key, key)  # Fallback to key if not found
    return message.format(**kwargs)