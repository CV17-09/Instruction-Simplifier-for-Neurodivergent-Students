Instruction-Simplifier-for-Neurodivergent-Students

Transforming complex academic instructions into clear, structured, and actionable learning plans.

Overview

Instruction Simplifier for Neurodivergent Students is an AI-powered accessibility platform designed to help students with ADHD, autism, dyslexia, executive functioning challenges, and other learning differences better understand academic instructions.

The application converts dense educational content—such as assignment prompts, course syllabi, grading rubrics, and instructor emails—into easy-to-follow formats that reduce cognitive overload and improve task initiation.

Instead of overwhelming users with large blocks of text, the platform generates plain-language summaries, prioritized action steps, personalized checklists, estimated completion timelines, and recommended work/break schedules to help students stay organized and focused.

Problem

Many academic materials are written for experienced readers and often contain:

Long paragraphs
Multiple embedded requirements
Ambiguous wording
Hidden deadlines
Several tasks mixed together
Complex grading rubrics

For neurodivergent students, these formats can create barriers including:

Difficulty understanding where to begin
Executive dysfunction
Task paralysis
Increased anxiety
Missed assignment requirements
Poor time management

Current AI assistants summarize text, but they rarely reorganize instructions into an accessibility-first workflow specifically designed for neurodivergent learners.

Solution

Instruction Simplifier uses Large Language Models (LLMs) combined with structured prompt engineering to transform educational content into actionable learning plans.

Given any academic instruction, the system automatically generates:

Plain-language explanation
Assignment objective
Step-by-step checklist
Priority ordering ("Do this first")
Estimated completion time
Suggested work/break schedule
Important deadlines and deliverables
Materials required
Questions students may need to ask their instructor

The goal is not to change assignment requirements—it is to improve comprehension and accessibility.

Key Features
AI Plain-Language Translation

Converts complex educational language into clear, concise explanations while preserving the original meaning.

Example:

Original

"Compose a comparative literary analysis synthesizing at least four scholarly sources while adhering to MLA formatting guidelines."

Simplified

Write a paper comparing two literary works. Use at least four academic sources and format everything using MLA style.

Smart Task Breakdown

Large assignments are automatically divided into smaller, manageable tasks.

Example:

Read assignment
Gather research articles
Create outline
Write introduction
Write body paragraphs
Write conclusion
Format citations
Proofread
Submit
Priority Starter

Executive dysfunction often makes starting the hardest step.

The application highlights:

Start Here

Read the assignment once without taking notes.

Then continues with the next actionable task.

Personalized Study Timeline

Based on assignment length and complexity, the application estimates:

Total workload
Suggested completion date
Daily milestones
Pomodoro work sessions
Recommended break intervals

Example:

Day 1

Read assignment
Find references

Day 2

Create outline

Day 3

Write first draft

Day 4

Revise and submit
Assignment Checklist

Students receive an interactive checklist including every required deliverable.

Example:

☐ Read prompt

☐ Identify deadline

☐ Collect sources

☐ Create outline

☐ Complete first draft

☐ Edit

☐ Submit

Deadline Extraction

The AI identifies important information such as:

Due dates
Required file formats
Submission platform
Citation style
Minimum word count
Required references
Rubric Simplification

Complex grading rubrics become understandable scoring guides.

Example:

Original:

"Demonstrates comprehensive synthesis of scholarly literature."

Simplified:

Explain ideas from several academic sources and connect them together.

Instructor Email Simplification

Students can paste long emails from instructors.

The application extracts:

What changed
What students must do
Important deadlines
Required actions
Accessibility-First Design

Designed with inclusive learning principles:

Minimal visual clutter
High contrast interface
Large typography
Keyboard navigation
Screen reader support
Mobile-friendly layout
Reduced cognitive load
System Architecture
                Academic Content
        (PDF, Email, Prompt, Rubric)
                       │
                       ▼
               Input Processing Layer
                       │
                       ▼
            Text Cleaning & Extraction
                       │
                       ▼
              Large Language Model
             (Instruction Analysis)
                       │
                       ▼
       ┌─────────────────────────────────┐
       │ Plain Summary                   │
       │ Step Checklist                  │
       │ Starter Task                    │
       │ Timeline Generator              │
       │ Deadline Extractor              │
       │ Rubric Simplifier               │
       └─────────────────────────────────┘
                       │
                       ▼
              React Frontend Dashboard
Tech Stack
Frontend
React
Next.js
TypeScript
Tailwind CSS
Backend
FastAPI
Python
AI
OpenAI GPT
Groq API
Prompt Engineering
Structured JSON Outputs
Data Processing
PyMuPDF
pdfplumber
python-docx
Pandas
Database
PostgreSQL
SQLAlchemy
Authentication
Clerk/Auth.js
JWT Authentication
Deployment
Docker
Vercel
Render
AI Workflow
User uploads or pastes academic content.
Text is extracted and cleaned.
The backend sends structured prompts to the LLM.
The model identifies objectives, deadlines, requirements, and tasks.
Responses are validated into structured JSON.
The frontend renders:
Plain-language summary
Checklist
Timeline
Priority starter
Study schedule
Example Output
Assignment Summary

Goal

Write a five-page research paper about climate change.

Start Here

Read the assignment carefully and highlight the required sections.

Checklist
Read assignment
Find five academic sources
Create outline
Write introduction
Write body
Write conclusion
Format APA citations
Proofread
Submit
