# Architecture

## Flow

User pastes assignment text.

↓

Next.js sends text to FastAPI.

↓

FastAPI validates text.

↓

AI service sends prompt to OpenAI or Groq.

↓

The LLM returns structured JSON.

↓

FastAPI saves the original text and simplified output to PostgreSQL.

↓

Frontend displays:

- Plain-language summary
- Start Here guidance
- Checklist
- Timeline
- Deadlines
- Materials needed
- Simplified rubric
- Time estimate

## Tech Stack

Frontend:

- Next.js
- React
- TypeScript
- Tailwind CSS

Backend:

- FastAPI
- Python
- SQLAlchemy
- PostgreSQL

AI:

- OpenAI
- Groq
- Prompt Engineering

Database:

- PostgreSQL