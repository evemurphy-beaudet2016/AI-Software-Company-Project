# AI Software Company Project

## Overview

An AI-powered software company simulator that uses multiple cooperative agents to transform ideas into software projects. The system supports persistent memory, agent communication, project management workflows, automated development, testing, and documentation.

---

## Features

### 🤖 Chatbot

* Accept ideas, prompts, and questions
* Support follow-up conversations through memory
* Create and manage projects

### 🧠 Multi-Agent System

#### Project Manager Agent

* Break projects into tasks
* Delegate work to other agents
* Coordinate workflows
* Communicate results

#### Requirements Agent

* Generate specifications
* Create functional requirements
* Create non-functional requirements

#### Architecture Agent

* Design system architecture
* Plan frontend, backend, database, and authentication
* Generate diagrams

#### Developer Agent

* Write code
* Generate files and components

#### QA Agent

* Create and execute tests
* Detect bugs and edge cases
* Identify missing validation and security issues
* Generate reports

#### Documentation Agent

* Generate README files
* Create API documentation
* Provide setup instructions
* Add code comments

---

## Dashboard

Visual panels display:

* Agent conversations
* Project progression
* Activity feed
* Scrum/Kanban boards
* Progress indicators

---

## Database

Stores:

* Projects (prompts)
* Tasks
* Agent messages
* Code files
* Meetings
* Documents

---

## Future Features

* GitHub integration
* Code execution
* Retrieval-Augmented Generation (RAG)

  * Design patterns
  * Company standards
  * API documentation
* Human approval workflow

---

# Tech Stack

| Component | Technology                 |
| --------- | -------------------------- |
| Frontend  | React                      |
| Backend   | FastAPI, Python            |
| Agents    | LangGraph                  |
| LLM       | OpenAI API or local models |
| Database  | PostgreSQL                 |
| Memory    | Chroma Vector Database     |

---

# Development Schedule

## Week 1

### Chatbot with Memory

* User → LLM interaction
* Create projects
* Save data to database
* Generate requirements

## Week 2

### Multi-Agent Workflow

User → Project Manager Agent → Architecture Agent → Other Agents

## Week 3

### UI Panels

* Chat window
* Requirements panel
* Architecture panel
* Activity feed

## Week 4

### Project Workflows

* Scrum boards
* Task tracking

## Week 5

### Developer Agent

## Week 6

### QA Agent

## Week 7

### Agent Conversations

## Week 8

### Long-Term Memory

## Week 9

### GitHub Integration

---

# Development Log

## Day 1

### Backend Setup

Installed:

```bash
pip install fastapi
pip install uvicorn
pip install sqlalchemy
pip install psycopg2-binary
pip install openai
```

### Initial FastAPI Setup

Created endpoints:

* `GET /`
* `POST /api`

Verified:

* Hardcoded response worked
* User input accepted successfully

### Database Integration

Installed:

* PostgreSQL
* pgAdmin 4

Created:

* Database
* Tables

Created `test_database.py` to verify Python ↔ PostgreSQL connection before integrating FastAPI.

Successfully confirmed:

FastAPI → Database → PostgreSQL

using Swagger UI ("Try it out" and "Execute").

---

## Day 2

### CRUD Operations

Implemented:

#### GET

* Retrieve all projects
* Retrieve a project by ID

#### POST

* Create a new project

### Database Expansion

Added:

#### Project Tasks Table

To support:

* Task tracking
* Agent assignments
* Workflow management

---

# Architecture

```
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
```

---

# Long-Term Goal

Create an autonomous AI software company capable of:

1. Receiving ideas from users.
2. Planning and organizing projects.
3. Designing architectures.
4. Writing code.
5. Testing applications.
6. Generating documentation.
7. Maintaining memory across conversations.
8. Collaborating through multiple specialized agents.
