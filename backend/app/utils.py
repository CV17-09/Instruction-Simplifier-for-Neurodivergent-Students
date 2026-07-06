import json

def safe_json_dumps(data):
    return json.dumps(data, ensure_ascii=False)

def validate_text(text: str):
    if not text or len(text.strip()) < 20:
        raise ValueError("Text is too short to simplify.")

    return text.strip()