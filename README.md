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
