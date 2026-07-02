# 🧠 Instruction Simplifier for Neurodivergent Students

<div align="center">

### **Transforming complex academic instructions into clear, manageable learning plans using AI**

*Helping students with ADHD, autism, dyslexia, executive functioning challenges, and other learning differences navigate school with greater confidence.*

![Python](https://img.shields.io/badge/Python-3.12-blue?logo=python)
![FastAPI](https://img.shields.io/badge/FastAPI-Backend-009688?logo=fastapi)
![Next.js](https://img.shields.io/badge/Next.js-Frontend-black?logo=next.js)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-Database-blue?logo=postgresql)
![OpenAI](https://img.shields.io/badge/OpenAI-LLM-412991)
![Groq](https://img.shields.io/badge/Groq-API-orange)
![License](https://img.shields.io/badge/License-MIT-green)

</div>

---

# 📖 Overview

**Instruction Simplifier for Neurodivergent Students** is an AI-powered accessibility platform that transforms dense educational content into structured, easy-to-follow learning plans.

Students can upload assignment prompts, syllabi, grading rubrics, instructor emails, or other academic documents, and the system automatically converts them into:

* ✅ Plain-language summaries
* ✅ Step-by-step action plans
* ✅ Interactive checklists
* ✅ "Start Here" guidance
* ✅ Estimated study timelines
* ✅ Work & break schedules
* ✅ Deadline extraction
* ✅ Simplified grading rubrics

Instead of overwhelming students with large blocks of text, the platform reduces cognitive load and helps users focus on completing one task at a time.

---

# 🎯 The Problem

Academic instructions are often written for experienced readers and may include:

* Long paragraphs
* Multiple hidden requirements
* Ambiguous wording
* Complex grading rubrics
* Several tasks combined into one paragraph
* Important deadlines buried in text

For many neurodivergent students, this can lead to:

* Executive dysfunction
* Task paralysis
* Increased anxiety
* Missed assignment requirements
* Poor time management
* Difficulty knowing where to begin

---

# 💡 The Solution

The platform combines **Large Language Models (LLMs)** with accessibility-focused prompt engineering to convert complicated academic content into structured learning plans.

Each uploaded document is analyzed to produce:

| AI Output                 | Purpose                                     |
| ------------------------- | ------------------------------------------- |
| 📝 Plain Language Summary | Explains the assignment in simpler language |
| ✅ Checklist               | Breaks work into manageable tasks           |
| 🚀 Start Here             | Identifies the first actionable step        |
| 📅 Study Timeline         | Creates a suggested completion schedule     |
| ⏱️ Time Estimate          | Estimates workload                          |
| 📌 Deadline Extraction    | Finds important due dates                   |
| 📚 Materials Needed       | Lists required resources                    |
| 🎓 Rubric Simplification  | Explains grading expectations               |

---

# ✨ Features

## 🧠 AI Plain-Language Translation

Transforms academic writing into clear, concise explanations without changing the assignment requirements.

### Before

> Compose a comparative literary analysis synthesizing at least four scholarly sources while adhering to MLA formatting guidelines.

### After

> Write a paper comparing two literary works. Use at least four academic sources and format everything in MLA style.

---

## ✅ Smart Task Breakdown

Large assignments become manageable steps.

```
Read the assignment
        ↓
Gather research
        ↓
Create an outline
        ↓
Write introduction
        ↓
Complete body paragraphs
        ↓
Write conclusion
        ↓
Proofread
        ↓
Submit
```

---

## 🚀 "Start Here" Guidance

Executive dysfunction often makes starting the hardest part.

The application always generates the **first actionable task**, helping students begin immediately.

**Example**

```
Start Here

Read the assignment once without taking notes.
```

---

## 📅 Personalized Study Planner

Automatically builds a study schedule based on assignment complexity.

| Day   | Tasks                                |
| ----- | ------------------------------------ |
| Day 1 | Read instructions & collect research |
| Day 2 | Build outline                        |
| Day 3 | Write first draft                    |
| Day 4 | Revise paper                         |
| Day 5 | Submit assignment                    |

---

## ☑ Interactive Assignment Checklist

Automatically generates a checklist.

* [ ] Read assignment
* [ ] Find research sources
* [ ] Create outline
* [ ] Write introduction
* [ ] Complete body paragraphs
* [ ] Write conclusion
* [ ] Format citations
* [ ] Proofread
* [ ] Submit

---

## 📌 Deadline Detection

The AI extracts important details including:

* Assignment due date
* Submission platform
* File format
* Citation style
* Minimum word count
* Required references

---

## 📊 Rubric Simplification

Complex grading criteria become easy-to-understand expectations.

**Original**

> Demonstrates comprehensive synthesis of scholarly literature.

**Simplified**

> Combine ideas from several academic sources and explain how they connect.

---

## 📧 Instructor Email Simplifier

Paste a long email from an instructor and instantly receive:

* Important updates
* Required actions
* New deadlines
* Key announcements

---

## ♿ Accessibility-First Design

Designed using inclusive design principles.

✔ High-contrast interface

✔ Large readable typography

✔ Keyboard navigation

✔ Screen reader compatibility

✔ Mobile responsive

✔ Minimal visual clutter

✔ Reduced cognitive load

---

# 🏗 System Architecture

```text
                  Academic Documents
     (PDF • Syllabus • Email • Rubric • Prompt)
                          │
                          ▼
                 Text Extraction Layer
                          │
                          ▼
                Cleaning & Preprocessing
                          │
                          ▼
                  AI Processing Engine
                (Prompt Engineering + LLM)
                          │
          ┌───────────────┼───────────────┐
          ▼               ▼               ▼
   Plain Summary    Step Checklist   Study Planner
          ▼               ▼               ▼
        JSON Structured Response
                          │
                          ▼
             React / Next.js User Interface
```

---

# ⚙ Technology Stack

| Category                | Technologies                                |
| ----------------------- | ------------------------------------------- |
| **Frontend**            | Next.js • React • TypeScript • Tailwind CSS |
| **Backend**             | FastAPI • Python                            |
| **AI**                  | OpenAI • Groq • Prompt Engineering          |
| **Database**            | PostgreSQL • SQLAlchemy                     |
| **Document Processing** | PyMuPDF • pdfplumber • python-docx          |
| **Authentication**      | Clerk / Auth.js                             |
| **Deployment**          | Docker • Vercel • Render                    |

---

# 🔄 AI Processing Pipeline

```text
Upload Document
        │
        ▼
Extract Text
        │
        ▼
Clean & Normalize
        │
        ▼
Prompt Engineering
        │
        ▼
Large Language Model
        │
        ▼
Structured JSON
        │
        ▼
Frontend Dashboard
```

---

# 📸 Example Output

### Assignment Summary

**Goal**

Write a five-page research paper about climate change.

---

### 🚀 Start Here

Read the assignment carefully and identify all required deliverables.

---

### ✅ Checklist

* Read assignment
* Find five academic sources
* Build outline
* Write first draft
* Edit
* Format citations
* Submit

---

### 📅 Timeline

**Today**

• Read assignment

• Collect research

**Tomorrow**

• Create outline

**Day 3**

• Write draft

**Day 4**

• Revise

**Day 5**

• Submit

---

# 🚀 Future Enhancements

* OCR support for scanned documents
* Canvas LMS integration
* Blackboard integration
* Moodle integration
* Google Classroom support
* Calendar synchronization
* Voice summaries
* Personalized learning profiles
* Mobile application
* Multilingual support

---

# 🎯 Educational Impact

This project demonstrates how generative AI can improve accessibility by reducing cognitive overload and helping students understand academic expectations without changing assignment requirements.

Rather than replacing learning, the application empowers students to:

* Learn independently
* Stay organized
* Reduce anxiety
* Build executive functioning skills
* Improve academic confidence

---

# 📚 Learning Outcomes

Through this project, I explored:

* AI-powered document understanding
* Prompt engineering
* Accessibility-first UX design
* Educational technology
* Full-stack AI development
* Structured JSON generation
* Python backend development
* Modern React application architecture

---

<div align="center">

## 🌟 Making education more accessible, one assignment at a time.

**Built with AI • Designed for Accessibility • Focused on Student Success**

</div>

---

## 📄 License

Released under the **MIT License**.

