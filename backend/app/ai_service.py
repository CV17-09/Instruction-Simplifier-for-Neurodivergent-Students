import os
import json

from anthropic import Anthropic
from openai import OpenAI

from app.config import (
    AI_PROVIDER,
    OPENAI_API_KEY,
    GROQ_API_KEY,
)

def simplify_assignment(text: str):

    prompt = f"""
You are an accessibility-focused academic assistant.

Simplify the following academic instructions for a neurodivergent student.

Do NOT complete the assignment.
Do NOT remove requirements.

Return ONLY valid JSON.

JSON format:

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

Assignment:

{text}
"""

    # ----------------------
    # Claude
    # ----------------------
    if AI_PROVIDER == "claude":

        client = Anthropic(
            api_key=os.getenv("ANTHROPIC_API_KEY")
        )

        response = client.messages.create(
            model="claude-3-5-sonnet-latest",
            max_tokens=1500,
            temperature=0.2,
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )

        content = response.content[0].text

    # ----------------------
    # Groq
    # ----------------------
    elif AI_PROVIDER == "groq":

        client = OpenAI(
            api_key=GROQ_API_KEY,
            base_url="https://api.groq.com/openai/v1"
        )

        response = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            temperature=0.2,
            messages=[
                {
                    "role": "system",
                    "content": "You simplify academic instructions into structured JSON."
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )

        content = response.choices[0].message.content

    # ----------------------
    # OpenAI
    # ----------------------
    else:

        client = OpenAI(api_key=OPENAI_API_KEY)

        response = client.chat.completions.create(
            model="gpt-4o-mini",
            temperature=0.2,
            messages=[
                {
                    "role": "system",
                    "content": "You simplify academic instructions into structured JSON."
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )

        content = response.choices[0].message.content

    try:
        return json.loads(content)

    except json.JSONDecodeError:

        return {
            "plain_summary": content,
            "start_here": "Read the assignment once without taking notes.",
            "checklist": [],
            "timeline": [],
            "deadlines": [],
            "materials_needed": [],
            "rubric_simplified": "",
            "time_estimate": "Unknown"
        }