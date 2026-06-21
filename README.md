# AI Software Company Project

## Overview

An AI-powered software company simulator that uses multiple cooperative agents to transform ideas into software projects. The system supports persistent memory, agent communication, project management workflows, automated development, testing, and documentation.

---

## Features

### 🤖 Chatbot

- Accept ideas, prompts, and questions
- Support follow-up conversations through memory
- Create and manage projects

### 🧠 Multi-Agent System

#### Project Manager Agent
- Break projects into tasks
- Delegate work to other agents
- Coordinate workflows
- Communicate results

#### Requirements Agent
- Generate specifications
- Create functional requirements
- Create non-functional requirements

#### Architecture Agent
- Design system architecture
- Plan frontend, backend, database, and authentication
- Generate diagrams

#### Developer Agent
- Write code
- Generate files and components

#### QA Agent
- Create and execute tests
- Detect bugs and edge cases
- Identify missing validation and security issues
- Generate reports

#### Documentation Agent
- Generate README files
- Create API documentation
- Provide setup instructions
- Add code comments

---

## Dashboard

Visual panels display:

- Agent conversations
- Project progression
- Activity feed
- Scrum/Kanban boards
- Progress indicators

---

## Database

Stores:

- Projects (prompts)
- Tasks
- Agent messages
- Code files
- Meetings
- Documents

---

## 🚀 How to Run This Project

## ⚡ Overview

This project uses:

- React + Vite for the frontend  
- FastAPI for the backend  
- PostgreSQL for the database  

React + Vite solve two major pain points in modern web development:
- Fast server startup
- Instant file hot-reloading during development

---

## 🖥️ Frontend (React + Vite)

### Status

- React running ✔  
- Vite dev server working ✔  
- Frontend visible in browser ✔  

### Run frontend

```bash
cd frontend
cd "AI Software Company"
npm install
npm run dev
```

#### Then open: http://localhost:5173

## 🧠 Backend (FastAPI)

### Status

- FastAPI running ✔
- SwaggerUI running ✔
- uvicorn running ✔

### Run backend
```bash
Run backend
cd backend
uvicorn main:app --reload
```

#### Then open: http://localhost:8000/docs

## 🗄️ Database (PostgreSQL)

### Make sure PostgreSQL is running locally and your database is created before starting the backend.

## 🔁 Full Stack Flow

```text
React (5173)
  |
  v
fetch()
  |
  v
FastAPI (8000)
  |
  v
SQL
  |
  v
PostgreSQL
```

## 💡 Notes

- Keep both frontend and backend running at the same time  
- If CORS errors occur, ensure FastAPI has CORS middleware enabled  
- Restart backend after any Python changes  

---

## ⚙️ Tech Stack

| Component | Technology |
|----------|------------|
| Frontend | React |
| Backend | FastAPI, Python |
| Agents | LangGraph |
| LLM | OpenAI API or local models |
| Database | PostgreSQL |
| Memory | Chroma Vector Database |

---

## 📅 Development Schedule

### Week 1
Chatbot with Memory

- User → LLM interaction  
- Create projects  
- Save data to database  
- Generate requirements  

---

### Week 2
Multi-Agent Workflow

User → Project Manager → Architecture → Other Agents  

---

### Week 3
UI Panels

- Chat window  
- Requirements panel  
- Architecture panel  
- Activity feed  

---

### Week 4
Project Workflows

- Scrum boards  
- Task tracking  

---

### Week 5
Developer Agent

---

### Week 6
QA Agent

---

### Week 7
Agent Conversations

---

### Week 8
Long-Term Memory

---

### Week 9
GitHub Integration

---

## 🏗️ Architecture

User
  ↓
Chatbot
  ↓
Project Manager Agent
  ├── Requirements Agent
  ├── Architecture Agent
  ├── Developer Agent
  ├── QA Agent
  └── Documentation Agent
  ↓
Dashboard + Database

---

## 🚀 Long-Term Goal

Create an autonomous AI software company capable of:

- Receiving ideas from users  
- Planning and organizing projects  
- Designing architectures  
- Writing code  
- Testing applications  
- Generating documentation  
- Maintaining memory across conversations  
- Collaborating through multiple specialized agents
