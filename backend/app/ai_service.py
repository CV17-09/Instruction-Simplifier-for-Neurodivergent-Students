import json
from openai import OpenAI
from app.config import OPENAI_API_KEY, GROQ_API_KEY, AI_PROVIDER

def get_client():
    if AI_PROVIDER == "groq":
        return OpenAI(
            api_key=GROQ_API_KEY,
            base_url="https://api.groq.com/openai/v1"
        )

    return OpenAI(api_key=OPENAI_API_KEY)

def simplify_assignment(text: str):
    client = get_client()

    prompt = f"""
You are an accessibility-focused academic assistant.

Simplify the following academic instructions for a neurodivergent student.
Do not complete the assignment. Do not remove requirements.
Only make the instructions easier to understand and organize.

Return ONLY valid JSON with this structure:

{{
  "plain_summary": "",
  "start_here": "",
  "checklist": [],
  "timeline": [],
  "deadlines": [],
  "materials_needed": [],
  "rubric_simplified": "",
  "time_estimate": ""
}}

Assignment text:
{text}
"""

    model = "llama-3.1-8b-instant" if AI_PROVIDER == "groq" else "gpt-4o-mini"

    response = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": "You simplify academic instructions into clear structured JSON."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.2
    )

    content = response.choices[0].message.content

    try:
        return json.loads(content)
    except json.JSONDecodeError:
        return {
            "plain_summary": content,
            "start_here": "Read the instructions once and highlight the main task.",
            "checklist": [],
            "timeline": [],
            "deadlines": [],
            "materials_needed": [],
            "rubric_simplified": "",
            "time_estimate": "Not available"
        }