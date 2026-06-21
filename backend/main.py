from fastapi import FastAPI
from backend.schemas import ProjectIdea, ProjectUpdate, TaskIdea, TaskUpdate
from backend.services.services import save_project, get_projects, get_project, update_project, delete_project
from backend.services.services import save_task, get_tasks, get_task, update_task, delete_task

app = FastAPI()

def load_requirements():
    with open("requirements.txt",
    "r"
    ) as file:
        return file.read()

requirements = load_requirements()

# Get the root (GET)
@app.get("/")
def root():
    return {"message" : "Hello User!"}

# PROJECT FUNCTIONALITIES

# Create a new project (POST)
@app.post("/projects")
def create_project(project: ProjectIdea):
    save_project(project.name, requirements)

    return {
        "project":project.name,
        "requirements":requirements,
    }

# Get all projects (GET)
@app.get("/projects")
def get_all_projects():
    return get_projects()

# Get project by id (GET)
@app.get("/projects/{project_id}")
def get_project_by_id(project_id):
    return get_project(project_id)

# Update project by id (PUT)
@app.put("/projects/{project_id}")
def update_project_by_id(
    project_id: int,
    project: ProjectUpdate
):
    update_project(project_id, project.name, project.requirements)
    return {
        "message":"Project updated!"
    }

# Delete project by id (DELETE)
@app.delete("/projects/{project_id}")
def delete_property_by_id(project_id):
    delete_project(project_id)

    return {
        "message":f"Project with id {project_id} deleted!"
    }

# TASK FUNCTIONALITIES
# Create a new task (POST)
@app.post("/tasks")
def create_task(task: TaskIdea):
    save_task(task.project_id, task.title, task.description, task.status)

    return {
        "project_id":task.project_id,
        "task":task.title,
        "description":task.description,
        "status":task.status
    }

# Get all tasks under one project (GET)
@app.get("/tasks")
def get_all_tasks():
    return get_tasks()

# Get task by id (GET)
@app.get("/tasks/{task_id}")
def get_task_by_id(task_id):
    return get_task(task_id)

# Update task by id (PUT)
@app.put("/tasks/{task_id}")
def update_task_by_id(
    task_id: int,
    task: TaskUpdate
):
    update_task(task_id, task.namtitle, task.description, task.status)
    return {
        "message":"Task updated!"
    }

# Delete task by id (DELETE)
@app.delete("/tasks/{task_id}")
def delete_task_by_id(task_id):
    delete_task(task_id)

    return {
        "message":f"Task with id {task_id} deleted!"
    }